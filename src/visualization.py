from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_DIR = Path("output/figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def _save_plot(filename: str) -> None:
    """
    Save the current matplotlib figure.
    """
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()


def plot_top_starred_repositories(
    df: pd.DataFrame,
    top_n: int = 10,
) -> None:
    """
    Plot repositories with the highest number of stars.
    """

    top = (
        df.sort_values("stars", ascending=False)
        .head(top_n)
    )

    plt.figure(figsize=(10, 6))

    plt.barh(top["name"], top["stars"])

    plt.title("Top Starred Repositories")
    plt.xlabel("Stars")

    plt.gca().invert_yaxis()

    _save_plot("top_starred_repositories.png")


def plot_top_forked_repositories(
    df: pd.DataFrame,
    top_n: int = 10,
) -> None:

    top = (
        df.sort_values("forks", ascending=False)
        .head(top_n)
    )

    plt.figure(figsize=(10, 6))

    plt.barh(top["name"], top["forks"])

    plt.title("Top Forked Repositories")
    plt.xlabel("Forks")

    plt.gca().invert_yaxis()

    _save_plot("top_forked_repositories.png")


def plot_repositories_by_language(
    df: pd.DataFrame,
) -> None:

    languages = (
        df["language"]
        .fillna("Unknown")
        .value_counts()
    )

    plt.figure(figsize=(8, 6))

    plt.bar(
        languages.index,
        languages.values,
    )

    plt.title("Repositories by Language")
    plt.ylabel("Repositories")

    plt.xticks(rotation=45)

    _save_plot("repositories_by_language.png")


def plot_stars_by_language(
    df: pd.DataFrame,
) -> None:

    stars = (
        df.groupby("language")["stars"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 6))

    plt.bar(
        stars.index.astype(str),
        stars.values,
    )

    plt.title("Stars by Language")
    plt.ylabel("Stars")

    plt.xticks(rotation=45)

    _save_plot("stars_by_language.png")


def plot_forks_by_language(
    df: pd.DataFrame,
) -> None:

    forks = (
        df.groupby("language")["forks"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 6))

    plt.bar(
        forks.index.astype(str),
        forks.values,
    )

    plt.title("Forks by Language")
    plt.ylabel("Forks")

    plt.xticks(rotation=45)

    _save_plot("forks_by_language.png")


def plot_repository_sizes(
    df: pd.DataFrame,
    top_n: int = 10,
) -> None:

    top = (
        df.sort_values("size_kb", ascending=False)
        .head(top_n)
    )

    plt.figure(figsize=(10, 6))

    plt.barh(
        top["name"],
        top["size_kb"],
    )

    plt.title("Largest Repositories")
    plt.xlabel("Size (KB)")

    plt.gca().invert_yaxis()

    _save_plot("largest_repositories.png")


def plot_repositories_per_year(
    df: pd.DataFrame,
) -> None:

    repositories = (
        df["created_at"]
        .dt.year
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(8, 5))

    plt.plot(
        repositories.index,
        repositories.values,
        marker="o",
    )

    plt.title("Repositories Created per Year")
    plt.xlabel("Year")
    plt.ylabel("Repositories")

    plt.grid(True)

    _save_plot("repositories_per_year.png")


def plot_watchers_distribution(
    df: pd.DataFrame,
) -> None:

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["watchers"],
        bins=10,
    )

    plt.title("Watchers Distribution")
    plt.xlabel("Watchers")
    plt.ylabel("Repositories")

    _save_plot("watchers_distribution.png")


def generate_all_figures(
    df: pd.DataFrame,
) -> None:
    """
    Generate every figure.
    """

    plot_top_starred_repositories(df)
    plot_top_forked_repositories(df)
    plot_repositories_by_language(df)
    plot_stars_by_language(df)
    plot_forks_by_language(df)
    plot_repository_sizes(df)
    plot_repositories_per_year(df)
    plot_watchers_distribution(df)