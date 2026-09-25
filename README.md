# withpoise.app

The Poise website: one page, plus `/privacy`, `/terms` and `/support`. Plain HTML and CSS, no build step. Hosted on GitHub Pages at the root of the `main` branch; `CNAME` holds the domain.

- `index.html` — the one page.
- `privacy.html`, `terms.html` — generated from the app repo's `docs/PRIVACY_POLICY.md` and `docs/TERMS_OF_SERVICE.md` by `_dev/legal.py`, so the hosted pages say what the app's own pages say. Edit the docs in the app repo, then run `python3 _dev/legal.py` here.
- `support.html` — reach us, how to cancel, a few answers.
- `404.html` — served for any missing address.
- `style.css` — the one stylesheet. Light only, the app's colors and fonts (Lora, Plus Jakarta Sans).
- `og.png`, `favicon.png`, `apple-touch-icon.png` — the link preview image and icons, made from the app's icon and bundled fonts.
- `_dev/serve.py` — local preview that behaves like GitHub Pages (`/privacy` serves `privacy.html`, missing paths get the 404). `python3 _dev/serve.py` then open http://localhost:8765. `_dev` and this README are excluded from the published site by `_config.yml`.

Copy, colors and the "words that must not appear" list live in the app repo at `docs/WEBSITE_BRIEF.md`.

## Going live (launch day)

1. Repository Settings → General → change visibility to Public (GitHub Pages is free only for public repositories).
2. Settings → Pages: source "Deploy from a branch", branch `main`, folder `/ (root)`. Custom domain `withpoise.app`. Save.
3. At GoDaddy, DNS for withpoise.app: remove the two `A` records for `@` that point to GoDaddy's builder (`13.248.243.5`, `76.223.105.230`); add four `A` records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; change the `www` CNAME to `rja4z3.github.io`. Leave the `MX` (`smtp.google.com`) and `TXT` records alone; email depends on them.
4. Back in Settings → Pages, tick "Enforce HTTPS" once it's offered (GitHub issues the certificate; up to an hour).
5. Check https://withpoise.app, /privacy, /terms and /support load without login. Then swap "Coming soon to the App Store." for the App Store badge in `index.html`.
