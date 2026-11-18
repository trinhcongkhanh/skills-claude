# Đóng góp

Cảm ơn bạn đã quan tâm! Mọi góp ý đều được hoan nghênh.

## Báo lỗi / đề xuất
Mở [Issue](https://github.com/trinhcongkhanh/skills-claude/issues) và mô tả:
- Bạn dùng Claude ở đâu (claude.ai, Desktop, Claude Code, API).
- Yêu cầu đã gửi cho Claude, kết quả mong đợi, kết quả thực tế.
- Skill liên quan.

## Gửi Pull Request
1. Fork, tạo nhánh: `git checkout -b feat/ten-thay-doi`.
2. Sửa skill, giữ đúng định dạng (xem [docs/CUSTOMIZE.md](docs/CUSTOMIZE.md)).
3. Chạy `python3 scripts/validate_skills.py` — phải pass.
4. Commit theo [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`.
5. Cập nhật `CHANGELOG.md` mục *Unreleased*.
6. Mở PR, mô tả lý do thay đổi.

## Nguyên tắc nội dung
- Thông tin kỹ thuật phải kiểm chứng được (tài liệu chính thức, RFC, OWASP, NIST, MITRE). Ghi nguồn khi thêm số liệu hoặc mốc thời gian.
- Không thêm script tải code từ mạng hoặc gửi dữ liệu ra ngoài.
- Nội dung tấn công chỉ ở mức học tập, luôn kèm phần phòng thủ và nhắc phạm vi được phép.
