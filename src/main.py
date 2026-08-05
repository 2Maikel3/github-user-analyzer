import sys
from api import get_user, get_repositories
from analysis import get_total_stars, get_most_starred_repository

def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python src/main.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]

    user = get_user(username)

    print("GitHub User Information")
    print("-----------------------")
    print("Username        :", user["login"] or "Not specified")
    print("Name            :", user["name"] or "Not specified")
    print("Public Repos    :", user["public_repos"])
    print("Followers       :", user["followers"])
    print("Following       :", user["following"])

    repositories = get_repositories(username)

    total_stars = get_total_stars(repositories)

    best_repo = get_most_starred_repository(repositories)

if __name__ == '__main__':
    main()