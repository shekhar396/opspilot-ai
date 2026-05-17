# OpsPilot AI Architecture

## Architecture Status

OpsPilot AI is in active MVP development with:

- Linux, Docker, and Jenkins monitoring
- Rule-based alerting
- SQLite alert persistence
- Alert history APIs
- Telegram notifications
- GitHub Actions CI

Current Release: v0.4.0

---

# Current Architecture

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

Runtime cooldown protection reduces repeated notifications while persistent alert history enables restart-safe deduplication for Jenkins failed-build alerts.

---

# Core Components

## 1. Monitoring Services

Collect operational signals from Linux hosts, Docker runtimes, and Jenkins CI/CD pipelines.

Current Capabilities:

- CPU, RAM, and disk monitoring
- Host and platform visibility
- Docker container status and health detection
- Jenkins API integration
- Jenkins job and build status visibility
- Failed Jenkins build detection

Technology:

- psutil
- Docker SDK
- Jenkins API

---

## 2. Jenkins Monitoring

Jenkins monitoring adds CI/CD observability to OpsPilot AI.

Responsibilities:

- Check Jenkins connectivity
- List Jenkins jobs
- Read build details from Jenkins job APIs
- Detect failed builds
- Expose Jenkins summary metrics
- Feed failed build events into the alert engine

Failed build alerts include job name, build number, build URL, result, and duration.

---

## 3. Alert Engine

Rule-based detection layer for infrastructure, container, and Jenkins issues.

Current Responsibilities:

- CPU threshold alerts
- RAM threshold alerts
- Disk threshold alerts
- Container stopped alerts
- Container unhealthy alerts
- Jenkins failed build alerts
- Severity classification
- Runtime cooldown protection
- Structured alert generation

---

## 4. SQLite Alert Storage

Persistent alert history layer backed by SQLite and SQLAlchemy.

Stores:

- Alert issue
- Alert severity
- Alert source
- Alert details
- Alert timestamp

This supports operational review, alert APIs, and restart-safe Jenkins duplicate alert protection.

---

## 5. Alert APIs

FastAPI endpoints expose alert history and monitoring status for operational review.

Current Capabilities:

- List persisted alerts
- Retrieve recent alerts
- Retrieve alerts by ID
- Filter by severity and source
- Limit result size
- Return alert summary counts
- Expose Jenkins health, jobs, failures, and summary data

---

## 6. Background Worker

Runs continuous monitoring and alert evaluation.

Responsibilities:

- Periodic metric collection
- Alert detection
- Cooldown enforcement
- Alert persistence
- Restart-safe Jenkins deduplication
- Telegram alert delivery
- Graceful shutdown on user interrupt

---

## 7. Telegram Notification

Operational notification layer for real-time alert delivery.

Responsibilities:

- Send infrastructure alerts
- Send Docker alerts
- Send Jenkins failed build alerts
- Support monitoring commands
- Provide future conversational DevOps access

---

# Data Flow

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
       ↓
DevOps Engineer
```

---

# Future AI-Assisted Flow

```text
Alert / Incident / Log / Failed Build
        ↓
AI Diagnosis Engine
        ↓
Root Cause Analysis
        ↓
Safe Recommendations
        ↓
Telegram Response
```

---

# Planned Scalable Architecture

## Multi-Server Agents

- Lightweight monitoring agents
- Central coordination service
- Scalable infrastructure monitoring

## Event Queue

- Alert processing
- AI analysis jobs
- Background tasks

Potential technologies:

- Redis Queue
- RabbitMQ
- Kafka

## Production Database

SQLite is suitable for the MVP. PostgreSQL remains the planned production migration path for multi-server scale, advanced querying, and reporting.

## Cloud and Kubernetes

Future integrations include Kubernetes, AWS monitoring, Prometheus, Grafana, and cloud-level observability.

---

# Engineering Principles

- MVP-first development
- Persistent monitoring before automation
- Stable alerting before AI diagnosis
- Cooldown protection for alert quality
- Restart-safe deduplication for repeated CI/CD failures
- Clean modular architecture
- Scalable design without premature overengineering

---

# Architecture Evolution Path

Monitoring -> Alerting -> Persistence -> CI/CD Observability -> Visibility -> AI Diagnosis -> AI Logs -> Conversational DevOps -> Intelligent Operations Platform