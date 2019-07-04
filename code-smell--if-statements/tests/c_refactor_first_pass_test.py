import pytest
import responses
from github_summary.c_refactor_first_pass import perform


@pytest.mark.end_to_end
@pytest.mark.vcr()
def test_perform():
    summary_text = perform(github_username="alysivji")

    assert "busy-beaver-dev/busy-beaver" in summary_text
    assert ":arrow_up: 19 commit(s) to 2 repo(s)" in summary_text
    assert ":star: 4 repo(s)" in summary_text
    assert ":arrow_heading_up: 2 PR(s)" in summary_text


@pytest.mark.end_to_end  # This became an integration test
@responses.activate
def test_generate_summary_for_empty_events():
    # Arrange
    responses.add(
        responses.GET,
        "https://api.github.com/users/alysivji/events/public",
        status=200,
        json=[],
    )

    output_text = perform("alysivji")

    assert "alysivji" in output_text
    assert "arrow_up" not in output_text
    assert "star" not in output_text
    assert "arrow_heading_up" not in output_text
