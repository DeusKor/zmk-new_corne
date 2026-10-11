"""Guard artwork-only scope and exact upstream status rendering."""
from pathlib import Path
import hashlib, re
r=Path(__file__).resolve().parents[1]
p=r/'boards/shields/nice_view_baymax'
s=(p/'widgets/peripheral_status.c').read_text()
block=s[s.index('static void draw_top'):s.index('// LVGL callbacks')]
assert hashlib.sha256(block.encode()).hexdigest() == "2163abdebc9188b094dc483d144b586146841f878f313613df44b4aba0bd95e4"
build=(r/'build.yaml').read_text()
assert 'shield: eyelash_corne_left nice_view_focus\n' in build
assert 'shield: eyelash_corne_right nice_view_baymax\n' in build
assert 'lv_timer_pause(timer)' in s and 'k_uptime_get() - widget->last_press > 4000' in s
assert 'ZMK_SUBSCRIPTION(widget_baymax_activity, zmk_position_state_changed)' in s
art=(p/'widgets/baymax.c').read_text()
assert art.count('.header.w=140, .header.h=68') == 3
assert 'LV_IMG_CF_INDEXED_1BIT' in art
assert 'CONFIG_NICE_VIEW_WIDGET_INVERTED' not in art
assert art.count('0,0,0,255, 255,255,255,255,') == 3
print('PASS: unchanged battery/connection drawing, right-only shield, bounded one-bit art and idle pause')

# Inspect the actual packed LVGL bitmaps independently of the generator.
for body in re.findall(r'baymax_\w+_map\[\] = \{(.*?)\};', art, re.S):
    data=list(map(int,re.findall(r'\d+',body)))[8:]
    assert len(data)==18*68
    pixels=[[bool(data[y*18+x//8] & (1 << (7-x%8))) for x in range(140)] for y in range(68)]
    seen=set()
    for y in range(68):
        for x in range(140):
            if not pixels[y][x] or (x,y) in seen:continue
            pending=[(x,y)];seen.add((x,y));count=0
            while pending:
                a,b=pending.pop();count+=1
                for c,d in tuple((a+dx,b+dy) for dx in (-1,0,1) for dy in (-1,0,1) if dx or dy):
                    if 0<=c<140 and 0<=d<68 and pixels[d][c] and (c,d) not in seen:
                        seen.add((c,d));pending.append((c,d))
            assert count>3, 'Detached dark pixels outside the outline'
print('PASS: all packed animation frames are free of detached 1-3 pixel slivers')

focus=(r/'boards/shields/nice_view_focus/widgets/status.c').read_text()
assert 'zmk_wpm' not in focus and 'circle_offsets' not in focus
assert 'state->active_profile_index + 1' in focus
assert all(k in focus for k in ['"LINKED"','"OFFLINE"','"NEW"','"USB"'])
assert 'display-name = "BT"' in (r/'config/eyelash_corne.keymap').read_text()
print('PASS: compact selected-slot status, no WPM graph, BT layer name')

import json
quotes=(r/'boards/shields/nice_view_focus/widgets/quotes.h').read_text()
messages=[json.loads(line.strip().rstrip(',')) for line in quotes.splitlines() if line.strip().startswith('"')]
assert len(messages)==100 and len(set(messages))==100
assert all(len(q.splitlines())<=5 and all(len(line)<=11 for line in q.splitlines()) for q in messages)
assert 'sys_rand32_get() % ARRAY_SIZE(focus_quotes)' in focus
print('PASS: 100 unique startup quotes fit the 68x68 small-font region')

for shield in ("nice_view_focus", "nice_view_baymax"):
    assert "CONFIG_NICE_VIEW_WIDGET_INVERTED=y" in (r / "boards/shields" / shield / f"{shield}.conf").read_text()

# Outline interiors must remain unfilled in the actual packed image.
for body in re.findall(r"baymax_\w+_map\[\] = \{(.*?)\};", art, re.S):
    data=list(map(int,re.findall(r"\d+",body)))[8:]
    assert sum(byte.bit_count() for byte in data) < 1000
