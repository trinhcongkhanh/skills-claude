# 📦 Hướng dẫn cài đặt chi tiết

Chọn đúng cách theo nơi bạn dùng Claude:

| Bạn dùng | Cách cài | Định dạng |
|---|---|---|
| claude.ai (web), Claude Desktop, app mobile | [Cách 1](#cách-1--claudeai--claude-desktop) | File `.zip` mỗi skill |
| Claude Code (terminal / IDE) | [Cách 2](#cách-2--claude-code-plugin-marketplace) hoặc [Cách 3](#cách-3--claude-code-copy-thủ-công) | Thư mục |
| Claude API | [Cách 4](#cách-4--claude-api) | `.zip` qua Skills API |

---

## Cách 1 — claude.ai / Claude Desktop

**Yêu cầu:** gói có hỗ trợ Skills và đã bật code execution.

1. **Tải file**: vào [Releases mới nhất](https://github.com/trinhcongkhanh/skills-claude/releases/latest), tải các file:
   - `khanh-work-protocol.zip`
   - `cyber-dark-style.zip`
   - `secure-code-and-lab.zip`
   - `app-build-standards.zip`
   > Không giải nén. Mỗi zip chứa đúng **một thư mục skill** ở cấp trên cùng — đó là định dạng Claude yêu cầu.
2. **Bật code execution**: Settings → Capabilities → bật *Code execution and file creation*.
3. **Upload**: vào **Customize → Skills** (trên Desktop: biểu tượng settings → Customize) → bấm **+** → **Create skill** → **Upload a skill** → kéo thả file `.zip`.
4. Lặp lại cho từng skill. Mỗi skill xuất hiện trong danh sách và có công tắc bật/tắt.
5. **Kiểm tra**: mở chat mới, hỏi *"Bạn đang có những skill nào?"* hoặc thử một câu trong [USAGE.md](USAGE.md).

> 💡 Skill đã bật trên claude.ai cũng tự đồng bộ sang Claude Code khi bạn đăng nhập cùng tài khoản (Claude Code bản mới; gõ `/skills` để xem).

> Tên menu có thể thay đổi theo phiên bản ứng dụng. Nếu không thấy, xem trang hỗ trợ chính thức: https://support.claude.com/en/articles/12512180

---

## Cách 2 — Claude Code (plugin marketplace)

```text
/plugin marketplace add trinhcongkhanh/skills-claude
/plugin install khanh-toolkit@khanh-skills
```
> `trinhcongkhanh/skills-claude` là tên repo GitHub; `khanh-skills` là tên marketplace khai báo bên trong repo, nên lệnh install dùng `@khanh-skills`.

Hoặc dùng menu: `/plugin` → *Browse and install plugins* → chọn `khanh-skills` → `khanh-toolkit`.

**Cập nhật** khi có bản mới:
```text
/plugin marketplace update khanh-skills
```
**Gỡ:**
```text
/plugin uninstall khanh-toolkit@khanh-skills
```

---

## Cách 3 — Claude Code (copy thủ công)

```bash
git clone https://github.com/trinhcongkhanh/skills-claude.git
cd skills-claude

# Cài cho mọi project của bạn
mkdir -p ~/.claude/skills
cp -r plugins/khanh-toolkit/skills/* ~/.claude/skills/

# Hoặc chỉ cho một project (chia sẻ với team qua git)
mkdir -p /path/to/project/.claude/skills
cp -r plugins/khanh-toolkit/skills/* /path/to/project/.claude/skills/
```
Chỉ muốn 1 skill? Copy đúng thư mục đó, ví dụ `cp -r plugins/khanh-toolkit/skills/app-build-standards ~/.claude/skills/`.

---

## Cách 4 — Claude API

Upload từng file `.zip` qua endpoint Skills API (`/v1/skills`), rồi tham chiếu `skill_id` trong request có bật code execution tool. Xem tài liệu chính thức: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

---

## ❓ Xử lý lỗi thường gặp

| Triệu chứng | Nguyên nhân / cách sửa |
|---|---|
| Upload báo lỗi "invalid skill" | Bạn đã giải nén rồi nén lại sai cấp. Zip phải chứa `ten-skill/SKILL.md`, không phải `SKILL.md` ở gốc. Dùng file zip gốc từ Releases. |
| Không thấy mục Skills | Chưa bật code execution, hoặc gói hiện tại chưa hỗ trợ Skills. |
| Claude không dùng skill | Kiểm tra công tắc đang bật; mở **chat mới**; diễn đạt yêu cầu rõ hơn (ví dụ "làm slide", "viết extension"). Có thể nói thẳng: "dùng skill cyber-dark-style". |
| Trả lời bằng tiếng Việt khi bạn muốn tiếng Anh | Viết câu hỏi bằng tiếng Anh, hoặc sửa §1 trong `khanh-work-protocol/SKILL.md`. |
| `/plugin marketplace add` lỗi | Kiểm tra mạng / quyền truy cập GitHub; thử Cách 3. |
