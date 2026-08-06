import sys

from api import get_repositories, get_user
from analysis import generate_report
from output import (
    export_all,
    print_generated_files,
    print_report,
)
from transform import repositories_to_dataframe
from visualization import generate_all_figures


def main() -> None:
    """
    Main entry point.
    """

    if len(sys.argv) != 2:
        print("Usage:")
        print("python src/main.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]

    try:

        print("Fetching GitHub data...")

        user = get_user(username)

        repositories = get_repositories(username)

        print("Transforming data...")

        dataframe = repositories_to_dataframe(repositories)

        print("Analyzing repositories...")

        report = generate_report(
            user,
            repositories,
        )

        print("Generating figures...")

        generate_all_figures(dataframe)

        print("Exporting files...")

        export_all(
            report,
            dataframe,
        )

        print_report(report)

        print_generated_files()

        print("\nAnalysis completed successfully!")

    except ValueError as error:

        print(f"\nError: {error}")

    except RuntimeError as error:

        print(f"\nAPI Error: {error}")

    except KeyboardInterrupt:

        print("\nExecution cancelled.")

    except Exception as error:

        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()