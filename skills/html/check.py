#!/usr/bin/env python3
# Renders a page in headless Chrome and reports what a glance would miss:
# script errors, whether the page shows any content, and a screenshot to look at.
# Usage: check.py page.html [width]
import pathlib
import re
import subprocess
import sys
import tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

page = pathlib.Path(sys.argv[1]).resolve()
width = sys.argv[2] if len(sys.argv) > 2 else "1440"
url = page.as_uri()
shot = pathlib.Path(tempfile.gettempdir()) / f"{page.stem}-{width}.png"
base = [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=8000", f"--window-size={width},900"]

dump = subprocess.run(base + ["--enable-logging=stderr", "--v=0", "--dump-dom", url], capture_output=True, text=True)
errors = [line for line in dump.stderr.splitlines() if "CONSOLE" in line and re.search(r"Uncaught|Error", line)]
text = re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>|\s+", " ", dump.stdout, flags=re.S).strip()

subprocess.run(base + [f"--screenshot={shot}", url], capture_output=True)

print("errors:", len(errors))
for line in errors:
    print("  ", line.split("CONSOLE")[-1])
print("visible text:", len(text), "characters")
print("screenshot:", shot)
