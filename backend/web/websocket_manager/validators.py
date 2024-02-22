from .exceptions import ValidationError, EventNotFoundError
from .events import Event


def event_validator(message: dict) -> bool:
    try:
        if not isinstance(message, dict):
            raise ValidationError

        if message.get("event") is None:
            raise ValidationError

        if message.get("body") is None:
            raise ValidationError

        try:
            event = Event(message)
            event.check()
        except (TypeError, EventNotFoundError):
            raise ValidationError

        return True

    except ValidationError:
        return False

