"""Generate the profile cards (pinned repos, stats, top languages) as static SVG.

Replaces the public github-readme-stats instance, which is often down.
Public data only. Usage: GITHUB_TOKEN=... python tools/cards.py
"""

import json
import os
import urllib.request
from xml.sax.saxutils import escape

USER = "lburdier"
PINS = ["blender-multiplayer", "witness360-releases", "EasyUV", "easyuv-lint", "cv-gen",
        "instagrowth", "TheWorstRoommate"]
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "cards")
TITLE, ICON, TEXT, BORDER = "#8fa0b0", "#7a9080", "#aaaaaa", "#8fa0b0"
FONT = "'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif"
COLORS = {"Python": "#3572A5", "Rust": "#dea584", "TypeScript": "#3178c6", "JavaScript": "#f1e05a",
          "PHP": "#4F5D95", "Kotlin": "#A97BFF", "C++": "#f34b7d", "C": "#555555", "HTML": "#e34c26",
          "CSS": "#663399", "Java": "#b07219", "C#": "#178600", "Shell": "#89e051",
          "PowerShell": "#012456", "Vue": "#41b883", "Go": "#00ADD8", "GLSL": "#5686a5",
          "HLSL": "#aace60", "Blade": "#f7523f", "Dart": "#00B4AB", "Swift": "#F05138",
          "PLpgSQL": "#336790", "TSQL": "#e38c00"}
# Names shown on the cards (the repository stays the link target)
NAMES = {"witness360-releases": "witness360"}
# English descriptions for the cards (the repositories describe themselves in French)
DESCRIPTIONS = {
    "blender-multiplayer": "Edit the same Blender scene together in real time, on a LAN or over the "
                           "internet with an invite link (Blender 4.2+ / 5.x).",
    "witness360-releases": "Camera tracking helped by a 360 witness camera on the rig, sent to Blender "
                           "with a matched HDRI. Windows and Mac.",
}
# Language shown when the repository only holds release files
LANG_OVERRIDE = {"witness360-releases": "Python"}

ICON_REPO = ('<path fill="%s" d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5'
             'a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Z'
             'm10.5-1V1.5h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8Z"/>' % ICON)
ICON_STAR = ('<path fill="%s" d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279'
             'l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79'
             'l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"/>' % ICON)
ICON_FORK = ('<path fill="%s" d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1'
             ' 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5'
             ' 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0'
             ' 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"/>' % ICON)


def api(path, data=None):
    url = path if path.startswith("http") else "https://api.github.com" + path
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data else None)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-cards")
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", "Bearer " + tok)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def wrap(text, width, lines):
    out, cur = [], ""
    for w in (text or "").split():
        if len(cur) + len(w) + 1 > width and cur:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        out.append(cur)
    if len(out) > lines:
        out = out[:lines]
        out[-1] = out[-1][:width - 3].rstrip(" ,.:;") + "..."
    return out


def svg(w, h, body, label):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
            'role="img" aria-label="%s"><title>%s</title><style>text{font-family:%s}</style>'
            '<rect x="0.5" y="0.5" rx="6" width="%d" height="%d" fill="none" stroke="%s" '
            'stroke-opacity="0.25"/>%s</svg>\n'
            % (w, h, w, h, escape(label), escape(label), FONT, w - 1, h - 1, BORDER, body))


def pin_card(repo):
    r = api("/repos/%s/%s" % (USER, repo))
    name = NAMES.get(repo, r["name"])
    lang = LANG_OVERRIDE.get(repo) or r.get("language")
    lines = wrap(DESCRIPTIONS.get(repo) or r.get("description") or "", 56, 2)
    body = '<g transform="translate(25,21)">%s</g>' % ICON_REPO
    body += ('<text x="49" y="34" fill="%s" font-size="17" font-weight="600">%s</text>'
             % (TITLE, escape(name)))
    for i, line in enumerate(lines):
        body += ('<text x="25" y="%d" fill="%s" font-size="13">%s</text>'
                 % (62 + i * 18, TEXT, escape(line)))
    x = 25
    if lang:
        body += '<circle cx="%d" cy="104" r="6" fill="%s"/>' % (x + 6, COLORS.get(lang, TITLE))
        body += '<text x="%d" y="108" fill="%s" font-size="12">%s</text>' % (x + 18, TEXT, escape(lang))
        x += 34 + 7 * len(lang)
    body += '<g transform="translate(%d,95)">%s</g>' % (x, ICON_STAR)
    body += '<text x="%d" y="108" fill="%s" font-size="12">%d</text>' % (x + 21, TEXT, r["stargazers_count"])
    x += 55
    body += '<g transform="translate(%d,95)">%s</g>' % (x, ICON_FORK)
    body += '<text x="%d" y="108" fill="%s" font-size="12">%d</text>' % (x + 21, TEXT, r["forks_count"])
    return svg(400, 125, body, name)


