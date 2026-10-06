---
name: cleanup-code
description: Cleanup and speed pass on a single code file or page (for a whole project or folder, use cleanup-project) with no behavior change. Makes it readable to humans and LLMs by preferring clear names and flow over comments, grouping related code, removing genuine duplication, and cutting avoidable work. Use when the user asks for a code cleanup, optimization, or readability pass. Takes a file path.
---

# cleanup-code

Usage: `/cleanup-code <file>`. Behavior stays identical; only structure, names, and cost change.

## Loop

1. Checkpoint: `git commit` is the user's call, so copy the file to `<scratchpad>/<name>.cleanup-code.bak`. One `cp` back restores it.
2. Baseline: capture how the file behaves now (run its tests, or render and screenshot it, or run it on sample input). Without a baseline, say so in the report.
3. Apply the passes below, one at a time.
4. Re-run the baseline and compare. Any difference is a regression: revert that pass.
5. Report.

## Passes

1. Readability
   1. Replace a comment with a better name or simpler flow wherever that says the same thing.
   2. Keep a comment only for what code cannot say, such as why something is odd.
   3. Names in a set form one connected series (primary / secondary / tertiary).
   4. Flatten nesting with early returns; give magic values a named constant.
2. Grouping
   1. Related code sits together under one short, specific heading.
   2. Order each group general to specific, or in the order it runs.
3. DRY
   1. Merge duplicates only when they change for the same reason.
   2. Leave coincidental similarity alone; a wrong abstraction costs more than a repeat.
4. Speed
   1. Remove dead code, unused rules, and unreachable branches.
   2. Hoist repeated work out of loops; avoid repeated DOM queries and layout reads.
   3. Load order: nothing render-blocking that can wait; no unused assets.
   4. Change an algorithm or data structure only when the gain is clear.

## Rules

1. No behavior, output, or visual change. Unsure means leave it.
2. Light edits (comments, local names) are made directly. Method names and structure within a file are shown in the report. Cross-file structure, contracts between layers, and dependencies are proposed, not made.
3. Do not commit.
4. Findings outside the file's scope are listed, not fixed.

## Report

1. What changed, grouped by pass, each as selector or function plus the change.
2. How no-regression was verified, or that it was not.
3. Proposed heavier changes, if any.
4. Backup path.
