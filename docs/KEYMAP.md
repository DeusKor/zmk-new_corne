# Keymap reference

US host layout. The supplied 48-position physical layout has six thumbs; physical hardware identity still needs confirmation.

## Typing thumbs (BASE / EXT / SYM / NUM)

| Reach | Left | Right |
|---|---|---|
| Inner | Space (44) | Enter (45) |
| Middle | Backspace (43) | Hold EXT (46) |
| Outer | Option (42) | Hold SYM (47) |

NUM is held at position 12, the top outer right finger key. EXT is momentary, not a toggle.

EXT: A/S/D/F = Left/Down/Up/Right; J/K/L/semicolon = Shift/Cmd/Option/Ctrl. Hold right-thumb EXT, hold Option with the right ring finger, then use left-hand arrows or left-thumb Backspace. Home, End and Page keys are removed. F1–F12 remain available. EXT+bottom outer right enters GAME.

For Cmd+A: hold right-thumb EXT, press and keep holding K (Cmd), release EXT, press A, then release A and K. Cmd+C/V/Z works the same way. The fork remembers the pressed key's layer for release, so the original Cmd releases even though K has reverted to a letter. Physical event testing remains necessary before declaring the sequence verified on the device.

Left outer thumb Option is available on BASE: hold it and use right I+O for Option+Backspace without activating a layer. BASE combos: W+E Escape; I+O Backspace; X+C Tab; comma+period Enter. Press within 40 ms after 150 ms without typing. Combos are disabled on all other layers.

NUM: U/I/O = 7/8/9, J/K/L = 4/5/6, M/comma/period = 1/2/3; N = 0, slash = decimal. A/S/D/F = Ctrl/Alt/Cmd/Shift. NUM+G selects USB; NUM+quote selects Bluetooth. Bluetooth profiles 0–3, Studio unlock and two-second soft-off are retained. No pairing-clear bindings. Wake from soft-off using the hardware reset button.

GAME keeps its previously configured dedicated modifiers, left-thumb number access, Space and right-thumb Backspace. GAME NUM puts 1–5 on Q–T and 6–0 on A–G. Bottom outer right exits either gaming layer to BASE. Release held keys before switching modes. Gaming has no combos or hold-tap behaviors.

Joystick: directions move the mouse on every layer. Centre left-clicks, EXT centre right-clicks, SYM centre middle-clicks. Existing maximum mouse speed 1200 is retained. Centre+direction dragging depends on the physical switch permitting simultaneous presses. Encoder volume is unchanged.

## Position reference

| Position | BASE | EXT | SYM | NUM | GAME | GAME NUM |
|---|---|---|---|---|---|---|
| 0 | TAB | TAB | TAB | TAB | ESC | ESC |
| 1 | Q | F1 | EXCL | N1 | Q | N1 |
| 2 | W | F2 | AT | N2 | W | N2 |
| 3 | E | F3 | HASH | N3 | E | N3 |
| 4 | R | F4 | DLLR | N4 | R | N4 |
| 5 | T | F5 | PRCNT | N5 | T | N5 |
| 6 | mmv MOVE_UP | mmv MOVE_UP | mmv MOVE_UP | mmv MOVE_UP | mmv MOVE_UP | mmv MOVE_UP |
| 7 | Y | F6 | CARET | FSLH | N1 | N1 |
| 8 | U | F7 | AMPS | N7 | N2 | N2 |
| 9 | I | F8 | ASTRK | N8 | N3 | N3 |
| 10 | O | F9 | LPAR | N9 | N4 | N4 |
| 11 | P | F10 | RPAR | ASTRK | N5 | N5 |
| 12 | mo NUM | mo NUM | mo NUM | trans | N6 | N6 |
| 13 | LSHFT | LSHFT | LSHFT | LSHFT | LSHFT | LSHFT |
| 14 | A | LEFT | GRAVE | LCTRL | A | N6 |
| 15 | S | DOWN | TILDE | LALT | S | N7 |
| 16 | D | UP | LBKT | LGUI | D | N8 |
| 17 | F | RIGHT | RBKT | LSHFT | F | N9 |
| 18 | G | DEL | BSLH | out OUT_USB | G | N0 |
| 19 | mmv MOVE_LEFT | mmv MOVE_LEFT | mmv MOVE_LEFT | mmv MOVE_LEFT | mmv MOVE_LEFT | mmv MOVE_LEFT |
| 20 | mkp LCLK | mkp RCLK | mkp MCLK | mkp LCLK | mkp LCLK | mkp LCLK |
| 21 | mmv MOVE_RIGHT | mmv MOVE_RIGHT | mmv MOVE_RIGHT | mmv MOVE_RIGHT | mmv MOVE_RIGHT | mmv MOVE_RIGHT |
| 22 | H | ESC | MINUS | PLUS | N7 | N7 |
| 23 | J | LSHFT | EQUAL | N4 | N8 | N8 |
| 24 | K | LGUI | LBRC | N5 | N9 | N9 |
| 25 | L | LALT | RBRC | N6 | N0 | N0 |
| 26 | SEMI | LCTRL | PIPE | MINUS | TAB | TAB |
| 27 | SQT | INS | DQT | out OUT_BLE | SQT | SQT |
| 28 | LCTRL | LCTRL | LCTRL | LCTRL | LCTRL | LCTRL |
| 29 | Z | F11 | LT | LALT | Z | Z |
| 30 | X | F12 | GT | bt BT_SEL 0 | X | X |
| 31 | C | C | LPAR | bt BT_SEL 1 | C | C |
| 32 | V | V | RPAR | bt BT_SEL 2 | V | V |
| 33 | B | B | UNDER | bt BT_SEL 3 | B | B |
| 34 | SPACE | SPACE | SPACE | studio_unlock | SPACE | SPACE |
| 35 | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN |
| 36 | N | N | PLUS | N0 | N | N |
| 37 | M | M | EQUAL | N1 | M | M |
| 38 | COMMA | COMMA | COMMA | N2 | COMMA | COMMA |
| 39 | DOT | DOT | DOT | N3 | DOT | DOT |
| 40 | FSLH | DEL | FSLH | DOT | FSLH | FSLH |
| 41 | ESC | to GAME | ESC | soft_off | to BASE | to BASE |
| 42 | LALT | LALT | LALT | LALT | LALT | LALT |
| 43 | BSPC | BSPC | BSPC | BSPC | mo GAME_NUM | mo GAME_NUM |
| 44 | SPACE | SPACE | SPACE | SPACE | SPACE | SPACE |
| 45 | ENTER | ENTER | ENTER | ENTER | BSPC | BSPC |
| 46 | mo EXT | trans | mo EXT | mo EXT | RSHFT | RSHFT |
| 47 | mo SYM | mo SYM | trans | mo SYM | ENTER | ENTER |

Thumb positions: left outer→inner 42,43,44; right inner→outer 45,46,47. Other positions follow `config/eyelash_corne.json`, including joystick and encoder press.
