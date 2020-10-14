from typing import Dict, List, NamedTuple

from .requests_client import RequestsClient, Response
from busy_beaver.exceptions import NoMeetupEventsFound, UnexpectedStatusCode
from busy_beaver.models import Event

BASE_URL = "https://api.meetup.com"


class EventDetails(NamedTuple):
    id: str
    name: str
    url: str
    venue: str
    start_epoch: int  # utc epoch
    end_epoch: int

    @classmethod
    def from_event_model(cls, model):
        if not isinstance(model, Event):
            raise ValueError("Can only convert Event type")
        return cls(
            id=model.remote_id,
            name=model.name,
            url=model.url,
            venue=model.venue,
            start_epoch=model.start_epoch,
            end_epoch=model.end_epoch,
        )

    def create_event_record_dict(self) -> Dict[str, str]:
        return {
            "remote_id": self.id,
            "name": self.name,
            "url": self.url,
            "venue": self.venue,
            "start_epoch": self.start_epoch,
            "end_epoch": self.end_epoch,
        }

    def create_event_record(self) -> Event:
        event_params = self.create_event_record_dict()
        return Event(**event_params)


class MeetupAdapter:
    """Pull the upcoming events from Meetup and send the message to Slack."""

    def __init__(self, oauth_token: str):
        default_headers = {"Authorization": f"Bearer {oauth_token}"}
        self.client = RequestsClient(headers=default_headers)

    def get_events(self, group_name: str, count: int = 1) -> List[EventDetails]:
        url = BASE_URL + f"/{group_name}/events"
        payload = {"page": count}
        resp: Response = self.client.get(url, params=payload)

        if resp.status_code != 200:
            raise UnexpectedStatusCode

        events = resp.json
        if not events:
            raise NoMeetupEventsFound

        upcoming_events = []
        for event in events:
            if "venue" in event:
                venue_name = event["venue"]["name"]
            else:
                venue_name = "TBD"

            start_epoch = int(event["time"] / 1000)
            upcoming_events.append(
                EventDetails(
                    id=event["id"],
                    name=event["name"],
                    url=event["link"],
                    venue=venue_name,
                    start_epoch=start_epoch,
                    end_epoch=start_epoch + int(event["duration"]),
                )
            )

        return upcoming_events
