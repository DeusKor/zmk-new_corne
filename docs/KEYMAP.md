# Keymap reference

US host layout; 48 positions, including six thumbs, a five-way switch and encoder press. Physical hardware identity remains to be confirmed before flashing.

## Typing thumbs (BASE / EXT / SYM / NUM)

| Reach | Left | Right |
|---|---|---|
| Inner | Command (44) | Space (45) |
| Middle | Option (43) | Backspace (46) |
| Outer | Ctrl (42) | Hold EXT (47) |

Typing Enter is the BASE comma+period combo; no dedicated Enter on typing layers. Hold the encoder-press key (34) for SYM; rotation still controls volume. Hold the top outer right key (12) for NUM. The outer left column is Esc/Tab/Shift, top to bottom, on every layer.

EXT has A/S/D/F arrows and J/K/L/semicolon = Shift/Cmd/Option/Ctrl. No Home/End/Page keys. F1–F12 remain. Left-thumb Option plus right-thumb Backspace works directly on BASE. For Option+arrows, hold right-thumb EXT, left-thumb Option, then use A/S/D/F. Cmd+A/C/V/Z can use left inner-thumb Cmd directly. Alternatively, hold EXT, hold K (Cmd), release EXT, then press the letter and release K; the fork routes releases to the original press layer. Physical event testing remains pending.

BASE combos: W+E Escape; I+O Backspace; X+C Tab; comma+period Enter. Press within 40 ms after 150 ms without typing. Combos are BASE-only. For Enter after using SYM/NUM/EXT, release that layer first. Left-thumb Option remains usable with the right-hand Backspace combo on BASE.

NUM: U/I/O = 7/8/9, J/K/L = 4/5/6, M/comma/period = 1/2/3; N = 0, slash = decimal. A/S/D/F = Ctrl/Alt/Cmd/Shift. NUM+G selects USB, NUM+quote Bluetooth; X/C/V/B select Bluetooth profiles 0–3. NUM+Z unlocks Studio. NUM+bottom outer right held for two seconds soft-powers off; hardware reset wakes it. No pairing-clear keys.

GAME remains separately optimized: plain movement/ability keys and dedicated modifiers, left-thumb number access, right-thumb Backspace and dedicated Enter. Its outer left column is Esc/Tab/Shift; Ctrl is at right semicolon. GAME NUM places 1–5 on Q–T and 6–0 on A–G. Bottom outer right exits to BASE. Release held keys before switching. No gaming combos or hold-taps.

Joystick directions move the mouse on every layer. Centre left-clicks, EXT centre right-clicks, SYM centre middle-clicks. Existing maximum movement speed 1200 is retained; centre+direction dragging depends on the physical switch. Encoder volume is unchanged.

## Position reference

| Position | BASE | EXT | SYM | NUM | GAME | GAME NUM |
|---|---|---|---|---|---|---|
| 0 | ESC | ESC | ESC | ESC | ESC | ESC |
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
| 13 | TAB | TAB | TAB | TAB | TAB | TAB |
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
| 26 | SEMI | LCTRL | PIPE | MINUS | LCTRL | LCTRL |
| 27 | SQT | INS | DQT | out OUT_BLE | SQT | SQT |
| 28 | LSHFT | LSHFT | LSHFT | LSHFT | LSHFT | LSHFT |
| 29 | Z | F11 | LT | studio_unlock | Z | Z |
| 30 | X | F12 | GT | bt BT_SEL 0 | X | X |
| 31 | C | C | LPAR | bt BT_SEL 1 | C | C |
| 32 | V | V | RPAR | bt BT_SEL 2 | V | V |
| 33 | B | B | UNDER | bt BT_SEL 3 | B | B |
| 34 | mo SYM | mo SYM | trans | mo SYM | SPACE | SPACE |
| 35 | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN |
| 36 | N | N | PLUS | N0 | N | N |
| 37 | M | M | EQUAL | N1 | M | M |
| 38 | COMMA | COMMA | COMMA | N2 | COMMA | COMMA |
| 39 | DOT | DOT | DOT | N3 | DOT | DOT |
| 40 | FSLH | DEL | FSLH | DOT | FSLH | FSLH |
| 41 | ESC | to GAME | ESC | soft_off | to BASE | to BASE |
| 42 | LCTRL | LCTRL | LCTRL | LCTRL | LALT | LALT |
| 43 | LALT | LALT | LALT | LALT | mo GAME_NUM | mo GAME_NUM |
| 44 | LGUI | LGUI | LGUI | LGUI | SPACE | SPACE |
| 45 | SPACE | SPACE | SPACE | SPACE | BSPC | BSPC |
| 46 | BSPC | BSPC | BSPC | BSPC | RSHFT | RSHFT |
| 47 | mo EXT | trans | mo EXT | mo EXT | ENTER | ENTER |

Thumb positions: left outer→inner 42,43,44; right inner→outer 45,46,47. Other positions follow `config/eyelash_corne.json`.
