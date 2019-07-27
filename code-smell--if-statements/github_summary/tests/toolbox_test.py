import pytest
import responses
from requests.exceptions import HTTPError

from github_summary.toolbox import get_github_events


@pytest.mark.unit
@pytest.mark.vcr()
def test_get_github_events():
    events = get_github_events("alysivji")
    assert len(events) > 0


@responses.activate
def test_get_github_events_returns_400():
    responses.add(
        responses.GET,
        "https://api.github.com/users/alysivji/events/public",
        status=400,
    )

    with pytest.raises(HTTPError):
        get_github_events("alysivji")
