# OpsPilot AI - Release Notes

All notable changes to this project are documented in this file.

---

# Current Stable Release

# v0.4.0 - Jenkins Monitoring and CI/CD Observability
Release Date: 2026-05-18

OpsPilot AI v0.4.0 adds Jenkins monitoring to the MVP platform. This release extends OpsPilot AI beyond Linux and Docker visibility into CI/CD pipeline health, enabling failed build detection, Jenkins APIs, Telegram notifications, and SQLite-backed alert persistence.

The milestone strengthens the production-style monitoring workflow: collect signals, evaluate alerts, persist history, avoid duplicate notifications, and notify operators in Telegram.

---

## Key Features

### Jenkins Monitoring

- Jenkins API integration
- Jenkins connection health checks
- Jenkins job listing
- Jenkins build detail inspection
- Failed build monitoring
- Jenkins summary metrics

### Jenkins Alerting

- Critical alerts for failed Jenkins builds
- Telegram notifications through the existing alert flow
- Alert details include job name, build number, build URL, result, and duration
- Runtime cooldown protection for alert noise reduction
- Restart-safe duplicate protection backed by SQLite alert history

### CI/CD Observability

v0.4.0 brings CI/CD failures into the same operational loop as infrastructure and Docker alerts. Failed builds are now visible through APIs, persisted in alert history, and delivered through Telegram.

---

## API Endpoints

| Endpoint                     | Description                |
| ---------------------------- | -------------------------- |
| GET /jenkins/health          | Jenkins connection health  |
| GET /jenkins/jobs            | List Jenkins jobs          |
| GET /jenkins/jobs/{job_name} | Get Jenkins job build data |
| GET /jenkins/failed          | List failed Jenkins builds |
| GET /jenkins/summary         | Jenkins build summary      |

---

## Architecture Improvements

v0.4.0 evolves the monitoring architecture into a broader operational pipeline:

```text
Linux Monitoring
Docker Monitoring
Jenkins Monitoring
       ↓
  Alert Engine
       ↓
SQLite Alert Storage
       ↓
   Alert APIs
       ↓
Telegram Notification
```

This keeps the MVP simple while establishing the foundation for AI-assisted build failure diagnosis, incident summaries, and future CI/CD troubleshooting recommendations.

---

## Monitoring Platform Evolution

OpsPilot AI now monitors infrastructure, containers, and CI/CD build outcomes in one alerting workflow. The system is better positioned for production-style operations because it can persist alert history, suppress noisy duplicates, survive worker restarts, and expose monitoring state through APIs.

---

# Previous Releases

## v0.3.0 - Alert History and Operational Visibility
Release Date: 2026-05-15

- SQLite-backed alert history
- Alert history APIs
- Severity and source filtering
- Alert summary endpoint
- Cooldown protection for repeated alerts

## v0.2.0 - Alerting Engine
Release Date: 2026-05-10

- Rule-based alert engine
- CPU/RAM/Disk threshold monitoring
- Docker alert support
- Telegram alert delivery
- Background alert worker
- GitHub Actions CI pipeline

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
- AI Jenkins build diagnosis
- AI alert diagnosis
- AI log analysis
- Conversational DevOps assistant