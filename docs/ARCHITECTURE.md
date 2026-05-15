# OpsPilot AI Architecture

## Architecture Status

OpsPilot AI is in active MVP development with:

- Linux and Docker monitoring
- Rule-based alerting
- SQLite alert persistence
- Alert history APIs
- Telegram notifications
- GitHub Actions CI

Current Release: v0.3.0

---

# Current Architecture

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

Cooldown protection runs during alert evaluation to reduce duplicate notifications while preserving persistent alert history for review.

---

# Core Components

## 1. Monitoring Services

Collect operational metrics from the host system and Docker runtime.

Current Capabilities:

- CPU, RAM, and disk monitoring
- Host and platform visibility
- Docker container status
- Container restart tracking
- Container health detection

Technology:

- psutil
- Docker SDK

---

## 2. Alert Engine

Rule-based detection layer for infrastructure and container issues.

Current Responsibilities:

- CPU threshold alerts
- RAM threshold alerts
- Disk threshold alerts
- Container stopped alerts
- Container unhealthy alerts
- Restart loop detection
- Severity classification
- Cooldown protection
- Structured alert generation

---

## 3. SQLite Alert Storage

Persistent alert history layer backed by SQLite and SQLAlchemy.

Stores:

- Alert issue
- Alert severity
- Alert source
- Alert details
- Alert timestamp

This creates persistent monitoring visibility across worker runs without changing the lightweight MVP footprint.

---

## 4. Alert APIs

FastAPI endpoints expose alert history for operational review.

Current Capabilities:

- List persisted alerts
- Retrieve recent alerts
- Retrieve alerts by ID
- Filter by severity and source
- Limit result size
- Return alert summary counts

---

## 5. Background Worker

Runs continuous monitoring and alert evaluation.

Responsibilities:

- Periodic metric collection
- Alert detection
- Cooldown enforcement
- Alert persistence
- Telegram alert delivery

---

## 6. Telegram Notification

Operational notification layer for real-time alert delivery.

Responsibilities:

- Send infrastructure alerts
- Send Docker alerts
- Support monitoring commands
- Provide future conversational DevOps access

---

# Data Flow

```text
Linux Host / Docker Runtime
        ↓
Monitoring Services
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
Alert / Incident / Log
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
- Clean modular architecture
- Scalable design without premature overengineering

---

# Architecture Evolution Path

Monitoring -> Alerting -> Persistence -> Visibility -> AI Diagnosis -> AI Logs -> CI/CD Awareness -> Conversational DevOps -> Intelligent Operations Platform
