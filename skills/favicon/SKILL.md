---
name: favicon
description: Make a favicon for a page in the user's style. A clay frame, ink panel and chalk letter cut from the page's real font outline, optically centered, as an inline SVG link tag. Use when asked for, or to fix, a favicon.
---

# favicon

Why: a hand-drawn letter never matches the page's type and sits off-center. Cutting the glyph from the real font and centering it by measurement fixes both.

## Rules

- **Letter**: capital, first letter of the page name. All caps, never lowercase, even when the page heading is lowercase ("kiln" gets K, "notes" gets N).
- **Font**: the font the page title uses, as a `.ttf`. Default EB Garamond Bold. Find the file in the project (`find . -iname 'EBGaramond-Bold*.ttf'`); ask only if none exists.
- **Look**: the page in miniature. Clay frame, ink panel, chalk letter. Colors come from the kiln (`~/Documents/code/dotfiles/kiln.html`): clay `#cc6633`, ink `#141414`; letter `#f0e0d0`.
- **Size**: letter up to 44 of 64 units tall and 38 wide; wide capitals (K, M, W) shrink to fit the panel. Frame `rx=10`, panel inset 5 with `rx=4`.
- **Centering**: bounding-box center, then shifted halfway toward the mass centroid. The script does both. Eyeballed coordinates look off.
- **Inline**: one `<link rel="icon" href="data:image/svg+xml,...">` in `<head>`, so the page stays one file. A one-line comment above it says what the icon is.

## Workflow

1. Run `python3 ~/Documents/code/dotfiles/skills/favicon/favicon.py <font.ttf> <letter>`. Needs `fonttools` (`pip3 install --user fonttools`). It prints the link tag.
2. Put the tag in `<head>`. If the file is generated (a build script writes the HTML), edit the generator, then rebuild. Check with `grep -n 'rel="icon"'` first; an edit to the output alone gets overwritten.
3. Verify: render the SVG at 16, 32 and 256 px in headless Chrome on a dark and a light bar. The letter must read at 16 px. Look at the render; do not assume.
4. Tell the user to hard-reload; browsers cache favicons.

## With the html skill

The html skill points here for pages worth keeping. Letter = the page name's initial; font = the page's title font.
