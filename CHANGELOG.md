# Changelog

Định dạng theo [Keep a Changelog](https://keepachangelog.com/), phiên bản theo [SemVer](https://semver.org/).

## [Unreleased]

## [1.1.0] - 2026-11-19
### Added
- Skill `app-build-standards`: chuẩn web app, API, mobile/desktop (Electron, Tauri), browser extension Manifest V3, OWASP Top 10:2025, Core Web Vitals, release checklist.
- Template `manifest.v3.json` và ví dụ xử lý message an toàn cho extension.
- Tài liệu: `docs/INSTALL.md`, `docs/USAGE.md`, `docs/CUSTOMIZE.md`, `CONTRIBUTING.md`, `SECURITY.md`.
- GitHub Actions: validate mọi push/PR, tự tạo Release kèm `.zip` khi push tag `v*`.
- Script `scripts/validate_skills.py`, `scripts/package_skills.sh`.

### Changed
- `khanh-work-protocol` gọi `app-build-standards` cho việc web/app/extension.
- `secure-code-and-lab` chuyển sang OWASP Top 10:2025.

## [1.0.0] - 2026-11-18
### Added
- Skill `khanh-work-protocol`, `cyber-dark-style`, `secure-code-and-lab`.
- Plugin marketplace cho Claude Code.
