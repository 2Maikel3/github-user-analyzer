from collections import Counter


def get_total_stars(repositories: list[dict]) -> int:
    """
    Calculate the total number of stars across all repositories.
    """
    return sum(repo["stargazers_count"] for repo in repositories)


def get_total_forks(repositories: list[dict]) -> int:
    """
    Calculate the total number of forks across all repositories.
    """
    return sum(repo["forks_count"] for repo in repositories)


def get_average_stars(repositories: list[dict]) -> float:
    """
    Calculate the average number of stars per repository.
    """
    if not repositories:
        return 0.0

    return get_total_stars(repositories) / len(repositories)


def get_most_starred_repository(repositories: list[dict]) -> dict:
    """
    Return the repository with the highest number of stars.
    """
    if not repositories:
        raise ValueError("Repository list is empty.")

    return max(
        repositories,
        key=lambda repo: repo["stargazers_count"],
    )


def get_most_used_language(repositories: list[dict]) -> str:
    """
    Return the most frequently used programming language.
    """
    languages = [
        repo["language"]
        for repo in repositories
        if repo["language"] is not None
    ]

    if not languages:
        return "Unknown"

    return Counter(languages).most_common(1)[0][0]


def generate_report(
    user: dict,
    repositories: list[dict],
) -> dict:
    """
    Generate a summary report.
    """

    if repositories:
        most_starred = get_most_starred_repository(repositories)

        most_starred_name = most_starred["name"]
        most_starred_stars = most_starred["stargazers_count"]

    else:
        most_starred_name = "None"
        most_starred_stars = 0

    return {
        "username": user["login"],
        "name": user["name"] or "Not specified",
        "followers": user["followers"],
        "following": user["following"],
        "public_repositories": user["public_repos"],
        "total_repositories": len(repositories),
        "total_stars": get_total_stars(repositories),
        "total_forks": get_total_forks(repositories),
        "average_stars": round(
            get_average_stars(repositories),
            2,
        ),
        "most_used_language": get_most_used_language(
            repositories
        ),
        "most_starred_repository": most_starred_name,
        "most_starred_repository_stars": most_starred_stars,
    }