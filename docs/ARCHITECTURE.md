# Architecture Overview

## Core Components

### Telegram Bot
User interaction layer.

### FastAPI Backend
Main API and orchestration service.

### Monitoring Agents
Collect metrics from Linux servers.

### AI Analysis Engine
Analyzes logs and incidents using LLM APIs.

### Storage Layer
SQLite for MVP.

## Initial Flow

```text
Server Agent
    ↓
FastAPI Backend
    ↓
AI Analyzer
    ↓
Telegram Alerts

# Future Architecture

## Planned Improvements

### Multi-Agent System
Dedicated monitoring agents deployed on multiple servers.

### Event Queue
Asynchronous event processing for alerts and monitoring tasks.

Possible technologies:
- Redis Queue
- RabbitMQ
- Kafka (future scale)

### Redis Caching
Temporary storage for metrics, alerts, and AI responses.

### PostgreSQL Migration
Transition from SQLite to PostgreSQL for production readiness.

### Kubernetes Deployment
Container orchestration for scalable deployment.

Future goals:
- Helm charts
- Horizontal scaling
- Self-healing services
- Multi-environment deployment

### Cloud Integrations
Planned integrations:
- AWS CloudWatch
- EC2 monitoring
- Docker Swarm
- Grafana
- Prometheus