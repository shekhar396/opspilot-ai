# OpsPilot AI - Release Notes

All notable changes to this project are documented in this file.

---

# Current Stable Release

# v0.3.0 - Alert History and Operational Visibility
Release Date: 2026-05-15

OpsPilot AI v0.3.0 is a major MVP milestone. The project now persists alerts in SQLite, exposes alert history through FastAPI endpoints, and provides summary data for operational visibility. This moves OpsPilot AI from real-time monitoring toward a persistent monitoring platform.

---

## Key Features

### Alert Persistence

- SQLite-backed alert history
- SQLAlchemy ORM integration
- Stored alert severity, source, details, and timestamps
- Persistent monitoring history across worker runs

### Alert APIs

- List persisted alerts
- Retrieve recent alerts
- Retrieve alert details by ID
- Filter alerts by severity
- Filter alerts by source
- Limit alert result size
- Retrieve alert summary counts

### Cooldown Protection

- Repeated alerts are suppressed during cooldown windows
- Alert noise is reduced before Telegram delivery
- Monitoring remains suitable for continuous background execution

---

## API Endpoints

| Endpoint             | Description                  |
| -------------------- | ---------------------------- |
| GET /alerts/         | List persisted alerts        |
| GET /alerts/recent   | List recent alerts           |
| GET /alerts/summary  | Return alert summary metrics |
| GET /alerts/{id}     | Return a single alert        |

Examples:

```text
GET /alerts/?severity=warning
GET /alerts/?source=docker
GET /alerts/?severity=warning&source=system&limit=20
GET /alerts/summary
```

---

## Architecture Improvements

v0.3.0 introduces the persistent alert visibility path:

```text
Metrics
   ↓
Alert Engine
   ↓
SQLite Alert Storage
   ↓
Alert APIs
   ↓
Telegram Notification
```

This architecture keeps the MVP lightweight while creating a foundation for dashboards, AI diagnosis, incident summaries, and future multi-server monitoring.

---

## Monitoring Platform Evolution

OpsPilot AI is evolving from a command-based monitoring assistant into a persistent operations platform. With stored alerts and queryable APIs, the system can now support:

- Alert history review
- Operational trend analysis
- Future dashboard views
- AI-assisted incident diagnosis
- Long-term monitoring workflows

---

# Previous Releases

## v0.3.0 - Infrastructure Monitoring Foundation
Release Date: 2026-05-11

- Linux system monitoring
- Docker container monitoring
- Telegram monitoring commands
- FastAPI service structure
- Modular monitoring services

## v0.2.0 - Linux System Monitoring
Release Date: 2026-05-10

- CPU monitoring
- RAM monitoring
- Disk monitoring
- Host information collection
- `/status` Telegram command

## v0.1.0 - Initial Project Foundation
Release Date: 2026-05-09

- Initial FastAPI project setup
- Telegram bot integration foundation
- Project folder structure
- Environment configuration
- MVP roadmap definition

---

# Upcoming Focus

- Monitoring dashboard
- Jenkins monitoring
- AI alert diagnosis
- AI log analysis
- Conversational DevOps assistant
