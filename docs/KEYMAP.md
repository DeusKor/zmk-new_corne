# Keymap reference

US host layout; 48 positions, including six thumbs, a five-way switch and encoder press. Physical hardware identity remains to be confirmed before flashing.

## Typing thumbs (BASE / EXT / SYM / BT)

| Reach | Left | Right |
|---|---|---|
| Inner | Command (44) | Space (45) |
| Middle | Option (43) | Backspace (46) |
| Outer | Ctrl (42) | Hold EXT (47) |

Typing Enter is the BASE comma+period combo; no dedicated Enter on typing layers. Hold the bottom-right outer finger key (41) from BASE for SYM (the third typing layer). Encoder press plays/pauses media on typing layers; rotation still controls volume. Hold the top outer right key (12) for BT. The outer left column is Esc/Tab/Shift, top to bottom, on every layer.

EXT combines A/S/D/F arrows on the left with the right-hand numpad: U/I/O = 7/8/9, J/K/L = 4/5/6, M/comma/period = 1/2/3, N = 0 and slash = decimal. Division, multiplication, plus and minus surround the grid. Modifiers are on the left thumbs and Shift is on the bottom-left key. No Home/End/Page keys. F1–F5 and F11–F12 remain on the left. Left-thumb Option plus right-thumb Backspace works directly on BASE. For Option+arrows, hold right-thumb EXT, left-thumb Option, then use A/S/D/F. Cmd+A/C/V/Z can use left inner-thumb Cmd directly. If EXT is already held, keep left-thumb Cmd down, release EXT, then press the BASE letter; the fork routes releases to the original press layer. Physical event testing remains pending.

BASE combos: W+E Escape; I+O Backspace; X+C Tab; comma+period Enter. Press within 40 ms after 150 ms without typing. Combos are BASE-only. For Enter after using SYM/BT/EXT, release that layer first. Left-thumb Option remains usable with the right-hand Backspace combo on BASE.

BT retains the same numpad plus connection and power controls: U/I/O = 7/8/9, J/K/L = 4/5/6, M/comma/period = 1/2/3; N = 0, slash = decimal. Left A/S/D/F remain letters; use thumb modifiers for modified numbers. BT+G selects USB, BT+quote Bluetooth; On layer 3, Q/W/E/R/T select Bluetooth slots 1–5 (internal indices 0–4). The old X/C/V/B selectors are restored to letters. BT+Z unlocks Studio. BT+bottom outer right held for two seconds soft-powers off; hardware reset wakes it. No pairing-clear keys.

GAME remains separately optimized: plain movement/ability keys and dedicated modifiers, left-thumb number access, right-thumb Backspace and dedicated Enter. Its outer left column is Esc/Tab/Shift; Ctrl is at right semicolon. GAME NUM places 1–5 on Q–T and 6–0 on A–G. Bottom outer right exits to BASE. Release held keys before switching. No gaming combos or hold-taps.

Joystick directions move the mouse on every layer. Centre left-clicks, EXT centre right-clicks, SYM centre middle-clicks. Existing maximum movement speed 1200 is retained; centre+direction dragging depends on the physical switch. Encoder volume is unchanged.

## Position reference

