from github_summary.c_refactor_first_pass import (
    perform
)
import pytest


@pytest.mark.end_to_end
@pytest.mark.vcr()
def test_perform():
    summary_text = perform(github_username="alysivji")

    assert "busy-beaver-dev/busy-beaver" in summary_text
    assert ":star:" in summary_text
