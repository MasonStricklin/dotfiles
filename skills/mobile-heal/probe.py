#!/usr/bin/env python3
# Renders a page at a true phone width and reports mobile defects, plus a screenshot of the first screens.
# Headless Chrome will not size its window below 500px, so the page loads in a 402px iframe instead.
# Usage: probe.py page.html [shot.png]
import math
import pathlib
import subprocess
import sys
import tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
WIDTH, HEIGHT = 402, 874  # iPhone 17
MAX_SCREENS, PER_ROW, GAP = 6, 3, 8

# Runs inside the page. With #probe it checks the page; with #y=N it only scrolls, for the screenshot.
PROBE = """<script>
addEventListener('load', () => setTimeout(() => {
    const hash = location.hash.slice(1);
    if (hash.startsWith('y=')) return scrollTo(0, +hash.slice(2));
    const W = document.documentElement.clientWidth, out = [], fails = new Map();
    const selector = el => el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + [...el.classList].map(c => '.' + c).join('');
    const text = el => `"${(el.textContent || el.value || '').trim().replace(/\\s+/g, ' ').slice(0, 30)}"`;
    const name = el => `${selector(el)} ${text(el)}`;
    // Repeated elements fail the same way, so each kind and selector is one line with a count and the first example.
    const fail = (kind, el, detail) => {
        const key = `${kind} ${selector(el)}`;
        if (fails.has(key)) fails.get(key).count++;
        else fails.set(key, { count: 1, example: `${text(el)} ${detail}` });
    };
    // Content inside a closed <details> cannot be seen or tapped, except the summary itself.
    const inClosedDetails = el => {
        for (let d = el.closest('details'); d; d = d.parentElement && d.parentElement.closest('details')) {
            const summary = el.closest('summary');
            if (!d.open && !(summary && summary.parentElement === d)) return true;
        }
        return false;
    };
    const shown = el => el.getClientRects().length && getComputedStyle(el).visibility !== 'hidden' && !inClosedDetails(el);
    const ownText = el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    const scroller = el => [...ancestors(el)].some(a => /auto|scroll|hidden|clip/.test(getComputedStyle(a).overflowX));
    function* ancestors(el) { for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) yield a; }
    const sticksOut = el => { const r = el.getBoundingClientRect(); return r.width && (r.right > W + 1 || r.left < -1); };

    out.push(`width ${W}`);
    const extra = document.documentElement.scrollWidth - W;
    if (extra > 0) {
        // Hidden elements widen the page too, so the culprit is the widest element of any kind.
        const widest = [...document.body.querySelectorAll('*')].reduce((a, b) =>
            b.getBoundingClientRect().right > a.getBoundingClientRect().right ? b : a);
        fail('FAIL overflow', widest, `page scrolls sideways by ${extra}px; this reaches furthest right`);
    }

    for (const el of document.body.querySelectorAll('*')) {
        if (!shown(el)) continue;
        const style = getComputedStyle(el), r = el.getBoundingClientRect();
        if (style.position === 'fixed') continue;
        if (sticksOut(el) && !scroller(el) && !(el.parentElement && sticksOut(el.parentElement)))
            fail('FAIL overflow', el, `spans ${Math.round(r.left)}..${Math.round(r.right)}`);
        if (!ownText(el)) continue;
        if (!scroller(el) && (r.left < 12 || r.right > W - 12))
            fail('FAIL gutter', el, `text at ${Math.round(r.left)}..${Math.round(r.right)}, needs 12px from each edge`);
        if (/hidden|clip/.test(style.overflowX) && el.scrollWidth > el.clientWidth + 1)
            fail('FAIL clipped', el, `content ${el.scrollWidth}px in ${el.clientWidth}px`);
        if (parseFloat(style.fontSize) < 12)
            fail('FAIL small-text', el, `${style.fontSize}`);
    }

    const controls = document.querySelectorAll('a[href], button, input, select, textarea, summary, [role=button], label[for]');
    let small = 0;
    for (const el of controls) {
        if (!shown(el)) continue;
        el.scrollIntoView({ block: 'center', inline: 'center' });
        const r = el.getBoundingClientRect();
        if (r.width < 24 || r.height < 24) fail('FAIL tap-size', el, `${Math.round(r.width)}x${Math.round(r.height)}, minimum 24x24`);
        else if (r.width < 44 || r.height < 44) small++;
        const hit = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
        if (hit && !el.contains(hit) && !hit.contains(el)) fail('FAIL covered', el, `center is covered by ${name(hit)}`);
    }
    scrollTo(0, 0);
    for (const [key, { count, example }] of fails)
        out.push(`${key}${count > 1 ? ` x${count}, e.g.` : ':'} ${example}`);
    if (small) out.push(`WARN tap-size ${small} controls under 44px (24px is the minimum, 44px is comfortable)`);
    out.push(`height ${document.documentElement.scrollHeight}`);
    parent.postMessage(out.join('\\n'), '*');
}, 1500));
</script>"""


def chrome(window, *args):
    base = [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=8000", f"--window-size={window}"]
    return subprocess.run(base + list(args), capture_output=True, text=True).stdout


def wrapper(frames):
    return ("<!doctype html><body style='margin:0;display:flex;flex-wrap:wrap;gap:%dpx;background:#888'>%s"
            "<pre id=report></pre><script>addEventListener('message', e => report.textContent = e.data)</script>"
            % (GAP, "".join(f"<iframe src='{src}' style='width:{WIDTH}px;height:{HEIGHT}px;border:0;background:#fff'></iframe>" for src in frames)))


page = pathlib.Path(sys.argv[1]).resolve()
shot = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else pathlib.Path(tempfile.gettempdir()) / f"{page.stem}-mobile.png").resolve()

with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    # A base tag keeps the page's relative links working from the temp copy.
    html = page.read_text().replace("<head>", f"<head><base href='{page.parent.as_uri()}/'>", 1)
    (tmp / "page.html").write_text(html.replace("</body>", PROBE + "</body>", 1))
    probe_url = (tmp / "page.html").as_uri()

    (tmp / "check.html").write_text(wrapper([probe_url + "#probe"]))
    dom = chrome(f"{WIDTH + 100},{HEIGHT}", "--dump-dom", (tmp / "check.html").as_uri())
    report = dom.split("<pre id=\"report\">", 1)[-1].split("</pre>", 1)[0].replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&").replace("&quot;", '"')
    if not report.startswith("width"):
        sys.exit("probe did not report; the page may have failed to load")

    lines = report.splitlines()
    height = int(lines[-1].split()[1])
    screens = min(math.ceil(height / HEIGHT), MAX_SCREENS)
    (tmp / "shot.html").write_text(wrapper([f"{probe_url}#y={i * HEIGHT}" for i in range(screens)]))
    rows = math.ceil(screens / PER_ROW)
    columns = min(screens, PER_ROW)
    chrome(f"{columns * (WIDTH + GAP)},{rows * (HEIGHT + GAP)}", f"--screenshot={shot}", (tmp / "shot.html").as_uri())

fails = [line for line in lines if line.startswith("FAIL")]
print(lines[0] + ("" if lines[0] == f"width {WIDTH}" else f"  (expected {WIDTH}; results are not a phone render)"))
print(*fails[:30], sep="\n")
if len(fails) > 30:
    print(f"... {len(fails) - 30} more")
print(*[line for line in lines if line.startswith("WARN")], sep="\n")
print(f"fails: {len(fails)}")
print(f"screenshot: {shot} (first {screens} of {math.ceil(height / HEIGHT)} screens, top-left to bottom-right)")
