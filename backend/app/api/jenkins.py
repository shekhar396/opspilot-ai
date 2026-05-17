from fastapi import APIRouter, HTTPException

from app.schemas.jenkins_build import (
    JenkinsBuildResponse,
    JenkinsSummaryResponse,
)
from app.schemas.jenkins import JenkinsHealthResponse, JenkinsJobResponse
from app.services.jenkins_service import (
    JenkinsConfigurationError,
    JenkinsJobNotFoundError,
    JenkinsRequestError,
    check_jenkins_connection,
    get_failed_jobs,
    get_job_details,
    get_jenkins_jobs,
    get_jenkins_summary,
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


@router.get("/jobs/{job_name}", response_model=JenkinsBuildResponse)
def jenkins_job_details(job_name: str):
    try:
        return get_job_details(job_name)
    except JenkinsConfigurationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except JenkinsJobNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except JenkinsRequestError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/failed", response_model=list[JenkinsBuildResponse])
def jenkins_failed_jobs():
    try:
        return get_failed_jobs()
    except JenkinsConfigurationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except JenkinsJobNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except JenkinsRequestError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/summary", response_model=JenkinsSummaryResponse)
def jenkins_summary():
    try:
        return get_jenkins_summary()
    except JenkinsConfigurationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except JenkinsJobNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except JenkinsRequestError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
