# withpoise.app

The Poise website: one page, plus `/privacy`, `/terms` and `/support`. Plain HTML and CSS, no build step. Hosted on GitHub Pages at the root of the `main` branch; `CNAME` holds the domain.

- `index.html` — the home page: top row, hero with the Reflect screen breathing in a phone, four beats with screenshots, The basics (four answers), a closing call to action (launch state only), footer. One switch on `<body data-cta="…">` chooses the call to action: `soon` (before launch: "Coming soon to the App Store." and the email line) or `launch` (Apple's badge and the trial line). The plain pages (`support.html`, `privacy.html`, `terms.html`) share the home's shell: the same top row (the switch shows their Get Poise link at launch) and footer around one reading column. Prices appear in three places on the page (the two launch-state lines and the trial answer); change all three together.
- `sitemap.xml` and `robots.txt` — the four pages for search engines (update `lastmod` when a page's content changes). The home page carries WebSite and Organization markup (the site name "Poise", the alternate name "Poise: Space to Message", the logo), which is what Google shows beside a result; every page carries the link-preview tags.
- `shots/write.webp`, `shots/reflect.webp`, `shots/send.webp`, `shots/refine.webp` — the four beat screenshots, 940×2040, taken from the real app on the iPhone 18 Pro simulator (iOS 27). Retake them when a screen changes.
- `app-store-badge.svg` — Apple's own "Download on the App Store" badge (from developer.apple.com); never redraw it.
- `privacy.html`, `terms.html` — generated from the app repo's `docs/PRIVACY_POLICY.md` and `docs/TERMS_OF_SERVICE.md` by `_dev/legal.py`, so the hosted pages say what the app's own pages say. Edit the docs in the app repo, then run `python3 _dev/legal.py` here.
- `support.html` — reach us, how to cancel, a few answers.
- `404.html` — served for any missing address.
- `style.css` — the one stylesheet. Light only, the app's colors and fonts (Lora, Plus Jakarta Sans).
- `og-mark.jpg`, `favicon.ico`, `favicon-48/96/192.png`, `apple-touch-icon.png`, `logo.png` — the link preview image (1200×630: the three dots and the name, centred so a square crop keeps the mark; Randall, Oct 26, after a WhatsApp thumbnail made the old text-heavy image unreadable; a new file name so apps that cached the old card fetch the new one) and the icons (Google wants favicons in multiples of 48; the .ico is for the crawlers that still ask for /favicon.ico; logo.png is the 512 the site-name markup points at), made from the app's icon and the site's fonts.
- `_dev/serve.py` — local preview that behaves like GitHub Pages (`/privacy` serves `privacy.html`, missing paths get the 404). `python3 _dev/serve.py` then open http://localhost:8765. `_dev` and this README are excluded from the published site by `_config.yml`.

Copy, colors and the "words that must not appear" list live in the app repo at `docs/WEBSITE_BRIEF.md`.

## Going live

LIVE since October 26, 2026. The repository is public (GitHub's free plan hosts Pages for public repositories only), GitHub Pages serves the root of `main`, `CNAME` holds the domain, GoDaddy's records point at GitHub (four `A` records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; `www` CNAME → `rja4z3.github.io`; the `MX`, `TXT` and `NS` records untouched, email depends on them), the certificate covers withpoise.app and www.withpoise.app, and Enforce HTTPS is on. http and www redirect to https://withpoise.app. A change is a commit and a push; Pages republishes in about a minute.

If the domain ever has to be set again: GitHub's checker can lag behind new DNS records by up to an hour (its own cache), and re-saving the same domain does nothing; removing the custom domain and setting it again in Settings → Pages (or by API, `cname` null then `withpoise.app`) requests the certificate at once, then tick Enforce HTTPS.

Still to do:

5. Verify the domain with GitHub so nobody else can claim withpoise.app on Pages if the site is ever unlinked: GitHub Settings → Pages → Add a domain → add the `TXT` record it shows at GoDaddy → Verify. Also turn off Issues, Wiki and Projects on the repository (public writing surfaces nobody needs).
6. Release day: (a) change `data-cta="soon"` to `data-cta="launch"` on every page (`index.html`, `support.html`, `privacy.html`, `terms.html`) and in the template inside `_dev/legal.py`, one find-and-replace; (b) put the App Store ID in place of `APPSTOREID` everywhere it appears (the badge links, the Get Poise links in each top row, and the commented `apple-itunes-app` meta tag in `index.html`'s `<head>`), then uncomment that tag (Safari on iPhone then shows Apple's own "open in the App Store" strip). Commit and push; Pages redeploys in about a minute.
7. Visit counter: PostHog, the app's own project, is already on every page (page views only, no cookies, nothing stored on the visitor's device, no replay, no identifying). It runs only when the address is withpoise.app, so nothing to switch on: once the site is live, the numbers appear under Web analytics in PostHog. Visitor counts read high there (each page load counts as a new visitor, by design); page views, pages, referrers and countries are the numbers to trust.
