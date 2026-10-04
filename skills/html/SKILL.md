---
name: html
description: Build or edit a single-file HTML page in the user's own style. Use for any standalone .html page, tool or artifact. Pulls colors, fonts and principles from the themer and checks the result in headless Chrome.
---

# html

Build single-file HTML pages in the user's style. Do not ask style questions; the themer answers them.

## Style source

The themer is the style guide: `~/Documents/code/dotfiles/themer.html`. Read it before building.

- **Colors**: `CORE` (clay `#CC6633`, clay ink `#442211`, ink `#141414`, white) and `EXTENDED` (hue, tone, name, shades) in the script. The page paper is `--paper` in the CSS tokens.
- **Fonts**: the `FONTS` table and the `--font-*` tokens.
- **Principles**: the `principles` section at the bottom of the page.

Defaults when the request names nothing:
- Fonts: primary (Optima, Garamond, DM Mono, Courier Prime), falling back to secondary (Inter, Georgia, Menlo, Courier New). Experimental fonts only when asked.
- Colors: clay accent, ink text and borders, paper background. Natural tones for extra colors; vivid only as accents.
- New hexes: memorable, per the conventions in the themer's principles.

## Structure

Patterns the themer is built on. Reuse what fits; leave out what the page does not need.

- **Tokens**: everything on `:root`. A spacing scale (`--s2` to `--s24`), border widths that form a series (base, hover, selected), one corner radius, one focus-ring offset.
- **Panels**: an ink border around a paper panel, titled by an inverted ink band. Collapsible with `<details>`.
- **Cards**: hover and selection grow the border inward, so the cumulative width is the same on every card type (base, then hover, then selected).
- **Focus**: a box-shadow ring, not an outline, so corners stay barely rounded. Ring offset plus width stays under the gap between cards.
- **Script**: data in tables at the top, small render functions, one delegated click listener, real `<button>`s and no button inside another.
- **Stability**: fixed heights where content varies by font, so choosing a font never moves the page.
- **Naming**: sets form one series (primary, secondary, tertiary).
- **Self-checks**: when a failure would be silent, such as a third-party font not loading, the page reports it in the console.

## Workflow

1. Build the smallest page that expresses the idea, then grow it.
2. Show visual choices as disposable previews in the page itself (see AGENTS.md).
3. After a rewrite or comprehensive overhaul, run the check: `python3 ~/Documents/code/dotfiles/skills/html/check.py <page.html>`. Not every turn.
