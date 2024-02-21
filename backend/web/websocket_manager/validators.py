from .exceptions import ValidationError


def message_validator(message: dict) -> dict:
    if not isinstance(message, dict):
        raise ValidationError(message_validator.__name__)

    return message
