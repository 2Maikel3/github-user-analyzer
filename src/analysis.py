def get_total_stars(repositories: list[dict]) -> int:
    """
    Calculate the total number of stars across all repositories.

    Args:
        repositories: List of GitHub repositories.

    Returns:
        Total number of stars.
    """
    return sum(repo["stargazers_count"] for repo in repositories)

def get_most_starred_repository(repositories: list[dict]) -> dict:
    """
    Find the repository with the highest number of stars.

    Args:
        repositories: List of GitHub repositories.

    Returns:
        The repository with the highest number of stars.

    Raises:
        ValueError: If the repository list is empty.
    """
    if not repositories:
        raise ValueError("Repository list is empty.")
    
    return max(repositories, key=lambda repo: repo["stargazers_count"])