| Position | BASE | EXT | SYM | BT | GAME | GAME NUM |
|---|---|---|---|---|---|---|
| 0 | ESC | ESC | ESC | ESC | ESC | ESC |
| 1 | Q | F1 | EXCL | bt BT_SEL 0 | Q | N1 |
| 2 | W | F2 | AT | bt BT_SEL 1 | W | N2 |
| 3 | E | F3 | HASH | bt BT_SEL 2 | E | N3 |
| 4 | R | F4 | DLLR | bt BT_SEL 3 | R | N4 |
| 5 | T | F5 | PRCNT | bt BT_SEL 4 | T | N5 |
| 6 | mmv MOVE_UP | mmv MOVE_UP | mmv MOVE_UP | mmv MOVE_UP | mmv MOVE_UP | mmv MOVE_UP |
| 7 | Y | FSLH | CARET | FSLH | N1 | N1 |
| 8 | U | N7 | AMPS | N7 | N2 | N2 |
| 9 | I | N8 | ASTRK | N8 | N3 | N3 |
| 10 | O | N9 | LPAR | N9 | N4 | N4 |
| 11 | P | ASTRK | RPAR | ASTRK | N5 | N5 |
| 12 | mo BT | mo BT | mo BT | trans | N6 | N6 |
| 13 | TAB | TAB | TAB | TAB | TAB | TAB |
| 14 | A | LEFT | GRAVE | A | A | N6 |
| 15 | S | DOWN | TILDE | S | S | N7 |
| 16 | D | UP | LBKT | D | D | N8 |
| 17 | F | RIGHT | RBKT | F | F | N9 |
| 18 | G | DEL | BSLH | out OUT_USB | G | N0 |
| 19 | mmv MOVE_LEFT | mmv MOVE_LEFT | mmv MOVE_LEFT | mmv MOVE_LEFT | mmv MOVE_LEFT | mmv MOVE_LEFT |
| 20 | mkp LCLK | mkp RCLK | mkp MCLK | mkp LCLK | mkp LCLK | mkp LCLK |
| 21 | mmv MOVE_RIGHT | mmv MOVE_RIGHT | mmv MOVE_RIGHT | mmv MOVE_RIGHT | mmv MOVE_RIGHT | mmv MOVE_RIGHT |
| 22 | H | PLUS | MINUS | PLUS | N7 | N7 |
| 23 | J | N4 | EQUAL | N4 | N8 | N8 |
| 24 | K | N5 | LBRC | N5 | N9 | N9 |
| 25 | L | N6 | RBRC | N6 | N0 | N0 |
| 26 | SEMI | MINUS | PIPE | MINUS | LCTRL | LCTRL |
| 27 | SQT | SQT | DQT | out OUT_BLE | SQT | SQT |
| 28 | LSHFT | LSHFT | LSHFT | LSHFT | LSHFT | LSHFT |
| 29 | Z | F11 | LT | studio_unlock | Z | Z |
| 30 | X | F12 | GT | X | X | X |
| 31 | C | C | LPAR | C | C | C |
| 32 | V | V | RPAR | V | V | V |
| 33 | B | B | UNDER | B | B | B |
| 34 | C_PP | C_PP | C_PP | C_PP | SPACE | SPACE |
| 35 | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN | mmv MOVE_DOWN |
| 36 | N | N0 | PLUS | N0 | N | N |
| 37 | M | N1 | EQUAL | N1 | M | M |
| 38 | COMMA | N2 | COMMA | N2 | COMMA | COMMA |
| 39 | DOT | N3 | DOT | N3 | DOT | DOT |
| 40 | FSLH | DOT | FSLH | DOT | FSLH | FSLH |
| 41 | mo SYM | to GAME | trans | soft_off | to BASE | to BASE |
| 42 | LCTRL | LCTRL | LCTRL | LCTRL | LALT | LALT |
| 43 | LALT | LALT | LALT | LALT | mo GAME_NUM | mo GAME_NUM |
| 44 | LGUI | LGUI | LGUI | LGUI | SPACE | SPACE |
| 45 | SPACE | SPACE | SPACE | SPACE | BSPC | BSPC |
| 46 | BSPC | BSPC | BSPC | BSPC | RSHFT | RSHFT |
| 47 | mo EXT | trans | mo EXT | mo EXT | ENTER | ENTER |

Thumb positions: left outer→inner 42,43,44; right inner→outer 45,46,47. Other positions follow `config/eyelash_corne.json`.

## Right display artwork

The right half uses Baymax artwork with brief blinks on right-half key activity and a rare wave (every tenth animation) and a static rest image when idle. Existing battery, charging and split-connection indicators are unchanged; the left display is unchanged. See `boards/shields/nice_view_baymax/README.md`.

The left display uses a compact selected-output header: USB, or BT 1–5 with LINKED/OFFLINE/NEW. Battery and active layer remain visible. WPM and the five-slot diagram are removed; the middle area is available for affirmations. No affirmation list is installed yet.
