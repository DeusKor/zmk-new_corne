# Compact left status display

Central-only variant of cormoran/zmk nice_view at
4493783ef88ce2e653bf8217c92ee17140df71e3. MIT notices retained.
Driver overlay, display settings, battery rendering and event subscriptions
for battery, endpoints and layers are preserved. Replaces the WPM graph and
five simultaneous slot indicators with the selected USB/BT output and
LINKED (connected), OFFLINE (bonded but disconnected), or NEW (unbonded).
The active layer remains visible. The middle region shows one of 100 short work reminders chosen randomly at
firmware startup, including reset wake from soft-off. Ordinary idle resumes do
not change it. Random selection can repeat a previous message; no settings are
written and there is no date tracking.
Right Baymax display, pairing and split transport are unchanged.
