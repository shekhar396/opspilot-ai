from pydantic import BaseModel


class JenkinsBuildResponse(BaseModel):
    name: str
    last_build_number: int | None = None
    build_status: str | None = None
    build_url: str | None = None
    building: bool = False
    timestamp: int | None = None
    duration: int | None = None


class JenkinsSummaryResponse(BaseModel):
    total_jobs: int
    failed_jobs: int
    successful_jobs: int
    running_jobs: int
