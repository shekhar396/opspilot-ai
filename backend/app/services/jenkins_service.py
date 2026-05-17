from urllib.parse import quote

import requests

from app.core.config import settings


class JenkinsConfigurationError(Exception):
    pass


class JenkinsRequestError(Exception):
    pass


class JenkinsJobNotFoundError(Exception):
    pass


def _get_jenkins_base_url() -> str:
    if not settings.jenkins_url:
        raise JenkinsConfigurationError(
            "JENKINS_URL is not configured."
        )

    return settings.jenkins_url.rstrip("/")


def _get_auth() -> tuple[str, str] | None:
    if settings.jenkins_username and settings.jenkins_api_token:
        return settings.jenkins_username, settings.jenkins_api_token

    return None


def _get_jenkins_api(path: str = "", params: dict | None = None) -> dict:
    url = f"{_get_jenkins_base_url()}{path}/api/json"

    try:
        response = requests.get(
            url,
            params=params,
            auth=_get_auth(),
            timeout=settings.jenkins_timeout_seconds,
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            raise JenkinsJobNotFoundError("Jenkins job does not exist.") from exc

        raise JenkinsRequestError(
            f"Jenkins request failed: {exc}"
        ) from exc

    except requests.exceptions.RequestException as exc:
        raise JenkinsRequestError(
            f"Jenkins request failed: {exc}"
        ) from exc

    except ValueError as exc:
        raise JenkinsRequestError(
            "Jenkins returned an invalid JSON response."
        ) from exc


def check_jenkins_connection() -> dict:
    data = _get_jenkins_api()

    return {
        "status": "connected",
        "jenkins_url": _get_jenkins_base_url(),
        "mode": data.get("mode"),
        "node_name": data.get("nodeName"),
    }


def get_jenkins_jobs() -> list[dict]:
    data = _get_jenkins_api(
        params={"tree": "jobs[name,url,color]"}
    )

    return data.get("jobs", [])


def get_job_details(job_name: str) -> dict:
    encoded_job_name = quote(job_name, safe="")
    data = _get_jenkins_api(
        path=f"/job/{encoded_job_name}",
        params={
            "tree": (
                "name,lastBuild[number,url,building,result,timestamp,duration]"
            )
        },
    )
    last_build = data.get("lastBuild") or {}

    return {
        "name": data.get("name", job_name),
        "last_build_number": last_build.get("number"),
        "build_status": _get_build_status(last_build),
        "build_url": last_build.get("url"),
        "building": bool(last_build.get("building", False)),
        "timestamp": last_build.get("timestamp"),
        "duration": last_build.get("duration"),
    }


def get_failed_jobs() -> list[dict]:
    failed_jobs = []

    for job in get_jenkins_jobs():
        job_details = get_job_details(job["name"])
        if job_details["build_status"] == "FAILURE":
            failed_jobs.append(job_details)

    return failed_jobs


def get_jenkins_summary() -> dict:
    job_details = [
        get_job_details(job["name"])
        for job in get_jenkins_jobs()
    ]

    return {
        "total_jobs": len(job_details),
        "failed_jobs": sum(
            job["build_status"] == "FAILURE"
            for job in job_details
        ),
        "successful_jobs": sum(
            job["build_status"] == "SUCCESS"
            for job in job_details
        ),
        "running_jobs": sum(
            job["building"]
            for job in job_details
        ),
    }


def _get_build_status(last_build: dict) -> str | None:
    if last_build.get("building"):
        return "RUNNING"

    return last_build.get("result")
