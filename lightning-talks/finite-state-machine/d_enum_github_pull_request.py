class GitHubPullRequest:
    OPENED = "opened"
    CLOSED = "closed"
    MERGED = "merged"

    def __init__(self):
        self.state = self.OPENED
        self.num_approvals = 0
        self.request_changes = False

    def approve(self):
        if self.state == self.OPENED:
            self.num_approvals += 1

    def request_changes(self):
        if self.state == self.OPENED:
            self.request_changes = True

    def close_pull_request(self):
        if self.state == self.OPENED:
            self.state = self.CLOSED

    def merge_pull_request(self, user):
        if self.state == self.OPENED and (self.num_approvals >= 1 or user.admin):
            self.state = self.MERGED
