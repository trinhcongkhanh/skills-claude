<div align="center">

# 🛡️ skills-claude

**Bộ Agent Skills cá nhân cho Claude — làm việc chống hiểu lầm, phong cách Cyber dark, code an toàn và chuẩn xây dựng web/app/extension.**

[![Release](https://img.shields.io/github/v/release/trinhcongkhanh/skills-claude?color=00E5A0&labelColor=0B1220)](https://github.com/trinhcongkhanh/skills-claude/releases/latest)
[![Validate](https://github.com/trinhcongkhanh/skills-claude/actions/workflows/validate.yml/badge.svg)](https://github.com/trinhcongkhanh/skills-claude/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-38BDF8?labelColor=0B1220)](LICENSE)

[Cài đặt](#-cài-đặt-nhanh) · [Các skill](#-các-skill) · [Cách dùng](docs/USAGE.md) · [Tự tuỳ biến](docs/CUSTOMIZE.md) · [English](#-english)

</div>

---

## 📌 Đây là gì?

**Skill** là một thư mục chứa file `SKILL.md` (hướng dẫn + metadata) và có thể kèm tài nguyên (template, CSS, ví dụ). Claude chỉ đọc phần mô tả ngắn của mỗi skill lúc đầu; khi yêu cầu của bạn khớp, Claude mới nạp toàn bộ nội dung (*progressive disclosure*). Bạn **không cần gọi tên skill** — cứ làm việc bình thường.

Bộ này do **Trinh Cong Khanh** (sinh viên Cyber Security) xây dựng từ cách làm việc, gu thiết kế và chuyên môn của mình, để Claude:
- hiểu đúng yêu cầu ngay lần đầu,
- tạo tài liệu / slide / sơ đồ cùng một phong cách,
- viết code, database, web app, extension đúng chuẩn bảo mật.

## 🧩 Các skill

| Skill | Khi nào Claude dùng | Nội dung chính |
|---|---|---|
| [`khanh-work-protocol`](plugins/khanh-toolkit/skills/khanh-work-protocol/SKILL.md) | Mọi yêu cầu | Đọc đúng mục tiêu, nêu giả định, chỉ hỏi khi cần (trắc nghiệm + gợi ý), trả lời thẳng trước → giải thích "why" → ví dụ → nguồn; kiểm chứng trước khi báo xong. Mặc định tiếng Việt, giữ thuật ngữ tiếng Anh. |
| [`cyber-dark-style`](plugins/khanh-toolkit/skills/cyber-dark-style/SKILL.md) | Tài liệu, slide, sơ đồ, chart, web, mockup | Màu navy `#0B1220` · neon `#00E5A0` · cyan `#38BDF8`; font Inter + JetBrains Mono; bảng cỡ chữ; dark mode cho màn hình, light mode cho bản in; màu mức độ lỗ hổng. Đạt WCAG AA. |
| [`secure-code-and-lab`](plugins/khanh-toolkit/skills/secure-code-and-lab/SKILL.md) | Code, database, review bảo mật, lab/CTF | Chuẩn code, SQL an toàn, checklist CWE, quy trình lab có kiểm tra phạm vi được phép, map MITRE ATT&CK, mẫu write-up. |
| [`app-build-standards`](plugins/khanh-toolkit/skills/app-build-standards/SKILL.md) | Web app, API, mobile/desktop, browser extension | WCAG 2.2, Core Web Vitals, bảo mật API, Electron/Tauri, Manifest V3, OWASP Top 10:2025, testing, checklist phát hành. |

Các skill phối hợp với nhau: `khanh-work-protocol` điều phối, tự gọi 3 skill còn lại khi phù hợp.

## 🚀 Cài đặt nhanh

> Chi tiết từng bước + xử lý lỗi: **[docs/INSTALL.md](docs/INSTALL.md)**

### Cách 1 — claude.ai / Claude Desktop (không cần code)
1. Tải các file `.zip` ở trang **[Releases mới nhất](https://github.com/trinhcongkhanh/skills-claude/releases/latest)** (mỗi skill một file, không giải nén).
2. Bật **Code execution** trong Settings → Capabilities.
3. Vào **Customize → Skills** → bấm **+** → **Create skill** → **Upload a skill** → chọn file `.zip`.
4. Lặp lại cho từng skill, đảm bảo công tắc đang bật.

### Cách 2 — Claude Code (plugin marketplace)
```text
/plugin marketplace add trinhcongkhanh/skills-claude
/plugin install khanh-toolkit@khanh-skills
```

### Cách 3 — Thủ công (Claude Code, mọi agent hỗ trợ SKILL.md)
```bash
git clone https://github.com/trinhcongkhanh/skills-claude.git
mkdir -p ~/.claude/skills
cp -r skills-claude/plugins/khanh-toolkit/skills/* ~/.claude/skills/
```

## 💡 Thử ngay

Sau khi cài, thử các câu sau (không cần nhắc tên skill):

```text
Viết báo cáo 2 trang về lỗ hổng IDOR, có phần phòng thủ.
→ cyber-dark-style (light mode) + secure-code-and-lab + khanh-work-protocol

Tạo extension Chrome lưu ghi chú cho từng trang web.
→ app-build-standards (Manifest V3, quyền tối thiểu, message an toàn)

Hướng dẫn mình làm máy "Lame" trên HackTheBox rồi viết write-up.
→ secure-code-and-lab (kiểm tra phạm vi, ATT&CK, mẫu write-up)
```
Xem thêm ví dụ: **[docs/USAGE.md](docs/USAGE.md)**

## 📁 Cấu trúc repo

```text
skills-claude/
├── .claude-plugin/marketplace.json        # Đăng ký marketplace cho Claude Code
├── plugins/khanh-toolkit/
│   ├── .claude-plugin/plugin.json         # Metadata plugin
│   └── skills/
│       ├── khanh-work-protocol/SKILL.md
│       ├── cyber-dark-style/
│       │   ├── SKILL.md
│       │   ├── references/palette.md      # Bảng màu đầy đủ + tỉ lệ tương phản
│       │   └── assets/{theme.css, mermaid-theme.json}
│       ├── secure-code-and-lab/
│       │   ├── SKILL.md
│       │   └── references/writeup-template.md
│       └── app-build-standards/
│           ├── SKILL.md
│           ├── assets/manifest.v3.json
│           └── references/extension-messaging-example.md
├── scripts/
│   ├── validate_skills.py                 # Kiểm tra cấu trúc + frontmatter
│   └── package_skills.sh                  # Đóng gói .zip
├── .github/workflows/                     # CI: validate + tự tạo Release khi push tag
└── docs/                                  # INSTALL, USAGE, CUSTOMIZE
```

## 🔧 Tự làm bộ skill của riêng bạn
Fork repo → đổi màu, font, tên tác giả, ngôn ngữ → chạy `python3 scripts/validate_skills.py` → push tag. Hướng dẫn đầy đủ: **[docs/CUSTOMIZE.md](docs/CUSTOMIZE.md)**.

## 🔒 An toàn
- Bộ skill **chỉ chứa Markdown, CSS, JSON** — không có script nào chạy trong phiên của Claude. Hãy tự đọc trước khi cài, như với mọi skill bên thứ ba.
- Nội dung bảo mật chỉ dành cho **lab, CTF và kiểm thử có ủy quyền**.
- Báo lỗ hổng: xem [SECURITY.md](SECURITY.md).

## 🤝 Đóng góp
Issue và Pull Request đều hoan nghênh — xem [CONTRIBUTING.md](CONTRIBUTING.md). Lịch sử phiên bản: [CHANGELOG.md](CHANGELOG.md).

---

## 🌐 English

Personal **Agent Skills** pack for Claude by Trinh Cong Khanh (Cyber Security student): a misunderstanding-proof work protocol, a "Cyber dark" visual style (navy / neon green / cyan, Inter + JetBrains Mono), secure code + cyber lab workflow, and build standards for web apps, APIs, desktop/mobile apps and Manifest V3 browser extensions.

- **claude.ai / Desktop:** download the `.zip` files from [Releases](https://github.com/trinhcongkhanh/skills-claude/releases/latest) → Customize → Skills → + → Create skill → Upload a skill.
- **Claude Code:** `/plugin marketplace add trinhcongkhanh/skills-claude` then `/plugin install khanh-toolkit@khanh-skills`.
- Responses default to Vietnamese; edit `khanh-work-protocol/SKILL.md` §1 to change.

License: [MIT](LICENSE)
