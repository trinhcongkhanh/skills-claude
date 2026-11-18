---
name: cyber-dark-style
description: Use whenever creating any visual or formatted output - documents, reports, slides, diagrams, charts, web pages, mockups - to apply the Cyber dark brand (navy, neon green, cyan; Inter + JetBrains Mono) with fixed sizes and layout rules.
---

# Cyber dark style

Personal brand system of Trinh Cong Khanh: security / terminal feel, clean and readable. Two modes:
- **Dark mode** - screens: slides, web pages, dashboards, diagrams, cover images.
- **Light mode** - anything printed or submitted (reports, Word/PDF, Docs): white paper, same accents darkened for contrast.

All color pairs below were checked for WCAG AA contrast (4.5:1 or better). Full tokens: `references/palette.md`. Ready CSS: `assets/theme.css`. Mermaid theme: `assets/mermaid-theme.json`.

## 1. Color tokens (summary)
| Token | Dark mode | Light mode | Use |
|---|---|---|---|
| background | #0B1220 | #FFFFFF | page / slide |
| surface | #111A2E | #F8FAFC | cards, table stripes |
| border | #1F2A44 | #E2E8F0 | lines, dividers |
| text | #E6EDF7 | #0F172A | body text |
| muted | #94A3B8 | #475569 | captions, metadata |
| primary | #00E5A0 | #047857 | accent, H2 bar, key numbers |
| secondary | #38BDF8 | #0369A1 | links, info |
| warning | #F59E0B | #B45309 | warnings |
| danger | #F43F5E | #BE123C | errors, critical |

Rules: one primary accent per view; never more than 3 accent colors on one page/slide; never put neon green text on white (use #047857 instead).

**Security severity colors** (findings, CVSS ratings), same in both modes for badges with white or navy text as noted in palette.md: Critical #BE123C, High #C2410C, Medium #B45309, Low #0369A1, Info #475569.

## 2. Typography
- Body / headings: **Inter** (fallback: "Segoe UI", Roboto, Arial, sans-serif). Supports Vietnamese diacritics.
- Code, commands, hashes, IPs, file paths: **JetBrains Mono** (fallback: Consolas, "Courier New", monospace).
- Never use more than these two families.

| Element | Document (pt) | Slide (pt) | Web (px) |
|---|---|---|---|
| Title / H1 | 22 bold | 40 bold | 32 |
| H2 | 16 semibold | 28 semibold | 24 |
| H3 | 13 semibold | 22 | 18 |
| Body | 11 | 20-24 | 16 |
| Caption / table | 9.5 | 14 | 13 |
| Code | 10 | 16-18 | 14 |

Line height 1.5 for body, 1.2 for headings. Left-aligned text (no justify - it breaks Vietnamese spacing).

## 3. Documents and reports (light mode)
- Page A4, margins 2.5 cm left, 2 cm other sides.
- Cover: title (22pt navy #0B1220), subtitle (muted), author "Trinh Cong Khanh", date, a thin 4px #047857 bar on top.
- H1 navy #0B1220. H2 navy with a 3px left bar in #047857. H3 #0F172A.
- Structure for reports: Summary -> Context -> Main content -> Findings/Results -> Recommendations -> References.
- Tables: header row #0B1220 background, white bold text; zebra rows #F8FAFC; numbers right-aligned.
- Code blocks: background #F1F5F9, 1px border #E2E8F0, JetBrains Mono 10pt, language label on top.
- Callouts (left border 4px + light tint): Note #0369A1, Tip #047857, Warning #B45309, Danger #BE123C.
- Header: document title (muted, 9pt). Footer: "Trinh Cong Khanh - page X/Y".
- When the output is a built-in editor document type that only supports some styling, keep the structure, heading levels, tables and callouts; do not fight the editor for exact colors.
- Never shrink fonts or margins to fit a page limit - cut words instead.

## 4. Slides (dark mode, 16:9)
- Background #0B1220; title #E6EDF7; one accent #00E5A0.
- One idea per slide; max 5 bullets, max ~8 words per bullet.
- Title slide: big title left-aligned, thin neon line under it, author + date in muted.
- Section divider: full #111A2E background, big number in #00E5A0.
- Code slide: JetBrains Mono 16-18pt on #111A2E card, highlight the important line with a #00E5A0 left marker.
- Data slide: one chart, one takeaway sentence as the title ("Port 22 is the most attacked service"), not "Chart 1".
- Footer: small muted text, slide number bottom right.

## 5. Diagrams and charts
- Use `assets/mermaid-theme.json` for Mermaid (`%%{init: ...}%%`).
- Nodes: fill #111A2E, border #38BDF8, text #E6EDF7; highlighted node border #00E5A0; attacker / threat nodes border #F43F5E.
- Arrows #94A3B8; label text 12-14px.
- Network diagrams: zone boxes (Internet, DMZ, Internal) with dashed borders and labels.
- Chart series order: #00E5A0, #38BDF8, #A78BFA, #F59E0B, #F43F5E. Gridlines #1F2A44, no 3D, no pie with more than 5 slices.

## 6. Web pages, artifacts, mockups
- Link or inline `assets/theme.css`. Default dark mode; respect `prefers-color-scheme: light` with the light tokens.
- Radius 10px cards, 6px buttons; spacing scale 4/8/12/16/24/32/48.
- Primary button: bg #00E5A0, text #0B1220. Secondary: transparent, border #38BDF8, text #38BDF8.
- Subtle terminal touches are fine (monospace labels, `$` prompt in hero) - no fake hacker clichés (green matrix rain, skulls, hoodies).

## 7. Final check
- Only Inter + JetBrains Mono used; sizes match the table.
- Correct mode (dark for screens, light for print/submission).
- Max 3 accent colors visible; text contrast OK.
- Open/render the output and look at it before delivering.
