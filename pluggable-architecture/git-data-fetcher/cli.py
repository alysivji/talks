import argparse
from git_data_fetcher.download_data import GitFetcher


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


if __name__ == "__main__":
    args = parse_args()
    client = GitFetcher(args["url"])
    client.get_stats()

    print()
