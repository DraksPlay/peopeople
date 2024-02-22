from pydantic import BaseModel

from .exceptions import EventNotFoundError


class Event:

    def __init__(self,
                 message: dict
                 ) -> None:
        self.message = message

        self.events = {
            "open": OpenEvent,
            "new_message": NewMessageEvent
        }

    def check(self):
        event_class = self.events.get(self.message.get("event"))
        if event_class is None:
            raise EventNotFoundError

        event_body = self.message.get("body")
        event_class(**event_body)

        return True

    def create(self):
        event_class = self.events.get(self.message.get("event"))

        event_body = self.message.get("body")
        return event_class(**event_body)


class OpenEvent(BaseModel):
    pass

class NewMessageEvent(BaseModel):
    text: str
    username: str
