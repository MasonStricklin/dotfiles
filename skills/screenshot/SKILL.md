---
name: screenshot
description: Look at the screenshots the user took before sending the message. Use when the user says "screenshot", "my last N screenshots", or refers to something they just captured. Takes an optional count and optional per-image notes ("1 of 3", "1o3").
---

1. Parse the arguments:
   1a. A bare number is a count: `/screenshot 3` = 3 screenshots. No arguments = 1.
   1b. A marker `K of N` or `KoN` (case-insensitive, spaces optional) starts the note for image K of N. N is the count. K = 1 is the oldest, so images read in capture order.
   1c. K may be a list: `2 4 o4` or `2,4 of 4` = images 2 and 4 of 4, sharing the note after the marker.
   1d. A note runs from its marker to the next marker. Markers may come in any order.
   1e. Text before any marker applies to all images.
   1f. A bare number followed by text, with no marker, is the count and a request: `/screenshot 2 compare these`.
2. Pick the screenshots: `python3 <base directory>/pick.py N [--sent TIME]`.
   2a. Contract: the N newest screenshots taken before the user sent this message. "Sent" is when they pressed enter, even if the message waited in the queue. Later screenshots never count. Queued `/screenshot` messages each resolve to their own send time.
   2b. Send time, in order: `--sent <epoch or ISO time>`, then the running agent's own session log (Claude Code and Codex are both read), then now.
   2c. An agent whose log `pick.py` cannot read passes its own send time with `--sent`.
   2d. The first output line names the anchor. If it says `anchor: now`, tell the user the pick is the newest at processing time and may be off if they took screenshots after sending.
   2e. The remaining lines are the files, oldest first. Image K of N is the Kth line.
3. View the files, lowest K first. If any marker is present, view only the marked images; otherwise view all. Apply each note to its image only.
4. Continue with the request, or describe the images if none was given.

Examples:
- `/screenshot` = the newest screenshot.
- `/screenshot 3 what changed?` = the newest three, request "what changed?".
- `/screenshot 1 of 2 this is the bug 2o2 this is the fix` = two images; the older gets "this is the bug", the newer gets "this is the fix".
- `/screenshot 2 4 o4` = four images; only the 2nd and 4th are viewed.
