from fastapi import APIRouter, HTTPException
from app.services.docker_metrics import get_docker_metrics

router = APIRouter(prefix="/metrics", tags=["Docker Metrics"])


@router.get("/docker")
def docker_metrics():
    try:
        return get_docker_metrics()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to collect Docker metrics: {str(e)}"
        )