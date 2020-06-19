import requests
from a_data_transfer_object import RepoStatistics

url = "https://github.com/alysivji/falcon-apispec"
if "github.com" not in url.lower():
    raise ValueError("Not a valid GitHub url")

repo = url.lower().split("github.com/")[1]
project_url = f"https://api.github.com/repos/{repo}"
response = requests.get(project_url)

data = response.json()
result = RepoStatistics(
    id=data["id"],
    description=data["description"],
    stars=data["stargazers_count"],
    forks=data["forks"],
    open_issues=data["open_issues"],
    last_activity=data["pushed_at"],
)

print(result)
