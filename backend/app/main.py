from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.alerts import router as alerts_router
from app.api.health import router as health_router
from app.api.metrics import router as metrics_router
from app.api import docker_metrics
from app.db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="OpsPilot AI",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(metrics_router)
app.include_router(docker_metrics.router)
app.include_router(alerts_router)


@app.get("/")
def root():
    return {
        "message": "OpsPilot AI Backend Running"
    }
