# Changelog

## v0.4.0 - Jenkins Monitoring

### Added

- Jenkins API integration
- Jenkins monitoring APIs
- Jenkins failed build monitoring
- Jenkins summary endpoint
- Telegram alerts for failed Jenkins builds
- SQLite-backed Jenkins alert persistence
- Restart-safe Jenkins failed-build deduplication
- Graceful alert worker shutdown

---

## v0.3.0 - Alert History and Alert APIs

### Added

- SQLite integration for MVP alert storage
- Persistent alert history
- Alert history APIs
- Severity and source filtering support
- Alert summary endpoint
- Cooldown protection for repeated alerts

---

## v0.2.0 - Alerting Engine

### Added

- Rule-based alert engine
- CPU/RAM/Disk threshold monitoring
- Docker alert support
- Telegram alert delivery
- Alert cooldown protection
- Background alert worker
- GitHub Actions CI pipeline

---

## v0.1.0 - Initial MVP

### Added

- FastAPI backend
- Telegram bot integration
- System metrics monitoring
- Docker monitoring
- Initial project architecture
