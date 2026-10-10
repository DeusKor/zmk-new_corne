# Keymap reference

US host layout. Three thumbs per half; position 45 is the inner right thumb in the supplied physical layout. Hardware identity still needs physical confirmation.

Hold EXT (left middle thumb) and tap position 41 (bottom outer right) to enter GAME. Tap position 41 alone to exit GAME. Release held keys before switching modes. GAME has dedicated left Shift, Ctrl and Alt; digits 1–6 are on the right top row and 7–0 on its home row. No timed key behaviors are used.

BASE combos: W+E Escape; I+O Backspace; X+C Tab; comma+period Enter. Press within 40 ms after 150 ms without typing. Combos are disabled on other layers. This idle guard reduces accidental typing rolls; pause before an intentional chord.

NUM is held at position 12 (top outer right). USB/BLE selection, Bluetooth profiles 0–3, Studio unlock and a two-second soft-off are on NUM. No pairing-clear bindings remain. Wake from soft-off using the hardware reset button. Encoder volume is unchanged.

| Position | BASE | EXT | SYM | NUM | GAME |
|---|---|---|---|---|---|
| 0 | TAB | TAB | TAB | TAB | ESC |
| 1 | Q | F1 | EXCL | N1 | Q |
| 2 | W | F2 | AT | N2 | W |
| 3 | E | F3 | HASH | N3 | E |
| 4 | R | F4 | DLLR | N4 | R |
| 5 | T | F5 | PRCNT | N5 | T |
| 6 | UP | UP | UP | UP | UP |
| 7 | Y | HOME | CARET | N6 | N1 |
| 8 | U | PG_DN | AMPS | N7 | N2 |
| 9 | I | PG_UP | ASTRK | N8 | N3 |
| 10 | O | END | LPAR | N9 | N4 |
| 11 | P | DEL | RPAR | N0 | N5 |
| 12 | mo NUM | mo NUM | mo NUM | trans | N6 |
| 13 | LSHFT | LSHFT | LSHFT | LSHFT | LSHFT |
| 14 | A | F6 | GRAVE | F6 | A |
| 15 | S | F7 | TILDE | F7 | S |
| 16 | D | F8 | LBKT | F8 | D |
| 17 | F | F9 | RBKT | F9 | F |
| 18 | G | F10 | BSLH | F10 | G |
| 19 | LEFT | LEFT | LEFT | LEFT | LEFT |
| 20 | ENTER | ENTER | ENTER | ENTER | ENTER |
| 21 | RIGHT | RIGHT | RIGHT | RIGHT | RIGHT |
| 22 | H | LEFT | MINUS | N4 | N7 |
| 23 | J | DOWN | EQUAL | N5 | N8 |
| 24 | K | UP | LBRC | N6 | N9 |
| 25 | L | RIGHT | RBRC | PLUS | N0 |
| 26 | SEMI | DEL | PIPE | MINUS | TAB |
| 27 | SQT | INS | DQT | SQT | SQT |
| 28 | LCTRL | LCTRL | LCTRL | out OUT_USB | LCTRL |
| 29 | Z | F11 | LT | out OUT_BLE | Z |
| 30 | X | F12 | GT | bt BT_SEL 0 | X |
| 31 | C | C | LPAR | bt BT_SEL 1 | C |
| 32 | V | V | RPAR | bt BT_SEL 2 | V |
| 33 | B | B | UNDER | bt BT_SEL 3 | B |
| 34 | SPACE | SPACE | SPACE | studio_unlock | SPACE |
| 35 | DOWN | DOWN | DOWN | DOWN | DOWN |
| 36 | N | HOME | PLUS | N1 | N |
| 37 | M | END | EQUAL | N2 | M |
| 38 | COMMA | PG_DN | COMMA | N3 | COMMA |
| 39 | DOT | PG_UP | DOT | N0 | DOT |
| 40 | FSLH | RALT | FSLH | DOT | FSLH |
| 41 | ESC | to GAME | ESC | soft_off | to BASE |
| 42 | LGUI | LGUI | LGUI | LGUI | LALT |
| 43 | mo EXT | trans | mo EXT | mo EXT | LCTRL |
| 44 | SPACE | SPACE | SPACE | SPACE | SPACE |
| 45 | BSPC | BSPC | BSPC | BSPC | BSPC |
| 46 | mo SYM | mo SYM | trans | mo SYM | RSHFT |
| 47 | ENTER | ENTER | ENTER | ENTER | ENTER |

Thumb positions: left outer→inner 42,43,44; right inner→outer 45,46,47. Other positions follow `config/eyelash_corne.json`, including the five-way control and encoder press.

The unavailable 34-key reference is inspiration only: this adaptation retains all 48 hardware positions and QWERTY. EXT supplies navigation and F1–F12; SYM supplies coding symbols; NUM supplies numbers and device controls.
