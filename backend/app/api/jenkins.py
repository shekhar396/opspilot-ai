from fastapi import APIRouter, HTTPException

from app.schemas.jenkins import JenkinsHealthResponse, JenkinsJobResponse
from app.services.jenkins_service import (
    JenkinsConfigurationError,
    JenkinsRequestError,
    check_jenkins_connection,
    get_jenkins_jobs,
)


router = APIRouter(
    prefix="/jenkins",
    tags=["Jenkins"],
)


@router.get("/health", response_model=JenkinsHealthResponse)
def jenkins_health():
    try:
        return check_jenkins_connection()
    except JenkinsConfigurationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except JenkinsRequestError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/jobs", response_model=list[JenkinsJobResponse])
def jenkins_jobs():
    try:
        return get_jenkins_jobs()
    except JenkinsConfigurationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except JenkinsRequestError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
