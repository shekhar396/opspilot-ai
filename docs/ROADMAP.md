# OpsPilot AI Roadmap

---

# Project Direction

OpsPilot AI is being developed as an AI-assisted DevOps operations platform focused on infrastructure visibility, intelligent diagnostics, and conversational operational assistance.

The MVP prioritizes:
- practical operational usefulness
- clean architecture
- AI-assisted troubleshooting
- scalable engineering practices

---

# MVP Development Strategy

The project follows an incremental MVP-first approach.

Priority order:

1. Monitoring Foundation
2. Operational Visibility
3. AI Diagnosis
4. AI Log Analysis
5. CI/CD Awareness
6. Conversational DevOps Assistant

---

# Phase 1 — Monitoring Foundation ✅

## Goals
Build a stable infrastructure monitoring foundation.

## Features
- Linux monitoring
- CPU monitoring
- RAM monitoring
- Disk monitoring
- Docker container monitoring
- Container restart tracking
- Telegram integration

## Technical Goals
- FastAPI backend
- Modular architecture
- Dockerized runtime
- Clean service structure

Release:
v0.3.0

---

# Phase 2 — Operational Visibility

## Goals
Enable proactive operational monitoring and alerting.

## Features
- CPU threshold alerts
- RAM threshold alerts
- Disk alerts
- Container down alerts
- Restart spike alerts
- Alert severity levels
- Telegram notifications

## Additional Features
- Alert history storage
- Alert log APIs
- Historical tracking

Release:
v0.4.0

---

# Phase 3 — AI Diagnosis Layer

## Goals
Introduce AI-assisted operational diagnostics.

## Features
- AI alert diagnosis
- Root cause suggestions
- Incident summaries
- Suggested troubleshooting commands
- AI operational insights

## Example
```text
Container restarting repeatedly due to memory exhaustion.
```

Release:
v0.5.0

---

# Phase 4 — AI Log Analysis

## Goals
Enable intelligent infrastructure log analysis.

## Features
- Docker log analysis
- Linux service log analysis
- Error summarization
- Suggested fixes
- Incident reporting

Release:
v0.6.0

---

# Phase 5 — CI/CD Visibility

## Goals
Introduce deployment and pipeline awareness.

## Features
- Jenkins monitoring
- Failed build alerts
- Deployment visibility
- Build diagnostics
- Pipeline summaries

Release:
v0.7.0

---

# Phase 6 — Conversational AI Operations

## Goals
Enable Hermes-style DevOps assistant behavior.

## Features
- Natural language troubleshooting
- Conversational operations
- Infrastructure-aware responses
- AI operational assistant

## Example Queries
```text
Why is nginx down?
Show unhealthy containers
Why did deployment fail?
```

Release:
v1.0.0

---

# Deferred Features (Post-MVP)

These are intentionally postponed to avoid MVP scope explosion.

## Future Features
- Kubernetes monitoring
- AWS integrations
- Terraform awareness
- Prometheus integration
- Grafana integration
- Multi-server agents
- Predictive analytics
- Autonomous remediation
- Self-healing infrastructure

---

# Long-Term Vision

OpsPilot AI aims to evolve into:
- AI-assisted operations platform
- Infrastructure intelligence engine
- AIOps platform
- Conversational DevOps copilot