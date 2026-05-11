# OpsPilot AI Architecture

## Architecture Status

Current architecture is designed for MVP-stage development with a clean path toward a scalable AI-assisted DevOps operations platform.

---

## Current MVP Architecture

```text
Telegram User
      ↓
Telegram Bot
      ↓
FastAPI Backend
      ↓
Monitoring Services
      ↓
Alerting Engine
      ↓
AI Diagnosis Engine
      ↓
Telegram Response / Alert
````

---

## Core Components

### Telegram Bot

User interaction and notification layer.

Responsibilities:

* Receive commands
* Send monitoring responses
* Send alert notifications
* Support future conversational DevOps queries

---

### FastAPI Backend

Main API and orchestration service.

Responsibilities:

* Expose monitoring APIs
* Coordinate monitoring services
* Process Telegram requests
* Trigger alert checks
* Connect with AI diagnosis layer

---

### Monitoring Services

Collect operational data from the host system and Docker runtime.

Current responsibilities:

* Linux CPU monitoring
* RAM monitoring
* Disk monitoring
* Docker container status
* Docker restart tracking
* Docker health visibility

---

### Alerting Engine

Detects abnormal infrastructure conditions.

Planned responsibilities:

* CPU threshold alerts
* RAM threshold alerts
* Disk threshold alerts
* Container down alerts
* Restart spike alerts
* Severity classification

---

### AI Diagnosis Engine

Analyzes alerts, logs, and incidents using LLM APIs.

Planned responsibilities:

* Explain detected issues
* Suggest possible root causes
* Recommend safe troubleshooting commands
* Generate incident summaries
* Analyze logs

---

### Storage Layer

Stores alert history and operational records.

MVP:

* SQLite

Future:

* PostgreSQL

Planned data:

* Alert history
* Alert severity
* Alert status
* Monitoring events
* AI diagnosis results

---

## Current Data Flow

```text
Linux / Docker Host
      ↓
Monitoring Services
      ↓
FastAPI Backend
      ↓
Alerting Engine
      ↓
Telegram Bot
      ↓
DevOps Engineer
```

---

## Future AI-Assisted Flow

```text
Alert / Log / Incident
      ↓
AI Diagnosis Engine
      ↓
Root Cause Suggestion
      ↓
Recommended Commands
      ↓
Telegram Response
```

---

## Future Architecture

These features are planned after the MVP foundation is stable.

### Multi-Agent System

Dedicated monitoring agents deployed on multiple servers.

Purpose:

* Monitor multiple Linux servers
* Register agents centrally
* Send metrics to central backend

---

### Event Queue

Asynchronous event processing for alerts and monitoring tasks.

Possible technologies:

* Redis Queue
* RabbitMQ
* Kafka for future scale

---

### Redis Caching

Temporary storage for:

* Recent metrics
* Alert cooldowns
* AI response cache
* Short-lived operational state

---

### PostgreSQL Migration

Transition from SQLite to PostgreSQL for production readiness.

Purpose:

* Better historical data storage
* Better reporting
* Multi-server support
* Production-grade persistence

---

### Kubernetes Deployment

Container orchestration for scalable deployment.

Future goals:

* Helm charts
* Horizontal scaling
* Multi-environment deployment
* Production deployment strategy

---

### Cloud Integrations

Planned integrations:

* AWS CloudWatch
* EC2 monitoring
* Grafana
* Prometheus

---

## Engineering Principles

* MVP-first development
* Keep current architecture simple
* Avoid premature overengineering
* Build stable monitoring before automation
* Add AI features incrementally
* Prefer safe recommendations before auto-remediation

