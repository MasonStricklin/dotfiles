---
name: cleanup-project
description: Cleanup pass on a whole project directory, workspace or repo (for a single code file or page, use cleanup-code). Finds loose ends, reviews each one, and fixes them in the same pass. Extremely cautious: nothing is deleted before it is reviewed.
---

# cleanup-project

EXTREMELY CAUTIOUS. Review everything before deleting anything.

Usage: `/cleanup-project [directory]`. Default is the current project.

1. Read the project's `AGENTS.md` and `README.md`. Their rules win over this skill.
2. Find loose ends:
   2a. Comments, docs, READMEs and counts that contradict the code or data.
   2b. Finished or abandoned plans, drafts and run files.
   2c. Empty directories, stray copies, and files in the wrong place.
   2d. Regenerable junk: `.DS_Store`, `__pycache__`, build caches, fetch dumps.
   2e. Links and paths that point at moved or missing files.
   2f. Documentation that omits a feature that exists.
3. Review each item before touching it.
   3a. Read the file, or list the directory's contents.
   3b. Confirm nothing references it: `grep` its name across the project.
   3c. Confirm it is regenerable, or that its content lives elsewhere.
   3d. Any item that fails 3a–3c stays in place and goes into the report as a decision.
4. Fix every reviewed item in the same pass. Do not ask first about reviewed items, and do not hand the user a list of options.
   4a. Delete only items that passed step 3 as regenerable junk or empty directories.
   4b. Move everything else that is old or finished to the project's `archive/`. Never delete it.
   4c. Open tasks go to one `TODO.md` at the project root, one line each. Delete a line when done. Do not create a `plans/` directory.
   4d. Edit generators, not their output, then rebuild.
5. Run the project's build, audit or test commands. A failure means stop and report it.
6. Report in the plan format: what was done, one numbered line each, with every deletion named. Then only the decisions that cannot be inferred, each ending "Recommend: <option>".
7. If this pass created or changed a skill or config that could run across tools or machines, say whether it is shared or siloed. Do not link, sync or push it unasked.

EXTREMELY CAUTIOUS. When in doubt, leave it in place and report it. Nothing is deleted that was not reviewed.
