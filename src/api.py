import requests

BASE_URL = "https://api.github.com/users"
TIMEOUT = 10


def _make_request(url: str) -> dict | list:
    """
    Perform a GET request to the GitHub REST API.

    Args:
        url: API endpoint.

    Returns:
        Parsed JSON response.

    Raises:
        ValueError: If the requested resource does not exist.
        RuntimeError: If the API returns an unexpected error.
    """

    response = requests.get(url, timeout=TIMEOUT)

    if response.status_code == 200:
        return response.json()

    if response.status_code == 404:
        raise ValueError("Resource not found.")

    raise RuntimeError(
        f"GitHub API returned status code {response.status_code}."
    )


def get_user(username: str) -> dict:
    """
    Retrieve information about a GitHub user.

    Args:
        username: GitHub username.

    Returns:
        Dictionary containing user information.
    """

    url = f"{BASE_URL}/{username}"

    return _make_request(url)


def get_repositories(username: str) -> list[dict]:
    """
    Retrieve all public repositories of a GitHub user.

    Args:
        username: GitHub username.

    Returns:
        List of repositories.
    """

    url = f"{BASE_URL}/{username}/repos"

    return _make_request(url)