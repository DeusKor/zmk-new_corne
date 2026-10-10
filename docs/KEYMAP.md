# Keymap reference

US host layout. Three thumbs per half; position 45 is the inner right thumb in the supplied physical layout. Hardware identity still needs physical confirmation.

Hold EXT (left middle thumb) and tap position 41 (bottom outer right) to enter GAME. Tap position 41 alone to exit GAME. Release held keys before switching modes. GAME has dedicated left Shift, Ctrl and Alt; digits 1–6 are on the right top row and 7–0 on its home row. Hold the left middle thumb for GAME NUM: left Q–T become 1–5 and A–G become 6–0, so numbers are available without leaving the mouse. Left Ctrl remains at position 28. No timed key behaviors are used.

BASE combos: W+E Escape; I+O Backspace; X+C Tab; comma+period Enter. Press within 40 ms after 150 ms without typing. Combos are disabled on other layers. This idle guard reduces accidental typing rolls; pause before an intentional chord.

NUM is held at position 12 (top outer right). USB/BLE selection, Bluetooth profiles 0–3, Studio unlock and a two-second soft-off are on NUM. No pairing-clear bindings remain. Wake from soft-off using the hardware reset button. Encoder volume is unchanged.

EXT places Left/Down/Up/Right directly on A/S/D/F. Hold the left middle thumb to navigate. NUM has a right-hand numpad one column farther right: U/I/O = 7/8/9, J/K/L = 4/5/6, M/comma/period = 1/2/3; N = 0, slash = decimal. Enter and Backspace stay on their thumbs. Use NUM alone for numbers, EXT alone for navigation.

| Position | BASE | EXT | SYM | NUM | GAME | GAME NUM |
|---|---|---|---|---|---|---|
| 0 | TAB | TAB | TAB | TAB | ESC | ESC |
| 1 | Q | F1 | EXCL | N1 | Q | N1 |
| 2 | W | F2 | AT | N2 | W | N2 |
| 3 | E | F3 | HASH | N3 | E | N3 |
| 4 | R | F4 | DLLR | N4 | R | N4 |
| 5 | T | F5 | PRCNT | N5 | T | N5 |
| 6 | UP | UP | UP | UP | UP | UP |
| 7 | Y | F6 | CARET | FSLH | N1 | FSLH |
| 8 | U | F7 | AMPS | N7 | N2 | N7 |
| 9 | I | F8 | ASTRK | N8 | N3 | N8 |
| 10 | O | F9 | LPAR | N9 | N4 | N9 |
| 11 | P | F10 | RPAR | ASTRK | N5 | ASTRK |
| 12 | mo NUM | mo NUM | mo NUM | trans | N6 | N6 |
| 13 | LSHFT | LSHFT | LSHFT | LSHFT | LSHFT | LSHFT |
| 14 | A | LEFT | GRAVE | out OUT_USB | A | out OUT_USB |
| 15 | S | DOWN | TILDE | out OUT_BLE | S | out OUT_BLE |
| 16 | D | UP | LBKT | F8 | D | N8 |
| 17 | F | RIGHT | RBKT | F9 | F | N9 |
| 18 | G | DEL | BSLH | F10 | G | N0 |
| 19 | LEFT | LEFT | LEFT | LEFT | LEFT | LEFT |
| 20 | ENTER | ENTER | ENTER | ENTER | ENTER | ENTER |
| 21 | RIGHT | RIGHT | RIGHT | RIGHT | RIGHT | RIGHT |
| 22 | H | LEFT | MINUS | SQT | N7 | SQT |
| 23 | J | DOWN | EQUAL | N4 | N8 | N4 |
| 24 | K | UP | LBRC | N5 | N9 | N5 |
| 25 | L | RIGHT | RBRC | N6 | N0 | N6 |
| 26 | SEMI | DEL | PIPE | MINUS | TAB | MINUS |
| 27 | SQT | INS | DQT | PLUS | SQT | PLUS |
| 28 | LCTRL | LCTRL | LCTRL | LCTRL | LCTRL | LCTRL |
| 29 | Z | F11 | LT | LALT | Z | LALT |
| 30 | X | F12 | GT | bt BT_SEL 0 | X | X |
| 31 | C | C | LPAR | bt BT_SEL 1 | C | C |
| 32 | V | V | RPAR | bt BT_SEL 2 | V | V |
| 33 | B | B | UNDER | bt BT_SEL 3 | B | B |
| 34 | SPACE | SPACE | SPACE | studio_unlock | SPACE | SPACE |
| 35 | DOWN | DOWN | DOWN | DOWN | DOWN | DOWN |
| 36 | N | HOME | PLUS | N0 | N | N0 |
| 37 | M | END | EQUAL | N1 | M | N1 |
| 38 | COMMA | PG_DN | COMMA | N2 | COMMA | N2 |
| 39 | DOT | PG_UP | DOT | N3 | DOT | N3 |
| 40 | FSLH | RALT | FSLH | DOT | FSLH | DOT |
| 41 | ESC | to GAME | ESC | soft_off | to BASE | to BASE |
| 42 | LGUI | LGUI | LGUI | LGUI | LALT | LALT |
| 43 | mo EXT | trans | mo EXT | mo EXT | mo GAME_NUM | mo GAME_NUM |
| 44 | SPACE | SPACE | SPACE | SPACE | SPACE | SPACE |
| 45 | BSPC | BSPC | BSPC | BSPC | BSPC | BSPC |
| 46 | mo SYM | mo SYM | trans | mo SYM | RSHFT | RSHFT |
| 47 | ENTER | ENTER | ENTER | ENTER | ENTER | ENTER |

Thumb positions: left outer→inner 42,43,44; right inner→outer 45,46,47. Other positions follow `config/eyelash_corne.json`, including the five-way control and encoder press.

The unavailable 34-key reference is inspiration only: this adaptation retains all 48 hardware positions and QWERTY. EXT supplies navigation and F1–F12; SYM supplies coding symbols; NUM supplies numbers and device controls.

GAME NUM otherwise duplicates GAME, including plain modifiers and the exit key. Releasing the thumb returns immediately to GAME.
