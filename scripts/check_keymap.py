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
assert all(bs[45] == '&kp BSPC' for bs in bindings.values())
game = bindings['game']
for layer in ('game', 'game_num'):
    assert all(b.startswith('&kp ') or b in ('&to BASE', '&mo GAME_NUM') for b in bindings[layer])
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
