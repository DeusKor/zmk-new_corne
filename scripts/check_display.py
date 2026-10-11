"""Guard artwork-only scope and exact upstream status rendering."""
from pathlib import Path
import hashlib, re
r=Path(__file__).resolve().parents[1]
p=r/'boards/shields/nice_view_baymax'
s=(p/'widgets/peripheral_status.c').read_text()
block=s[s.index('static void draw_top'):s.index('// LVGL callbacks')]
assert hashlib.sha256(block.encode()).hexdigest() == "2163abdebc9188b094dc483d144b586146841f878f313613df44b4aba0bd95e4"
build=(r/'build.yaml').read_text()
assert 'shield: eyelash_corne_left nice_view\n' in build
assert 'shield: eyelash_corne_right nice_view_baymax\n' in build
assert 'lv_timer_pause(timer)' in s and 'k_uptime_get() - widget->last_press > 4000' in s
assert 'ZMK_SUBSCRIPTION(widget_baymax_activity, zmk_position_state_changed)' in s
art=(p/'widgets/baymax.c').read_text()
assert art.count('.header.w=140, .header.h=68') == 3
assert 'LV_IMG_CF_INDEXED_1BIT' in art
print('PASS: unchanged battery/connection drawing, right-only shield, bounded one-bit art and idle pause')
