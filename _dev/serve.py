#!/usr/bin/env python3
"""Local preview that behaves like GitHub Pages: /privacy serves privacy.html,
a missing path serves 404.html. Run: python3 _dev/serve.py [port]"""
import http.server, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765

class Pages(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def send_head(self):
        path = self.translate_path(self.path.split("?", 1)[0])
        if not os.path.exists(path) and os.path.isfile(path + ".html"):
            self.path = self.path.split("?", 1)[0] + ".html"
        elif not os.path.exists(path):
            self.path = "/404.html"
        return super().send_head()
    def log_message(self, fmt, *args):
        sys.stderr.write("%s\n" % (fmt % args))

print(f"serving {ROOT} at http://localhost:{PORT}", flush=True)
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Pages).serve_forever()
