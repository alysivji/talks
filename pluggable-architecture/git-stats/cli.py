import argparse
from git_stats.download import GitApiClient
from git_stats.plugins.base import RepoStatistics


def parse_args():
    description = "Fetch statistics from Online Git Repo"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--url",
        type=str,
        help="URL to repository: https://[github/bitbucket/gitlab].com/repo",
        required=True,
    )
    return vars(parser.parse_args())


def format_output(stats: RepoStatistics):
    print("Description: ", stats.description)
    print("Stars: ", stats.stars)
    print("Forks: ", stats.forks)
    print("Open Issues: ", stats.open_issues)
    print("Last Activity: ", stats.last_activity)


if __name__ == "__main__":
    args = parse_args()
    client = GitApiClient(args["url"])
    stats = client.get_stats()
    format_output(stats)
    print()
