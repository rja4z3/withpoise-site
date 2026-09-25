#!/usr/bin/env python3
"""Rebuild privacy.html and terms.html from the app repo's docs, so the hosted
pages always say what the app's own pages say.
Run from anywhere: python3 _dev/legal.py"""
import html, pathlib, re, sys

SITE = pathlib.Path(__file__).resolve().parent.parent
DOCS = SITE.parent / "Poise" / "docs"
PAGES = [
    ("PRIVACY_POLICY.md", "privacy.html", "Privacy Policy", "privacy",
     "What Poise handles, how it is used, and the choices you have."),
    ("TERMS_OF_SERVICE.md", "terms.html", "Terms of Service", "terms",
     "The terms for using Poise."),
]

LOCKUP = '''    <a class="lockup small" href="./" aria-label="Poise home">
      <svg class="mark" viewBox="0 0 54 17" width="54" height="17" aria-hidden="true" focusable="false">
        <circle cx="4" cy="8.5" r="4" fill="#B8D9C5"/>
        <circle cx="22.5" cy="8.5" r="6.5" fill="#5A8472"/>
        <circle cx="45.5" cy="8.5" r="8.5" fill="#3E5C50"/>
      </svg>
      <span class="wordmark">Poise</span>
    </a>'''

FOOTER = '''  <footer>
    <nav aria-label="Site">
      <a href="privacy">Privacy</a>
      <a href="terms">Terms</a>
      <a href="support">Support</a>
    </nav>
    <p>© 2026 With Poise LLC · <a href="mailto:hello@withpoise.app">hello@withpoise.app</a></p>
  </footer>'''

def inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(hello@withpoise\.app)", r'<a href="mailto:\1">\1</a>', t)
    t = t.replace(" → ", " → ")
    return t

def convert(md):
    title, updated, body, in_list = None, None, [], False
    def close():
        nonlocal in_list
        if in_list: body.append("  </ul>"); in_list = False
    for raw in md.splitlines():
        line = raw.rstrip()
        if not line or line == "---" or line.startswith(">"):
            close(); continue
        if line.startswith("# "):
            title = line[2:].strip(); continue
        m = re.match(r"\*\*Last Updated\*\*:\s*(.+)", line)
        if m:
            updated = m.group(1).strip(); continue
        if line.startswith("## "):
            close(); body.append(f"  <h2>{inline(line[3:].strip())}</h2>"); continue
        if line.startswith("- "):
            if not in_list: body.append("  <ul>"); in_list = True
            body.append(f"    <li>{inline(line[2:].strip())}</li>"); continue
        close(); body.append(f"  <p>{inline(line)}</p>")
    close()
    return title, updated, "\n".join(body)

for src, out, name, slug, desc in PAGES:
    md = (DOCS / src).read_text()
    title, updated, body = convert(md)
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{name} — Poise</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://withpoise.app/{slug}">
<meta name="theme-color" content="#F9F4EA">
<link rel="icon" href="favicon.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:wght@500&family=Plus+Jakarta+Sans:wght@300;400;500&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main class="page plain">
  <header>
{LOCKUP}
    <h1>{html.escape(name)}</h1>
    <p class="updated">Last updated {html.escape(updated or "")}</p>
  </header>
{body}
{FOOTER}
</main>
</body>
</html>
'''
    (SITE / out).write_text(page)
    print("wrote", out, "from", src, "updated", updated)
