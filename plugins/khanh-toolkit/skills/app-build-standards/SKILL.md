---
name: app-build-standards
description: Use when building, reviewing or planning web apps, websites, APIs, mobile or desktop apps (Electron, Tauri), and browser extensions (Chrome, Edge, Firefox) - project setup, structure, security, accessibility, performance, Manifest V3 rules, testing and release checklist.
---

# App build standards

Standards for shipping web apps, APIs, mobile/desktop apps and browser extensions that are secure, fast, accessible and maintainable. Works together with `secure-code-and-lab` (general code + database + CWE review) and `cyber-dark-style` (UI look) when installed.

Versions of frameworks and tools change often: check the official docs for the current stable version before pinning, and say when a recommendation may be outdated.

---
## 0. Before writing code
1. One-paragraph spec: who uses it, the 3-5 core features, what data it stores, where it runs.
2. Threat sketch (5 minutes): what is valuable (accounts, payments, personal data), who could attack, the entry points (forms, APIs, uploads, messages, deep links).
3. Pick the smallest stack that fits; explain the choice in the README.
4. Create: `README.md`, `.gitignore`, `.env.example` (no real values), `LICENSE`, linter/formatter config, a `tests/` folder, CI file.

## 1. Rules for every project type
- **TypeScript with `strict: true`** for JS projects; type hints + a type checker (mypy/pyright) for Python.
- Lint + format on every commit (ESLint + Prettier, or Biome; Ruff for Python).
- Config from environment variables; secrets never in code, bundles, git or client apps.
- Validate every input at the trust boundary with a schema (Zod, Valibot, Pydantic). Client-side validation is UX only; the server decides.
- Dependencies: few, maintained, pinned with a lockfile; `npm audit` / `pip-audit` / Dependabot in CI.
- Git: small commits, Conventional Commits (`feat:`, `fix:`, `docs:`), protected main branch, PR review.
- Versioning: SemVer (`MAJOR.MINOR.PATCH`) + `CHANGELOG.md`.
- CI pipeline: install -> lint -> type check -> test -> audit -> build. A failing step blocks merge.

---
## 2. Web frontend
**Structure** - group by feature (`features/auth`, `features/cart`), shared UI in `components/`, API calls in one `api/` layer, no fetch calls scattered in components.

**Accessibility (WCAG 2.2 AA)**
- Semantic HTML first (`button`, `nav`, `main`, `label`), ARIA only when needed.
- Everything works with keyboard; visible focus ring; logical tab order.
- Every input has a label; every meaningful image has `alt`; text contrast 4.5:1 or better.
- Test with Lighthouse / axe DevTools and a quick keyboard-only pass.

**Performance (Core Web Vitals, 75th percentile of real users)**
- LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less.
- Responsive images (`srcset`, modern formats, `width`/`height` set), lazy-load below the fold, code-split routes, preload the LCP image and fonts, avoid long main-thread tasks.

