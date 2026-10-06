---
name: mobile-heal
description: Fix a web page's mobile layout in a short, capped loop. Probes the page at a true 402px phone width for overflow, edge gutters, clipped text, small text, tap-target size and covered controls, fixes the worst issues in CSS, and re-probes. Use when the user says a page is broken on mobile or asks to clean up its phone layout. Takes the page path and an optional round cap.
---

# mobile-heal

Usage: `/mobile-heal <page.html> [max-rounds]`. The round cap defaults to 3, at most 5.

## Probe

`python3 ~/Documents/code/dotfiles/skills/mobile-heal/probe.py <page.html> [shot.png]`

The probe renders the page in a 402x874 iframe, because headless Chrome will not size a window below 500px. It prints:
1. `width 402`. Any other width means the results are not a phone render: stop and report it.
2. One line per failing kind and selector, with a count and the first example:
   1. `overflow`: the page scrolls sideways, or an element sticks out past an edge. Content inside a scroll or clip container is exempt. A page-level overflow names the element that reaches furthest right, hidden ones included.
   2. `gutter`: text closer than 12px to either screen edge.
   3. `clipped`: an element hides its overflow and its content does not fit.
   4. `small-text`: text under 12px. 0px means a container-relative size collapsed in a squeezed box; fix the box, not the font.
   5. `tap-size`: a control under 24x24px (WCAG 2.5.8). Under 44px is a WARN only.
   6. `covered`: something else sits on a control's center, so a tap misses it.
3. `fails: N`, the number of failing lines, and a screenshot of the first six phone screens, in reading order.

## Loop

1. Back up the page: `cp <page> <scratchpad>/<name>.mobile-heal.bak`. One `cp` back restores it.
2. Round 1: run the probe and view the screenshot.
3. Fix the three worst fail lines, in this order: overflow, covered, clipped, tap-size, gutter, small-text. Fix the cause: one squeezed grid can produce several lines.
4. Run the probe again (text only). Next round from step 3.
5. Stop when any of these is true:
   1. `fails: 0`.
   2. The round cap is reached.
   3. `fails` did not drop since the previous round. Revert that round's edits first.
6. Final round: view the screenshot to confirm the page still shows its content.

## Fix rules

1. CSS only, inside the page's existing mobile `@media` block, or a new `@media (max-width: 520px)` block if it has none. Desktop must not change.
2. Reflow first: fewer columns, stacking, wrapping. Then smaller sizes. Sideways scrolling only for genuinely tabular content, and the report says where it was used.
3. Hidden helper elements that widen the page (measuring probes and the like) get `position: fixed` so they leave the scroll area.
4. Changes to HTML structure or JS: propose them in the report; do not make them. Exception: rule 7.
5. Small text that is a deliberate design size (labels, hex codes) is listed in the report, not enlarged without asking.
6. Do not commit.
7. One mobile check in JS: `const device = { get isMobile() { return mobile.matches; } }`, where `mobile = matchMedia('(max-width: <the CSS breakpoint>px)')`. The getter reads live, so it needs no listener. Page JS branches on `device.isMobile` only: no `userAgent`, `innerWidth` or second `matchMedia`. If the page's JS has a mobile branch without it, replace that branch with `device.isMobile`; that is the only JS edit allowed. The breakpoint matches the page's CSS `@media` breakpoint. No other device flags until needed.

## Report

1. Rounds run, and why the loop stopped.
2. Each fix: the selector and the change.
3. Fail lines remaining, each with why it was left.
4. Proposed structure or JS changes, if any.
5. Final screenshot path, and the backup path.
