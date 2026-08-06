from pathlib import Path
import json

import pandas as pd

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def print_report(report: dict) -> None:
    """
    Print the analysis report.
    """

    print("\n" + "=" * 60)
    print("GITHUB USER ANALYSIS REPORT")
    print("=" * 60)

    print("\nUser Information")
    print("-" * 60)
    print(f"Username              : {report['username']}")
    print(f"Name                  : {report['name']}")
    print(f"Followers             : {report['followers']}")
    print(f"Following             : {report['following']}")
    print(f"Public repositories   : {report['public_repositories']}")

    print("\nRepository Statistics")
    print("-" * 60)
    print(f"Total repositories    : {report['total_repositories']}")
    print(f"Total stars           : {report['total_stars']}")
    print(f"Total forks           : {report['total_forks']}")
    print(f"Average stars/repo    : {report['average_stars']:.2f}")
    print(f"Most used language    : {report['most_used_language']}")
    print(
        f"Most starred repo     : "
        f"{report['most_starred_repository']} "
        f"({report['most_starred_repository_stars']} ⭐)"
    )


def save_report_json(
    report: dict,
    filename: str = "report.json",
) -> None:
    """
    Save report as JSON.
    """

    path = OUTPUT_DIR / filename

    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False,
        )


def save_repositories_csv(
    df: pd.DataFrame,
    filename: str = "repositories.csv",
) -> None:
    """
    Save repository DataFrame as CSV.
    """

    path = OUTPUT_DIR / filename

    df.to_csv(
        path,
        index=False,
    )


def export_all(
    report: dict,
    df: pd.DataFrame,
) -> None:
    """
    Export every output file.
    """

    save_report_json(report)

    save_repositories_csv(df)


def print_generated_files() -> None:
    """
    Print generated files.
    """

    print("\nFiles generated")
    print("-" * 60)
    print("output/report.json")
    print("output/repositories.csv")
    print("output/figures/")