**Security**
- Never put untrusted data into `innerHTML`, `dangerouslySetInnerHTML`, `eval`, `new Function`; use `textContent` or the framework's escaping. If HTML is required, sanitize with DOMPurify.
- Content-Security-Policy (start strict: `default-src 'self'`), plus `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `frame-ancestors` to block clickjacking, HSTS on HTTPS.
- Auth tokens in `HttpOnly; Secure; SameSite=Lax` (or `Strict`) cookies, not `localStorage`.
- Third-party scripts: minimum, with Subresource Integrity (`integrity=`) when loaded from a CDN.

**UX basics** - mobile-first layout, loading / empty / error states for every data view, form errors next to the field, Vietnamese + English text kept in i18n files if the app is bilingual.

---
## 3. Backend and APIs
- REST: nouns in plural (`/api/v1/orders/{id}`), correct verbs and status codes, versioned path, pagination (`limit` + cursor), filtering via query params.
- Errors in one JSON shape (RFC 9457 Problem Details: `type`, `title`, `status`, `detail`); never leak stack traces or SQL errors.
- **AuthN**: proven library or provider (no home-made crypto); passwords hashed with Argon2id; MFA for admin; short-lived access tokens + rotating refresh tokens if using JWT; validate `alg`, `iss`, `aud`, `exp`.
- **AuthZ**: check ownership on every object access (`order.user_id == current_user.id`), deny by default, separate admin routes. This prevents IDOR.
- Rate limiting and lockout on login, signup, password reset, OTP, and expensive endpoints.
- CORS: explicit allow-list of origins; never `*` together with credentials.
- Webhooks and payments: verify signatures, check amounts server-side, make handlers idempotent (idempotency key), log every state change.
- Uploads: allow-list file types by content, size limit, random file names, store outside web root or in object storage, scan if possible.
- Outbound requests from user-supplied URLs: allow-list hosts, block internal ranges and cloud metadata (SSRF).
- Observability: structured logs with request ID, health endpoint (`/healthz`), alerts on auth failures and 5xx spikes.
- Document the API with OpenAPI.

---
## 4. Mobile and desktop apps
- Treat the app as public: anything inside the bundle (keys, endpoints, logic) can be extracted. Real secrets stay on the server.
- Store tokens in the OS secure store: iOS Keychain, Android Keystore / EncryptedSharedPreferences, OS credential manager on desktop.
- HTTPS only, default certificate validation (no "trust all certs" in release builds).
- Request the minimum OS permissions, at the moment they are needed, with a reason shown.
- Validate deep links / custom URL schemes like any other input.
- Mobile security baseline: OWASP MASVS; test with OWASP MASTG.
- **Electron**: `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true`, expose a minimal API through `contextBridge` in the preload script, never load remote content into a window with Node access, validate IPC messages, set a CSP, use `shell.openExternal` only for allow-listed URLs, enable auto-update with signed builds.
- **Tauri**: grant only the needed capabilities/permissions per window, scope filesystem and shell access.
- Sign release builds; keep signing keys out of the repo.

---
## 5. Browser extensions
**Platform facts**: Chrome removed all remaining Manifest V2 extensions from the Chrome Web Store on Aug 31, 2026; build with **Manifest V3** only. Edge is retiring MV2 too. Firefox supports MV3 (with some differences, e.g. background scripts); check MDN for cross-browser details.

**Architecture**
- `manifest.json` (MV3) -> background **service worker** (event-driven, can be stopped any time: keep no state in globals, persist to `chrome.storage`) -> content scripts (run inside web pages) -> popup / options / side panel pages.
- Template: `assets/manifest.v3.json`.

**Permissions (least privilege)**
- Prefer `activeTab` over broad host permissions; use `optional_permissions` / `optional_host_permissions` and request at the moment of use.
- Never request `<all_urls>`, `tabs`, `history`, `cookies`, `webRequest` unless the single purpose truly needs it. Each permission must be justified in the store listing.

**Security**
- No remotely hosted code: MV3 forbids loading or `eval`-ing code from the network. Bundle everything; fetch only data.
- Treat the web page as hostile: content scripts must not trust page DOM or `window.postMessage`; validate origin and message shape.
- In `chrome.runtime.onMessage`, check `sender.id` / `sender.url` and validate the payload with a schema before acting.
- Inject UI with `textContent` / DOM APIs, or inside a Shadow DOM; never insert page-derived strings with `innerHTML`.
- Sensitive temporary data in `chrome.storage.session`; do not store passwords; minimize stored personal data.
- Keep the default extension-page CSP (`script-src 'self'`); never weaken it.
- Network blocking/modifying: use `declarativeNetRequest`.

**Store and privacy** - single clear purpose, privacy policy if any user data is handled, accurate data-use disclosure, no obfuscated code (minified is fine).

**Cross-browser** - use the `browser.*` namespace via `webextension-polyfill` or a framework such as WXT or Plasmo; test in Chrome and Firefox.

**Testing** - unit-test logic; E2E with Playwright loading the unpacked extension in Chromium; test service worker restarts (state must survive).

---
## 6. Testing pyramid
- Unit (Vitest / Jest / pytest): pure logic, validation, permission checks.
- Integration: API + real test database (container), auth flows, webhooks.
- E2E (Playwright): the 3-5 core user journeys, on mobile and desktop widths.
- Security tests: one malicious-input test per input (XSS payload, SQLi string, oversized body, other user's ID), plus a DAST scan (OWASP ZAP baseline) against a staging build you own.

---
## 7. OWASP Top 10:2025 quick map (final edition, Jan 2026)
| Category | Where it bites in apps |
|---|---|
| A01 Broken Access Control (now includes SSRF) | IDOR, missing role checks, SSRF from URL fetchers |
| A02 Security Misconfiguration | debug on, default creds, open CORS, verbose errors |
| A03 Software Supply Chain Failures | malicious/vulnerable packages, unpinned deps, CI secrets |
| A04 Cryptographic Failures | weak hashing, no TLS, keys in code |
| A05 Injection | SQL/NoSQL/command injection, XSS |
| A06 Insecure Design | no rate limit, trusting client prices |
| A07 Authentication Failures | weak sessions, no MFA, JWT misuse |
| A08 Software or Data Integrity Failures | unsigned updates, unsafe deserialization |
| A09 Logging & Alerting Failures | no audit trail, no alerts |
| A10 Mishandling of Exceptional Conditions | fail-open errors, leaked stack traces |
Verify names at owasp.org/Top10 before quoting in formal reports.

---
## 8. Release checklist
- [ ] Lint, type check, tests, audit all green in CI
- [ ] No secrets in repo or build output (gitleaks)
- [ ] Security headers / CSP / CORS verified on the deployed URL
- [ ] Lighthouse: Performance and Accessibility checked on mobile
- [ ] Error, empty and loading states tested; backups and rollback plan ready
- [ ] Extensions: permissions re-reviewed, privacy disclosure updated, version bumped
- [ ] README + CHANGELOG updated; tag the release
