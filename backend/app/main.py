from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.metrics import router as metrics_router
from app.api import docker_metrics

app = FastAPI(
    title="OpsPilot AI",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(metrics_router)
app.include_router(docker_metrics.router)


@app.get("/")
def root():
    return {
        "message": "OpsPilot AI Backend Running"
    }