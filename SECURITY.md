# Security Policy

## Phạm vi
Repo này chỉ chứa hướng dẫn (Markdown), CSS và JSON. Không có script nào được thiết kế để chạy trong phiên của Claude. Các script trong `scripts/` chỉ dùng cho CI (kiểm tra và đóng gói).

## Báo cáo lỗ hổng
Nếu bạn phát hiện nội dung có thể khiến Claude hành xử không an toàn (ví dụ: prompt injection, hướng dẫn sai gây lỗ hổng, link độc hại), vui lòng **không mở Issue công khai**. Hãy dùng [GitHub Private Vulnerability Reporting](https://github.com/trinhcongkhanh/skills-claude/security/advisories/new).

Mình sẽ phản hồi trong vòng 7 ngày.

## Khuyến nghị cho người dùng
- Luôn đọc `SKILL.md` và mọi file đi kèm trước khi cài bất kỳ skill bên thứ ba nào.
- Chỉ tải `.zip` từ trang Releases chính thức của repo này.
- Nội dung bảo mật chỉ dùng cho lab, CTF và kiểm thử có ủy quyền.
