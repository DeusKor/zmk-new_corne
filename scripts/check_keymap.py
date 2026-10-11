"""Static safety checks; firmware and physical event tests are separate."""
from pathlib import Path
import re
p = Path(__file__).resolve().parents[1]
s = (p / 'config/eyelash_corne.keymap').read_text()
layers = dict(re.findall(r'(\w+)_layer\s*\{.*?bindings\s*=\s*<(.*?)>;', s, re.S))
bindings = {n: re.findall(r'&\w+(?:\s+[^&]+)?', b) for n, b in layers.items()}
bindings = {n: [' '.join(b.split()) for b in bs] for n, bs in bindings.items()}
assert list(bindings) == ['base', 'ext', 'sym', 'num', 'game', 'game_num']
transform = (p / 'boards/shields/eyelash_corne/eyelash_corne.dtsi').read_text().split('map = <')[1].split('>;')[0]
assert len(re.findall(r'RC\(', transform)) == 48
assert all(len(bs) == 48 for bs in bindings.values())
for layer in ('base', 'ext', 'sym', 'num'):
    assert bindings[layer][42:47] == ['&kp LCTRL', '&kp LALT', '&kp LGUI', '&kp SPACE', '&kp BSPC']
    assert '&kp ENTER' not in bindings[layer]
assert bindings['base'][47] == '&mo EXT'
assert bindings['base'][41] == '&mo SYM'
assert all(bindings[layer][34] == '&kp C_PP' for layer in ('base','ext','sym','num'))
assert bindings['ext'][47] == '&trans' and bindings['sym'][41] == '&trans'
assert all(k not in bindings['ext'] for k in ['&kp HOME', '&kp END', '&kp PG_UP', '&kp PG_DN'])
game = bindings['game']
for layer in ('game', 'game_num'):
    assert all(b.startswith('&kp ') or b in ('&to BASE', '&mo GAME_NUM') for i, b in enumerate(bindings[layer]) if i not in (6,19,20,21,35))
    assert bindings[layer][41] == '&to BASE'
    assert bindings[layer][43] == '&mo GAME_NUM'
assert [bindings['game_num'][i] for i in [1,2,3,4,5,14,15,16,17,18]] == ['&kp N'+str(i) for i in [1,2,3,4,5,6,7,8,9,0]]
for i, key in {1:'Q',2:'W',3:'E',4:'R',14:'A',15:'S',16:'D',17:'F'}.items():
    assert game[i] == '&kp ' + key
assert all('&kp N' + str(i) in game for i in range(10))
assert all('&kp '+k in game for k in ['LSHFT','LCTRL','LALT'])
assert game[41] == '&to BASE' and bindings['ext'][41] == '&to GAME'
expected = {(2,3): ('W','E','ESC'), (9,10): ('I','O','BSPC'), (30,31): ('X','C','TAB'), (38,39): ('COMMA','DOT','ENTER')}
combos = re.findall(r'combo_\w+\s*\{(.*?)\};', s, re.S)
assert len(combos) == 4
for c in combos:
    pos = tuple(map(int,re.search(r'key-positions = <(.*?)>',c)[1].split()))
    a,b,result = expected.pop(pos)
    assert [bindings['base'][i] for i in pos] == ['&kp '+a,'&kp '+b]
    assert 'layers = <BASE>' in c and 'bindings = <&kp '+result+'>' in c
assert not expected
assert 'BT_CLR' not in s and 'settings_reset' not in s
assert '&soft_off' not in ' '.join(game)
print('PASS: positions, layer sizes, combos, gaming bindings, exit, modifiers and pairing guards')

# Left-hand navigation and right-shifted numpad follow physical letter positions.
assert [bindings['base'][i] for i in [14,15,16,17]] == ['&kp '+k for k in ['A','S','D','F']]
assert [bindings['ext'][i] for i in [14,15,16,17]] == ['&kp '+k for k in ['LEFT','DOWN','UP','RIGHT']]
for positions, letters, digits in [([8,9,10], ['U','I','O'], [7,8,9]), ([23,24,25], ['J','K','L'], [4,5,6]), ([37,38,39], ['M','COMMA','DOT'], [1,2,3])]:
    assert [bindings['base'][i] for i in positions] == ['&kp '+k for k in letters]
    assert [bindings['num'][i] for i in positions] == ['&kp N'+str(k) for k in digits]
assert bindings['num'][36] == '&kp N0'
assert bindings['num'][40] == '&kp DOT'
print('PASS: ASDF arrows and shifted UIO/JKL/M-comma-period numpad')

for i in [7,8,9,10,11,22,23,24,25,26,36,37,38,39,40]:
    assert bindings['ext'][i] == bindings['num'][i]
assert [bindings['num'][i] for i in [14,15,16,17]] == ['&kp '+k for k in ['A','S','D','F']]
assert '&out OUT_USB' in bindings['num'] and '&out OUT_BLE' in bindings['num']
print('PASS: restored home-row letters and output selection')

# Joystick identity comes from the editor's physical layout, not letter positions.
import json
physical = json.loads((p / 'config/eyelash_corne.json').read_text())['layouts']['default_layout']['layout']
for pos, direction in {6:'up',19:'left',21:'right',35:'down'}.items():
    assert physical[pos]['label'] == '5-way '+direction
    assert all(bs[pos] == '&mmv MOVE_'+direction.upper() for bs in bindings.values())
assert physical[20]['label'] == '5-way press'
for layer, bs in bindings.items():
    assert bs[20] == '&mkp '+{'ext':'RCLK','sym':'MCLK'}.get(layer,'LCLK')
assert 'CONFIG_ZMK_POINTING=y' in (p / 'config/eyelash_corne.conf').read_text()
print('PASS: joystick directions, layer clicks and existing mouse support')

# Cmd is a plain thumb key; letters are restored after releasing EXT.
assert bindings['ext'][44] == '&kp LGUI'
assert bindings['base'][14] == '&kp A'
assert bindings['base'][43] == '&kp LALT'
assert bindings['base'][44] == '&kp LGUI'
print('PASS: left Ctrl/Option/Cmd, right Space/Backspace, EXT/SYM access and combo-only Enter')

assert [physical[i]['row'] for i in [0,13,28]] == [0,1,2]
assert all(physical[i]['col'] == 0 for i in [0,13,28])
assert all([bs[i] for i in [0,13,28]] == ['&kp ESC','&kp TAB','&kp LSHFT'] for bs in bindings.values())
assert all(bindings[n][26] == '&kp LCTRL' for n in ['game','game_num'])
print('PASS: outer left Esc/Tab/Shift on all layers and dedicated game Ctrl')

assert bindings['num'][1:6] == ['&bt BT_SEL '+str(i) for i in range(5)]
assert bindings['num'][30:34] == ['&kp '+k for k in 'XCVB']
print('PASS: all five Bluetooth slots on the settings top row, no duplicate lower-row selectors')
