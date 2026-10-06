# Print the N newest screenshots taken before the user sent the /screenshot message being processed.
# Usage: python3 pick.py N [--sent EPOCH_OR_ISO] [CLAUDE_TRANSCRIPT.jsonl]
# Send time, in order: --sent (any agent supplies it), the active Claude Code or Codex session log, now. The first line names which.
import json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

FRESH = 120  # seconds since the active session's transcript was last written
GRACE = 10  # seconds between a queued message's dequeue and its user entry


def stamp(text):
    return datetime.fromisoformat(text.replace("Z", "+00:00")).timestamp()


def is_screenshot(text):
    return "/screenshot" in (text or "")


def typed_text(entry):
    """What the user typed: a string, or the text blocks of a message (tool results are not typing)."""
    content = entry.get("message", {}).get("content")
    if isinstance(content, str):
        return content
    return " ".join(block.get("text", "") for block in content or [] if block.get("type") == "text")


def send_time(path):
    """Send time of the latest /screenshot message in the transcript, or None."""
    queue, popped, latest = [], [], None
    for line in path.open():
        entry = json.loads(line)
        kind = entry.get("type")
        if kind == "queue-operation":
            op = entry["operation"]
            if op == "enqueue":
                queue.append((stamp(entry["timestamp"]), entry.get("content", "")))
            elif op == "dequeue" and queue:
                popped.append((*queue.pop(0), stamp(entry["timestamp"])))
            elif op == "remove":
                match = next((item for item in queue if item[1] == entry.get("content")), None)
                if match:
                    queue.remove(match)
        elif kind == "attachment" and (entry.get("attachment") or {}).get("type") == "queued_command":
            if is_screenshot(entry["attachment"].get("prompt")):
                latest = stamp(entry["timestamp"])  # absorbed mid-turn: stamped at send time
        elif kind == "user" and not entry.get("isMeta") and is_screenshot(typed_text(entry)):
            seen = stamp(entry["timestamp"])
            queued = [sent for sent, content, dequeued in popped if is_screenshot(content) and 0 <= seen - dequeued <= GRACE]
            latest = queued[-1] if queued else seen  # queued: its send time; otherwise sent while idle
    return latest


def codex_send_time(path):
    """Codex logs a user message when it processes it; there is no queue record."""
    latest = None
    for line in path.open():
        entry = json.loads(line)
        payload = entry.get("payload", {})
        if payload.get("role") == "user" and any(block.get("text", "").lstrip().startswith("/screenshot") for block in payload.get("content", [])):
            latest = stamp(entry["timestamp"])
    return latest


AGENTS = [  # (own-session env variable, log glob under home, send-time parser)
    ("CLAUDE_CODE_SESSION_ID", ".claude/projects/*/*.jsonl", send_time),
    ("CODEX_THREAD_ID", ".codex/sessions/*/*/*/*.jsonl", codex_send_time),  # variable name unverified
]


def find_log():
    """(path, parser) of the running session's log, or None."""
    logs = [(path, parser) for _, pattern, parser in AGENTS for path in Path.home().glob(pattern)]
    for variable, _, _ in AGENTS:  # a running agent names its own log; mtime alone misleads when several agents are active
        session = os.environ.get(variable)
        own = [log for log in logs if session and session in log[0].name]
        if own:
            return own[0]
    newest = max(logs, key=lambda log: log[0].stat().st_mtime, default=None)
    fresh = newest and datetime.now().timestamp() - newest[0].stat().st_mtime <= FRESH  # a stale log belongs to no running session
    return newest if fresh else None


def parse_sent(text):
    return float(text) if text.replace(".", "", 1).isdigit() else stamp(text)


args = sys.argv[1:]
sent = parse_sent(args.pop(args.index("--sent") + 1)) if "--sent" in args else None
if sent is not None:
    args.remove("--sent")
count = int(args[0]) if args else 1
log = (Path(args[1]), send_time) if len(args) > 1 else find_log()
anchor = sent or (log[1](log[0]) if log else None)
note = "anchor: send time (--sent)" if sent else "anchor: send time" if anchor else "anchor: now (no send time found)"
anchor = anchor or datetime.now(timezone.utc).timestamp()

folder = subprocess.run(["defaults", "read", "com.apple.screencapture", "location"], capture_output=True, text=True).stdout.strip() or "~/Desktop"
shots = sorted((p for p in Path(folder).expanduser().glob("*.png") if p.stat().st_mtime <= anchor), key=lambda p: p.stat().st_mtime)
print(f"{note} {datetime.fromtimestamp(anchor).strftime('%H:%M:%S')}")
for shot in shots[-count:]:
    print(shot)
