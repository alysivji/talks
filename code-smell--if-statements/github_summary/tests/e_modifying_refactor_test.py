import pytest
import responses

from github_summary.e_modifying_refactor import (
    Commits,
    GitHubUserEvents,
    IssuesOpened,
    perform,
    PullRequestsOpened,
    Stars,
)


@pytest.mark.end_to_end
@pytest.mark.vcr()
def test_perform():
    summary_text = perform(github_username="alysivji")

    assert "busy-beaver-dev/busy-beaver" in summary_text
    assert ":arrow_up: 19 commit(s) to 2 repo(s)" in summary_text
    assert ":star: 4 repo(s)" in summary_text
    assert ":arrow_heading_up: 2 PR(s)" in summary_text
    assert ":interrobang:" not in summary_text


@pytest.mark.end_to_end
@responses.activate
def test_generate_summary_for_empty_events():
    # Arrange
    responses.add(
        responses.GET,
        "https://api.github.com/users/alysivji/events/public",
        status=200,
        json=[],
    )

    events = GitHubUserEvents("alysivji")
    output_text = events.generate_summary_text()

    assert "alysivji" in output_text
    assert "arrow_up" not in output_text
    assert "star" not in output_text
    assert "arrow_heading_up" not in output_text


@pytest.mark.unit
def test_classify_events():
    # Arrange
    events = [
        {"type": "PushEvent"},
        {"type": "PushEvent"},
        {"type": "WatchEvent"},
        {"type": "PullRequestEvent", "payload": {"action": "opened"}},
        {"type": "PullRequestEvent", "payload": {"action": "closed"}},
        {"type": "IssuesEvent", "payload": {"action": "opened"}},
        {"type": "IssuesEvent", "payload": {"action": "closed"}},
    ]

    # Act
    commit_events = Commits()
    num_commit_events = sum([commit_events.matches_event(event) for event in events])

    star_events = Stars()
    num_stars = sum([star_events.matches_event(event) for event in events])

    pr_events = PullRequestsOpened()
    num_prs = sum([pr_events.matches_event(event) for event in events])

    issue_events = IssuesOpened()
    num_issues = sum([issue_events.matches_event(event) for event in events])

    # Assert
    assert num_commit_events == 2
    assert num_stars == 1
    assert num_prs == 1
    assert num_issues == 1


@pytest.mark.unit
def test_extract_events_of_interest_no_events():
    # Arrange
    events = [{"type": "RandomEvent"}]

    # Act
    commit_events = Commits()
    num_commit_events = sum([commit_events.matches_event(event) for event in events])

    star_events = Stars()
    num_stars = sum([star_events.matches_event(event) for event in events])

    pr_events = PullRequestsOpened()
    num_prs = sum([pr_events.matches_event(event) for event in events])

    issue_events = IssuesOpened()
    num_issues = sum([issue_events.matches_event(event) for event in events])

    # Assert
    assert num_commit_events == 0
    assert num_stars == 0
    assert num_prs == 0
    assert num_issues == 0


@pytest.mark.unit
def test_commits():
    # Arrange
    classified_events = [
        {
            "repo": {"name": "alysivji/repo1"},
            "payload": {"commits": ["commit1", "commit2", "commit3"]},
        },
        {
            "repo": {"name": "alysivji/repo2"},
            "payload": {"commits": ["commit1", "commit2", "commit3"]},
        },
    ]
    commits = Commits()
    [commits.append(event) for event in classified_events]

    # Act
    output_text = commits.generate_summary_text()

    # Assert
    assert "arrow_up" in output_text
    assert "6 commit(s)" in output_text
    assert "alysivji/repo1" in output_text
    assert "alysivji/repo2" in output_text


@pytest.mark.unit
def test_stars():
    # Arrange
    classified_events = [
        {"repo": {"name": "alysivji/repo1"}},
        {"repo": {"name": "alysivji/repo2"}},
    ]

    stars = Stars()
    [stars.append(event) for event in classified_events]

    # Act
    output_text = stars.generate_summary_text()

    # Assert
    assert "star" in output_text
    assert "2 repo(s)" in output_text
    assert "alysivji/repo1" in output_text
    assert "alysivji/repo2" in output_text


@pytest.mark.unit
def test_pull_requests_opened():
    # Arrange
    classified_events = [
        {
            "repo": {"name": "alysivji/repo1"},
            "payload": {"pull_request": {"number": "123"}},
        },
        {
            "repo": {"name": "alysivji/repo2"},
            "payload": {"pull_request": {"number": "123"}},
        },
    ]
    pull_requests = PullRequestsOpened()
    [pull_requests.append(event) for event in classified_events]

    # Act
    output_text = pull_requests.generate_summary_text()

    # Assert
    assert "arrow_heading_up" in output_text
    assert "2 PR(s)" in output_text
    assert "alysivji/repo1#123" in output_text
    assert "alysivji/repo2#123" in output_text


@pytest.mark.unit
def test_issues_opened():
    # Arrange
    classified_events = [
        {
            "repo": {"name": "alysivji/repo1"},
            "payload": {"issue": {"number": "123"}},
        },
        {
            "repo": {"name": "alysivji/repo2"},
            "payload": {"issue": {"number": "123"}},
        },
    ]
    issue_events = IssuesOpened()
    [issue_events.append(event) for event in classified_events]

    # Act
    output_text = issue_events.generate_summary_text()

    # Assert
    assert "interrobang" in output_text
    assert "2 issue(s)" in output_text
    assert "alysivji/repo1#123" in output_text
    assert "alysivji/repo2#123" in output_text
