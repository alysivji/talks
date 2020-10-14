from typing import Dict, List, NamedTuple
from meetup.api import Client as MeetupClient

from busy_beaver.exceptions import NoMeetupEventsFound
from busy_beaver.models import Event


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

    def __init__(self, api_key):
        self.meetup_client = MeetupClient(api_key)

    def get_events(self, group_name: str, count: int = 1) -> List[EventDetails]:
        events = self.meetup_client.GetEvents(group_urlname=group_name)
        if not events.results:
            raise NoMeetupEventsFound

        upcoming_events = []
        for event in events.results[:count]:
            if "venue" in event:
                venue_name = event["venue"]["name"]
            else:
                venue_name = "TBD"

            start_epoch = int(event["time"] / 1000)
            upcoming_events.append(
                EventDetails(
                    id=event["id"],
                    name=event["name"],
                    url=event["event_url"],
                    venue=venue_name,
                    start_epoch=start_epoch,
                    end_epoch=start_epoch + int(event["duration"]),
                )
            )

        return upcoming_events
