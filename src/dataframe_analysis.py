import pandas as pd


def repositories_by_language(df: pd.DataFrame) -> pd.Series:
    """
    Count repositories by programming language.
    """
    return (
        df["language"]
        .fillna("Unknown")
        .value_counts()
    )


def stars_by_language(df: pd.DataFrame) -> pd.Series:
    """
    Calculate the total number of stars for each language.
    """
    return (
        df.groupby("language")["stars"]
        .sum()
        .sort_values(ascending=False)
    )


def forks_by_language(df: pd.DataFrame) -> pd.Series:
    """
    Calculate the total number of forks for each language.
    """
    return (
        df.groupby("language")["forks"]
        .sum()
        .sort_values(ascending=False)
    )


def top_starred_repositories(
    df: pd.DataFrame,
    n: int = 5,
) -> pd.DataFrame:
    """
    Return the repositories with the most stars.
    """
    return (
        df.sort_values(
            by="stars",
            ascending=False,
        )
        .head(n)
    )


def top_forked_repositories(
    df: pd.DataFrame,
    n: int = 5,
) -> pd.DataFrame:
    """
    Return the repositories with the most forks.
    """
    return (
        df.sort_values(
            by="forks",
            ascending=False,
        )
        .head(n)
    )


def largest_repositories(
    df: pd.DataFrame,
    n: int = 5,
) -> pd.DataFrame:
    """
    Return the largest repositories by size.
    """
    return (
        df.sort_values(
            by="size_kb",
            ascending=False,
        )
        .head(n)
    )


def repositories_per_year(df: pd.DataFrame) -> pd.Series:
    """
    Count repositories created each year.
    """
    return (
        df["created_at"]
        .dt.year
        .value_counts()
        .sort_index()
    )


def updated_per_year(df: pd.DataFrame) -> pd.Series:
    """
    Count repositories updated each year.
    """
    return (
        df["updated_at"]
        .dt.year
        .value_counts()
        .sort_index()
    )


def dataframe_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return descriptive statistics.
    """
    return df[
        [
            "stars",
            "forks",
            "watchers",
            "size_kb",
            "open_issues",
        ]
    ].describe()


def language_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return aggregated statistics for each language.
    """
    return (
        df.groupby("language")
        .agg(
            repositories=("name", "count"),
            total_stars=("stars", "sum"),
            average_stars=("stars", "mean"),
            total_forks=("forks", "sum"),
            average_size=("size_kb", "mean"),
        )
        .sort_values(
            by="total_stars",
            ascending=False,
        )
    )