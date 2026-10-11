# Right-half Baymax artwork

Peripheral-only copy of the nice_view shield from cormoran/zmk commit
4493783ef88ce2e653bf8217c92ee17140df71e3 (v0.3-branch+dya).
Upstream MIT notices are retained. The display overlay, display configuration,
status drawing functions, charging icon and battery/connection listeners are unchanged.
Only the right build selects this shield; the left still uses upstream nice_view.

Baymax replaces the random mountain/balloon artwork. Right-half key presses start
a brief blink about every three seconds of activity; every tenth animation is
a short wave. Waking from idle starts in the rest pose instead of waving. After four seconds without a right-half press, the
animation returns to rest and pauses its LVGL timer. Initial/idle artwork is static.
Battery and connection events continue to update normally. There is no WPM or
layer label added, and no keymap or pairing change.

Regenerate the three 140x68 one-bit LVGL images with
`python3 scripts/generate_baymax.py`. The exact-pixel portrait preview is
`docs/baymax-preview.png`; firmware rotates it to match the original art orientation.
The upstream image bounds are preserved. Test orientation, preserved status icons,
activity and idle pause on hardware after an approved flash; battery impact is unmeasured.

Baymax is intended to appear as a solid white body with black details on black.
Its encoded palette is reversed to compensate for the inversion the owner
observed on the physical right display. Only the artwork palette changes.
The artwork palette deliberately does not follow status-widget inversion; existing
status icons still use their original theme. The native-pixel preview shows the same geometry embedded in the firmware,
in the intended physical display colours.

The revised contour is traced from the approved concept coordinates and uniformly
scaled (reference bounds 334x469). Head overlaps shoulders; the original broad
belly and short feet proportions are retained, subject to the 68-pixel grid. The wave uses the earlier compact rounded arm.
