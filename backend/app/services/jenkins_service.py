import requests

from app.core.config import settings


class JenkinsConfigurationError(Exception):
    pass


class JenkinsRequestError(Exception):
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


def _get_jenkins_api(params: dict | None = None) -> dict:
    url = f"{_get_jenkins_base_url()}/api/json"

    try:
        response = requests.get(
            url,
            params=params,
            auth=_get_auth(),
            timeout=settings.jenkins_timeout_seconds,
        )
        response.raise_for_status()
        return response.json()

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
