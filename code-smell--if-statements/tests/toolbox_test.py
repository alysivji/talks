import pytest
from github_summary.toolbox import get_github_events


@pytest.mark.unit
@pytest.mark.vcr()
def test_get_github_events():
    events = get_github_events("alysivji")
    assert len(events) > 0
