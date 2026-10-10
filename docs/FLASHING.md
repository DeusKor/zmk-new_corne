# Verification, flashing and rollback

No flashing has been performed. Do not flash without the owner's explicit approval.

## Compatibility gate

This checkout targets an Eyelash Corne, not a generic Corne or Sofle. Before flashing, confirm the PCB/model, controller and bootloader using board markings/vendor evidence and bootloader identification. The build matrix uses nice_nano_v2 with eyelash_corne_left/right and nice_view. Left is central; right has column offset 7. Preserve the existing manifest, overlays, display, split transport and Bluetooth configuration. Do not substitute standard Corne firmware or update the ZMK version for this keymap.

The manifest imports the vendor shield module from a moving main branch and uses cormoran ZMK v0.3-branch+dya. Record resolved dependency revisions from each Actions run; a build is not physical compatibility proof. Save the expanded devicetree/build logs to verify the resolved shield and GPIO mapping against the local overlay. Export any active Studio/DYA layout using its supported UI: persisted mappings may override the compiled keymap. Do not erase settings to resolve an override.

## Build and checks

Run `python3 scripts/check_keymap.py`, then require successful firmware and safety workflows for the exact implementation commit. The existing firmware workflow builds both halves plus settings_reset. Download the two normal firmware artifacts, record their SHA256 hashes, and identify left/right from build metadata. Never use the settings_reset image for an ordinary update.

Static checks validate mapping and isolation, not timing. After approved flashing, test in a key-event viewer:

- Every physical key and all six thumbs; inner right Backspace repeats normally.
- Each BASE chord emits one intended key; ordinary fast WE/IO/XC/comma-period rolls remain ordinary typing. Test both release orders, and tune timing only from observed results.
- EXT A/S/D/F = Left/Down/Up/Right and F1–F12; SYM punctuation with the host's US layout; NUM U/I/O = 7/8/9, J/K/L = 4/5/6, M/comma/period = 1/2/3, N = 0 and slash = decimal, plus profile selection.
- EXT: hold its thumb and use right-hand Cmd/Shift/Alt/Ctrl with left-hand arrows. NUM: use left-hand Ctrl/Alt/Cmd/Shift with right-hand digits. Verify press/release events and multi-modifier chords.
- GAME simultaneous W+E, I+O, X+C and comma+period never emit combos. Hold W/A/S/D, repeat Q/E/R/F and digits, and combine dedicated Shift/Ctrl/Alt. No stuck keys on release.
- Enter GAME via EXT + bottom outer right, release both, and exit with bottom outer right. Repeat while other keys were held and verify all release events. Release keys before switching during normal use.
- Joystick: test all four pointer directions and stopping on release, including any supported diagonal combinations. Centre left-clicks on BASE/NUM/GAME; EXT centre right-clicks; SYM centre middle-clicks. Verify held clicks release and drag works if the physical switch permits centre+direction simultaneously. Repeat mouse checks over USB and already-paired Bluetooth. Pointing was already enabled; this change does not intentionally alter its HID descriptor.
- USB, previously paired Bluetooth, both halves/displays, encoder, sleep/wake. Do not remove pairing to make this test pass.

## Approval and flashing

Before asking for approval, obtain known-good compatible firmware for BOTH halves and save source revisions, hashes and any runtime layout export. A rebuild of the old source is not proof that it matches the currently installed firmware. If originals are missing, state that rollback is unverified.

Present the owner with hardware evidence, exact left/right artifacts and hashes, the vendor-confirmed bootloader entry steps and flash order. Have another keyboard available. After approval, enter the identified half's bootloader following its vendor instructions, verify the drive identity, and copy only its corresponding normal UF2. Repeat in the verified vendor order, then perform the checks above. Do not guess reset-button timing or use a reset image.

## Rollback

Re-enter each affected half's verified bootloader and restore its saved known-good UF2 using the same procedure. Restore runtime mappings only through supported tools. Do not erase settings, clear Bluetooth bonds, replace the bootloader or change dependency versions. If recovery requires a settings reset, stop and seek separate approval explaining pairing loss. Firmware rollback alone cannot guarantee restoration after persistent-setting migrations, which this change does not intentionally introduce.
