# OpsPilot AI Architecture

## Architecture Status

OpsPilot AI is currently in MVP stage with:

- Monitoring foundation completed
- Alerting engine implemented
- Telegram integration active
- CI pipeline enabled

The architecture is intentionally modular to support future AI-driven expansion.

Current Release: v0.2.0

---

# Current Production-Ready Architecture (MVP)

```text
Telegram User
      ↓
Telegram Bot
      ↓
FastAPI Backend
      ↓
Monitoring Services
      ↓
Alert Engine
      ↓
Background Worker
      ↓
Telegram Notification
````

---

# Core Components

## 1. Telegram Bot

User interaction and notification layer.

Responsibilities:

* Receive user commands
* Send system status responses
* Deliver alerts
* Support future conversational DevOps features

---

## 2. FastAPI Backend

Main orchestration service.

Responsibilities:

* Expose REST APIs
* Coordinate monitoring modules
* Trigger alert evaluations
* Manage system configuration
* Provide health endpoints
* Serve future AI integration layer

---

## 3. Monitoring Services

Collect operational metrics from host system and Docker runtime.

Current Capabilities:

* CPU usage monitoring
* RAM usage monitoring
* Disk usage monitoring
* Docker container status
* Container restart tracking
* Container health detection

Technology:

* psutil
* Docker SDK

---

## 4. Alert Engine (Implemented in v0.2.0)

Rule-based detection system.

Current Responsibilities:

* CPU threshold alerts
* RAM threshold alerts
* Disk threshold alerts
* Container stopped alerts
* Container unhealthy alerts
* Restart loop detection
* Alert cooldown protection
* Structured alert generation

Alert Evaluation Frequency:

* Periodic background loop (configurable interval)

---

## 5. Background Worker

Continuously runs alert evaluation.

Responsibilities:

* Periodic monitoring checks
* Alert detection
* Telegram alert delivery
* Cooldown enforcement
* Prevent duplicate spam alerts

This is the operational core of v0.2.0.

---

## 6. Storage Layer

### Current (MVP)

* SQLite

Stores:

* Alert history
* Alert timestamps
* Alert severity
* Monitoring records

### Future

* PostgreSQL (production migration)

---

# Current Data Flow

```text
Linux Host / Docker Runtime
        ↓
Monitoring Services
        ↓
Alert Engine
        ↓
Background Worker
        ↓
Telegram Bot
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

# Planned Scalable Architecture (Post-MVP)

## 1. Multi-Server Agent System

* Lightweight monitoring agents
* Installed on multiple servers
* Centralized coordination
* Scalable infrastructure monitoring

---

## 2. Event Queue System

For asynchronous processing.

Possible technologies:

* Redis Queue
* RabbitMQ
* Kafka (future scale)

Use cases:

* Alert processing
* AI analysis jobs
* Background tasks

---

## 3. Redis Layer

For:

* Alert cooldown tracking
* Short-term caching
* Rate limiting
* AI response caching

---

## 4. PostgreSQL Migration

Production database upgrade.

Benefits:

* Reliable long-term storage
* Multi-server scalability
* Advanced querying
* Reporting support

---

## 5. Kubernetes Deployment

Future container orchestration.

Goals:

* Horizontal scaling
* Helm-based deployment
* Multi-environment support
* Production-grade deployment strategy

---

## 6. Cloud Integrations

Future integrations:

* AWS monitoring
* CloudWatch
* Prometheus
* Grafana dashboards
* Infrastructure-level observability

---

# Engineering Principles

* MVP-first development
* Incremental complexity
* Stable monitoring before automation
* Safe recommendations before self-healing
* Clean modular architecture
* Scalable design without premature overengineering
* AI features added progressively

---

# Architecture Evolution Path

Monitoring → Alerting → Visibility → AI Diagnosis → AI Logs → CI/CD Awareness → Conversational DevOps → Intelligent Operations Platform

