import pandas as pd


def repositories_to_dataframe(repositories: list[dict]) -> pd.DataFrame:
    """
    Convert GitHub repositories into a clean pandas DataFrame.

    Args:
        repositories: List of GitHub repositories.

    Returns:
        A pandas DataFrame containing the most relevant repository information.
    """

    data = []

    for repo in repositories:
        data.append(
            {
                "name": repo["name"],
                "description": repo["description"],
                "language": repo["language"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "watchers": repo["watchers_count"],
                "open_issues": repo["open_issues_count"],
                "size_kb": repo["size"],
                "default_branch": repo["default_branch"],
                "visibility": repo["visibility"],
                "archived": repo["archived"],
                "fork": repo["fork"],
                "created_at": repo["created_at"],
                "updated_at": repo["updated_at"],
                "pushed_at": repo["pushed_at"],
                "html_url": repo["html_url"],
            }
        )

    dataframe = pd.DataFrame(data)

    if dataframe.empty:
        return dataframe

    dataframe["created_at"] = pd.to_datetime(dataframe["created_at"])
    dataframe["updated_at"] = pd.to_datetime(dataframe["updated_at"])
    dataframe["pushed_at"] = pd.to_datetime(dataframe["pushed_at"])

    dataframe["language"] = dataframe["language"].fillna("Unknown")

    return dataframe