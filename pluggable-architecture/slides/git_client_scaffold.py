class GitApiClient:
    def __init__(self, url):
        self.plugin = initialize_plugin(url)

    def get_stats(self):
        return self.plugin.repo_stats()


url = ""
client = GitApiClient(url)
stats = client.get_stats()
print(stats)
