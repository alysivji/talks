from github_summary.d_refactor_complete import (
    perform
)
import pytest


@pytest.mark.end_to_end
@pytest.mark.vcr()
def test_perform():
    summary_text = perform(github_username="alysivji")

    assert "busy-beaver-dev/busy-beaver" in summary_text
    assert ":star:" in summary_text
