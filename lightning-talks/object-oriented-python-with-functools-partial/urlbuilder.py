from functools import partial

GITHUB_BASE_URL = "https://api.github.com"


def create_url(*items):
    return "/".join(items)


GITHUB_BASE_URL = "https://api.github.com"
user = "alysivji"
repo = "talks"


url_fstring = f"{GITHUB_BASE_URL}/repos/{user}/{repo}"
print(url_fstring)

url_formatstring = "{0}/repos/{1}/{2}".format(GITHUB_BASE_URL, user, repo)
print(url_formatstring)


def create_url(*items):
    return "/".join(items)


GITHUB_BASE_URL = "https://api.github.com"
github_url = partial(create_url, GITHUB_BASE_URL)  # we just have to define this one


user = "alysivji"
repo = "talks"
url = github_url("repos", user, repo)
print(url)