def own_repos():
    repos, page = [], 1
    while True:
        batch = api("/users/%s/repos?per_page=100&type=owner&page=%d" % (USER, page))
        repos += batch
        if len(batch) < 100:
            return [r for r in repos if not r["fork"] and not r["archived"]]
        page += 1


def stats_card(repos):
    u = api("/users/%s" % USER)
    stars = sum(r["stargazers_count"] for r in repos)
    contrib = None
    if os.environ.get("GITHUB_TOKEN"):
        try:
            q = ('query{user(login:"%s"){contributionsCollection{contributionCalendar'
                 '{totalContributions}}}}' % USER)
            d = api("https://api.github.com/graphql", {"query": q})
            contrib = d["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
        except Exception:  # noqa: BLE001
            contrib = None
    rows = [("Public repositories", len(repos)), ("Total stars", stars),
            ("Followers", u.get("followers", 0))]
    if contrib is not None:
        rows.insert(0, ("Contributions (last year)", contrib))
    body = '<text x="25" y="36" fill="%s" font-size="18" font-weight="600">GitHub stats</text>' % TITLE
    for i, (k, v) in enumerate(rows):
        y = 72 + i * 26
        body += '<circle cx="30" cy="%d" r="4" fill="%s"/>' % (y - 5, ICON)
        body += '<text x="44" y="%d" fill="%s" font-size="14">%s</text>' % (y, TEXT, escape(k))
        body += ('<text x="330" y="%d" fill="%s" font-size="14" font-weight="600" text-anchor="end">%s</text>'
                 % (y, TITLE, "{:,}".format(v)))
    return svg(355, 165, body, "GitHub stats")


def langs_card(repos):
    total = {}
    for r in repos:
        try:
            for k, v in api(r["languages_url"]).items():
                total[k] = total.get(k, 0) + v
        except Exception:  # noqa: BLE001
            continue
    for skip in ("Jupyter Notebook", "Makefile", "Batchfile", "NSIS", "Inno Setup", "Dockerfile"):
        total.pop(skip, None)
    top = sorted(total.items(), key=lambda kv: -kv[1])[:8]
    s = float(sum(v for _k, v in top)) or 1.0
    body = '<text x="25" y="36" fill="%s" font-size="18" font-weight="600">Most used languages</text>' % TITLE
    body += ('<clipPath id="bar"><rect x="25" y="52" width="300" height="8" rx="4"/></clipPath>'
             '<g clip-path="url(#bar)">')
    x = 25.0
    for k, v in top:
        w = 300 * v / s
        body += '<rect x="%.2f" y="52" width="%.2f" height="8" fill="%s"/>' % (x, w + 0.5, COLORS.get(k, TITLE))
        x += w
    body += "</g>"
    for i, (k, v) in enumerate(top):
        cx, cy = 25 + (i % 2) * 155, 88 + (i // 2) * 22
        body += '<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (cx + 5, cy - 4, COLORS.get(k, TITLE))
        body += ('<text x="%d" y="%d" fill="%s" font-size="13">%s %.1f%%</text>'
                 % (cx + 16, cy, TEXT, escape(k), 100 * v / s))
    return svg(350, 165, body, "Most used languages")


def write(name, content):
    path = os.path.join(OUT, name)
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old != content:
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        print("updated", name)


def main():
    os.makedirs(OUT, exist_ok=True)
    for repo in PINS:
        write("pin-%s.svg" % repo.lower(), pin_card(repo))
    repos = own_repos()
    write("stats.svg", stats_card(repos))
    write("languages.svg", langs_card(repos))


if __name__ == "__main__":
    main()
