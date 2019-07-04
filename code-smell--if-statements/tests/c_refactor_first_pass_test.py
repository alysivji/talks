from github_summary.c_refactor_first_pass import (
    perform
)
import pytest


@pytest.mark.end_to_end
@pytest.mark.vcr()
def test_perform():
    summary_text = perform(github_username="alysivji")

    assert "busy-beaver-dev/busy-beaver" in summary_text
    assert ":arrow_up: 19 commit(s) to 2 repo(s)" in summary_text
    assert ":star: 4 repo(s)" in summary_text
    assert ":arrow_heading_up: 2 PR(s)" in summary_text
