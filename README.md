# withpoise.app

The Poise website: one page, plus `/privacy`, `/terms` and `/support`. Plain HTML and CSS, no build step. Hosted on GitHub Pages at the root of the `main` branch; `CNAME` holds the domain.

- `index.html` — the home page: top row, hero with the Reflect screen breathing in a phone, four beats with screenshots, The basics (four answers), a closing call to action (launch state only), footer. One switch on `<body data-cta="…">` chooses the call to action: `soon` (before launch: "Coming soon to the App Store." and the email line) or `launch` (Apple's badge and the trial line). The plain pages (`support.html`, `privacy.html`, `terms.html`) share the home's shell: the same top row (the switch shows their Get Poise link at launch) and footer around one reading column. Prices appear in three places on the page (the two launch-state lines and the trial answer); change all three together.
- `shots/write.webp`, `shots/reflect.webp`, `shots/send.webp`, `shots/refine.webp` — the four beat screenshots, 940×2040, taken from the real app on the iPhone 18 Pro simulator (iOS 27). Retake them when a screen changes.
- `app-store-badge.svg` — Apple's own "Download on the App Store" badge (from developer.apple.com); never redraw it.
- `privacy.html`, `terms.html` — generated from the app repo's `docs/PRIVACY_POLICY.md` and `docs/TERMS_OF_SERVICE.md` by `_dev/legal.py`, so the hosted pages say what the app's own pages say. Edit the docs in the app repo, then run `python3 _dev/legal.py` here.
- `support.html` — reach us, how to cancel, a few answers.
- `404.html` — served for any missing address.
- `style.css` — the one stylesheet. Light only, the app's colors and fonts (Lora, Plus Jakarta Sans).
- `og.png`, `favicon.png`, `apple-touch-icon.png` — the link preview image and icons, made from the app's icon and bundled fonts.
- `_dev/serve.py` — local preview that behaves like GitHub Pages (`/privacy` serves `privacy.html`, missing paths get the 404). `python3 _dev/serve.py` then open http://localhost:8765. `_dev` and this README are excluded from the published site by `_config.yml`.

Copy, colors and the "words that must not appear" list live in the app repo at `docs/WEBSITE_BRIEF.md`.

## Going live

The site must be public BEFORE the app is submitted: App Review opens the privacy page. Steps 1–5 happen then; steps 6–7 on release day.

1. Repository Settings → General → change visibility to Public (GitHub Pages is free only for public repositories).
2. Settings → Pages: source "Deploy from a branch", branch `main`, folder `/ (root)`. Custom domain `withpoise.app`. Save.
3. At GoDaddy, DNS for withpoise.app: remove the two `A` records for `@` that point to GoDaddy's builder (`13.248.243.5`, `76.223.105.230`); add four `A` records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; change the `www` CNAME to `rja4z3.github.io`. Leave the `MX` (`smtp.google.com`) and `TXT` records alone; email depends on them.
4. Back in Settings → Pages, tick "Enforce HTTPS" once it's offered (GitHub issues the certificate; up to an hour).
5. Check https://withpoise.app, /privacy, /terms and /support load without login.
6. Release day: (a) change `data-cta="soon"` to `data-cta="launch"` on every page (`index.html`, `support.html`, `privacy.html`, `terms.html`) and in the template inside `_dev/legal.py`, one find-and-replace; (b) put the App Store ID in place of `APPSTOREID` everywhere it appears (the badge links, the Get Poise links in each top row, and the commented `apple-itunes-app` meta tag in `index.html`'s `<head>`), then uncomment that tag (Safari on iPhone then shows Apple's own "open in the App Store" strip). Commit and push; Pages redeploys in about a minute.
7. Visit counter: PostHog, the app's own project, is already on every page (page views only, no cookies, nothing stored on the visitor's device, no replay, no identifying). It runs only when the address is withpoise.app, so nothing to switch on: once the site is live, the numbers appear under Web analytics in PostHog. Visitor counts read high there (each page load counts as a new visitor, by design); page views, pages, referrers and countries are the numbers to trust.
