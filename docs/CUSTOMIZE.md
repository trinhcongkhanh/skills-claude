# 🔧 Tự tuỳ biến thành bộ skill của bạn

## 1. Fork và clone
1. Bấm **Fork** trên trang repo.
2. Clone bản fork:
```bash
git clone https://github.com/<your-username>/skills-claude.git
cd skills-claude
```

## 2. Hiểu cấu trúc một skill
```text
ten-skill/
├── SKILL.md          # BẮT BUỘC: frontmatter YAML + hướng dẫn
├── references/       # Tuỳ chọn: tài liệu Claude đọc khi cần
├── assets/           # Tuỳ chọn: template, CSS, ảnh, font
└── scripts/          # Tuỳ chọn: code Claude có thể chạy
```
Frontmatter tối thiểu:
```yaml
---
name: ten-skill            # kebab-case, trùng tên thư mục
description: Use when ...  # Claude dựa vào câu này để quyết định khi nào dùng skill
---
```
Quy tắc quan trọng:
- Tên file đúng là `SKILL.md` (phân biệt hoa thường); tên thư mục kebab-case.
- Không dùng `<` `>` trong frontmatter; tên skill không chứa "claude" hay "anthropic".
- `description` nói **khi nào** dùng skill, càng cụ thể càng kích hoạt đúng (dưới 1024 ký tự).
- Giữ `SKILL.md` gọn; chi tiết dài đưa vào `references/`.

## 3. Đổi những gì?

| Muốn đổi | Sửa file |
|---|---|
| Ngôn ngữ trả lời, phong cách trả lời | `khanh-work-protocol/SKILL.md` §1, §3 |
| Màu sắc | `cyber-dark-style/SKILL.md` §1 + `references/palette.md` + `assets/theme.css` + `assets/mermaid-theme.json` |
| Font, cỡ chữ, lề | `cyber-dark-style/SKILL.md` §2, §3 |
| Tên tác giả trên tài liệu | `cyber-dark-style/SKILL.md` §3, `secure-code-and-lab/references/writeup-template.md` |
| Chuẩn code/stack riêng | `secure-code-and-lab/SKILL.md`, `app-build-standards/SKILL.md` |
| Tên repo / plugin | `.claude-plugin/marketplace.json`, `plugins/*/.claude-plugin/plugin.json`, README |

Khi đổi màu, kiểm tra tương phản đạt WCAG AA (chữ thường ≥ 4.5:1), ví dụ bằng WebAIM Contrast Checker.

## 4. Thêm skill mới
```bash
mkdir -p plugins/khanh-toolkit/skills/my-new-skill
$EDITOR plugins/khanh-toolkit/skills/my-new-skill/SKILL.md
```
Plugin tự nhận mọi thư mục trong `skills/`, không cần khai báo thêm.

## 5. Kiểm tra và đóng gói
```bash
python3 scripts/validate_skills.py     # kiểm tra cấu trúc, frontmatter, JSON
bash scripts/package_skills.sh         # tạo dist/*.zip để thử upload
```
Nếu có Claude Code: `claude plugin validate .`

## 6. Phát hành
```bash
# cập nhật version trong marketplace.json, plugin.json và CHANGELOG.md
git add -A
git commit -m "feat: add my-new-skill"
git tag v1.2.0
git push origin main --tags
```
GitHub Actions (`.github/workflows/release.yml`) sẽ tự validate, đóng gói từng skill thành `.zip` và tạo Release với các file đính kèm.

> Lần đầu dùng Actions trên bản fork: vào tab **Actions** bấm *Enable workflows*; vào Settings → Actions → General → Workflow permissions chọn **Read and write permissions** để workflow tạo được Release.
