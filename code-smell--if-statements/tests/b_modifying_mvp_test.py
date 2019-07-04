from github_summary.b_modifying_mvp import (
    extract_events_of_interest,
    generate_summary_from_events,
    perform
)
import pytest


@pytest.mark.end_to_end
@pytest.mark.vcr()
def test_perform():
    summary_text = perform(github_username="alysivji")

    assert "busy-beaver-dev/busy-beaver" in summary_text
    assert ":star:" in summary_text


@pytest.mark.unit
def test_extract_events_of_interest_standard_case():
    # Arrange
    events = [
        {"type": "PushEvent"},
        {"type": "PushEvent"},
        {"type": "WatchEvent"},
        {"type": "PullRequestEvent", "payload": {"action": "opened"}},
        {"type": "PullRequestEvent", "payload": {"action": "closed"}},
    ]

    # Act
    classified_events = extract_events_of_interest(events)

    # Assert
    assert len(classified_events["PushEvent"]) == 2
    assert len(classified_events["WatchEvent"]) == 1
    assert len(classified_events["PullRequestEvent"]) == 1


@pytest.mark.unit
def test_extract_events_of_interest_no_events():
    # Arrange
    events = [{"type": "RandomEvent"}]

    # Act
    classified_events = extract_events_of_interest(events)

    # Assert
    assert not classified_events


@pytest.mark.unit
def test_generate_summary_for_empty_events():
    output_text = generate_summary_from_events("alysivji", {})

    assert "alysivji" in output_text
    assert "arrow_up" not in output_text
    assert "star" not in output_text
    assert "arrow_heading_up" not in output_text


@pytest.mark.unit
def test_generate_summary_for_commits():
    # Arrange
    classified_events = {
        "PushEvent": [
            {
                "repo": {"name": "alysivji/repo1"},
                "payload": {"commits": ["commit1", "commit2", "commit3"]},
            },
            {
                "repo": {"name": "alysivji/repo2"},
                "payload": {"commits": ["commit1", "commit2", "commit3"]},
            },
        ]
    }

    # Act
    output_text = generate_summary_from_events("alysivji", classified_events)

    # Assert
    assert "alysivji" in output_text

    assert "arrow_up" in output_text
    assert "6 commit(s)" in output_text
    assert "alysivji/repo1" in output_text
    assert "alysivji/repo2" in output_text

    assert "star" not in output_text
    assert "arrow_heading_up" not in output_text


@pytest.mark.unit
def test_generate_summary_for_stars():
    # Arrange
    classified_events = {
        "WatchEvent": [
            {"repo": {"name": "alysivji/repo1"}},
            {"repo": {"name": "alysivji/repo2"}},
        ]
    }

    # Act
    output_text = generate_summary_from_events("alysivji", classified_events)

    # Assert
    assert "alysivji" in output_text
    assert "arrow_up" not in output_text
    assert "arrow_heading_up" not in output_text

    assert "star" in output_text
    assert "2 repo(s)" in output_text
    assert "alysivji/repo1" in output_text
    assert "alysivji/repo2" in output_text


@pytest.mark.unit
def test_generate_summary_for_pull_requests_opened():
    # Arrange
    classified_events = {
        "PullRequestEvent": [
            {
                "repo": {"name": "alysivji/repo1"},
                "payload": {"pull_request": {"number": "123"}},
            },
            {
                "repo": {"name": "alysivji/repo2"},
                "payload": {"pull_request": {"number": "123"}},
            },
        ]
    }

    # Act
    output_text = generate_summary_from_events("alysivji", classified_events)

    # Assert
    assert "alysivji" in output_text
    assert "arrow_up" not in output_text
    assert "star" not in output_text

    assert "arrow_heading_up" in output_text
    assert "2 PR(s)" in output_text
    assert "alysivji/repo1" in output_text
    assert "alysivji/repo2" in output_text
