from pydantic import BaseModel


class JenkinsHealthResponse(BaseModel):
    status: str
    jenkins_url: str
    mode: str | None = None
    node_name: str | None = None


class JenkinsJobResponse(BaseModel):
    name: str
    url: str
    color: str | None = None
