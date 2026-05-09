from fastapi import APIRouter

from app.services.system_metrics import get_system_metrics

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)


@router.get("/system")
def system_metrics():
    return get_system_metrics()