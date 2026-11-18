# 💡 Cách dùng và ví dụ

Bạn **không cần gọi tên skill**. Claude đọc mô tả của từng skill và tự kích hoạt khi yêu cầu phù hợp. Muốn chắc chắn, có thể nói thẳng: *"dùng skill `cyber-dark-style`"*.

## Viết yêu cầu sao cho Claude hiểu đúng (kết hợp `khanh-work-protocol`)

Một yêu cầu tốt có 4 phần — skill sẽ tự hỏi lại nếu thiếu phần quan trọng:

```text
[Mục tiêu]   Mình cần một báo cáo đánh giá bảo mật cho web bán hàng của nhóm.
[Bối cảnh]   Backend Node.js + PostgreSQL, deploy trên AWS, đồ án môn học.
[Ràng buộc]  Tối đa 5 trang, tiếng Việt, nộp bản PDF.
[Đầu ra]     Có bảng phát hiện theo mức độ + cách khắc phục.
```

## Ví dụ theo từng skill

### 🧠 khanh-work-protocol (mọi yêu cầu)
```text
So sánh JWT và session cookie, nên dùng cái nào cho app của mình?
```
Kỳ vọng: câu trả lời thẳng ở đầu → giải thích cơ chế bên dưới → ví dụ code → góc tấn công + phòng thủ → nguồn (RFC, OWASP) → key takeaways.

### 🎨 cyber-dark-style
```text
Làm 8 slide thuyết trình về Zero Trust cho lớp.
Vẽ sơ đồ mạng có DMZ, firewall và web server.
Tạo trang landing page giới thiệu CTF team của mình.
```
Kỳ vọng: nền tối navy, điểm nhấn neon, Inter + JetBrains Mono; tài liệu để in thì chuyển sang nền trắng.

### 🔐 secure-code-and-lab
```text
Review đoạn code login này giúp mình. [dán code]
Thiết kế database cho hệ thống quản lý thư viện.
Mình đang làm máy Blue trên TryHackMe, hướng dẫn và viết write-up.
```
Kỳ vọng: phát hiện gắn mã CWE + mức độ; SQL parameterized; lab có bước xác nhận phạm vi được phép, bảng MITRE ATT&CK, phần phát hiện/phòng thủ.

### 🏗️ app-build-standards
```text
Khởi tạo project React + API Express có đăng nhập.
Viết extension Chrome đếm thời gian dùng từng trang web.
Checklist trước khi deploy web app lên production.
```
Kỳ vọng: cấu trúc theo feature, TypeScript strict, validate bằng schema, Manifest V3 với quyền tối thiểu, CSP, test Playwright, checklist phát hành.

## Mẹo
- Gửi kèm file (code, đề bài, báo cáo cũ) để Claude có đủ ngữ cảnh.
- Nếu kết quả lệch, nói rõ phần nào lệch — skill được thiết kế để sửa theo phản hồi, không làm lại từ đầu.
- Kết hợp được: *"Viết write-up máy này theo style của mình và xuất PDF"*.
