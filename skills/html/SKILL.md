---
name: html
description: Build or edit a single-file HTML page in the user's own style. Use for any standalone .html page, tool or artifact. Pulls colors, fonts and principles from the kiln and checks the result in headless Chrome.
---

# html

Why: a single HTML file is the quickest agent-friendly way to spin up an ad-hoc visual thing. Plain JS handles fairly complex visualizations, with no build step, and the file opens anywhere. Treat each page as a fast tool, not a product.

Fast to build is not an excuse for sloppy code. Code quality still matters, and the page must stay lightweight: no repeated work per item (N+1 lookups, a fetch or a layout read inside a loop), no needless re-renders, no heavy libraries where a few lines of JS will do.

Build single-file HTML pages in the user's style. Generally, do not ask style questions; the kiln answers them.
When a page needs something the kiln does not cover (charts, long-form text, pull quotes, images), propose the new conventions and confirm them before building.

## Style source

The kiln is the style guide: `~/Documents/code/dotfiles/kiln.html`. Read it before building.

- **Colors**: `CORE` (clay `#CC6633`, clay ink `#442211`, clay chalk `#EEE5D5`, and ink `#141414` / white `#FFFFFF` on one split card) and `EXTENDED` (hue, tone, name, shades) in the script. The page background is `--clay-chalk` in the CSS tokens.
- **Fonts**: the `FONTS` table and the `--font-*` tokens.
- **Principles**: the `principles` section at the bottom of the page.

Defaults when the request names nothing:
- Fonts: primary (Optima, EB Garamond, DM Mono, Courier Prime), falling back to secondary (Inter, Palatino, Menlo, Courier New). Experimental fonts only when asked.
- Font roles: serif (EB Garamond) for names and headings; sans (Optima) for interface and prose, meaning headers, buttons, pills and chips; mono (DM Mono) for data compared down a column, meaning numbers, dates and scores. One job per font.
- Table headers: a header over a text column starts on the same edge as its cells; over a chip column, its focus ring is flush with the chips. A last column is right-aligned, its header and cells alike, and its sort arrow sits left of the label.
- Offline pages embed the fonts they use; an installed or remote font is a silent fallback elsewhere.
- Colors: clay accent, ink text and borders, clay chalk background. Natural tones for extra colors; vivid only as accents.
- New hexes: memorable, per the conventions in the kiln's principles.

## Structure

Patterns the kiln is built on. Reuse what fits; leave out what the page does not need.

- **Tokens**: everything on `:root`. A spacing scale (`--s2` to `--s24`), border widths that form a series (base, hover, selected), one corner radius, one focus-ring offset.
- **Panels**: an ink border around a clay chalk panel, titled by an inverted ink band. Collapsible with `<details>`.
- **Cards**: hover and selection grow the border inward, so the cumulative width is the same on every card type (base, then hover, then selected).
- **Focus**: a box-shadow ring, not an outline, so corners stay barely rounded. Ring offset plus width stays under the gap between cards.
- **Script**: data in tables at the top, small render functions, one delegated click listener, real `<button>`s and no button inside another.
- **Stability**: fixed heights where content varies by font, so choosing a font never moves the page.
- **Naming**: sets form one series (primary, secondary, tertiary).
- **Favicon**: a page you keep and name gets one from the `favicon` skill. Throwaway pages skip it.
- **Self-checks**: when a failure would be silent, such as a third-party font not loading, the page reports it in the console.

## Workflow

1. Build the smallest page that expresses the idea, then grow it.
2. Show visual choices as disposable previews in the page itself (see AGENTS.md).
3. After a rewrite or comprehensive overhaul, run the check: `python3 ~/Documents/code/dotfiles/skills/html/check.py <page.html>`. Not every turn.
