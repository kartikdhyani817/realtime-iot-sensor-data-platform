from datetime import datetime
from uuid import UUID


VALID_LOCATIONS = {
    "Dublin",
    "Cork",
    "Galway",
    "Limerick",
    "Waterford",
}

VALID_STATUSES = {
    "active",
    "inactive",
    "maintenance",
}


REQUIRED_FIELDS = {
    "event_id",
    "sensor_id",
    "device_type",
    "temperature",
    "humidity",
    "pressure",
    "battery_level",
    "status",
    "location",
    "event_time",
}


def validate_sensor_event(event):
    """Validate a single IoT sensor event."""

    errors = []

    if not isinstance(event, dict):
        return False, ["Event must be a dictionary."]

    missing_fields = REQUIRED_FIELDS - event.keys()

    if missing_fields:
        errors.append(
            f"Missing fields: {sorted(missing_fields)}"
        )

    if errors:
        return False, errors

    try:
        UUID(event["event_id"])
    except (ValueError, TypeError, AttributeError):
        errors.append("event_id must be a valid UUID.")

    if not isinstance(event["sensor_id"], str):
        errors.append("sensor_id must be a string.")
    elif not event["sensor_id"].startswith("SENSOR-"):
        errors.append("sensor_id must start with 'SENSOR-'.")

    if not isinstance(event["temperature"], (int, float)):
        errors.append("temperature must be numeric.")
    elif not 15.0 <= event["temperature"] <= 35.0:
        errors.append("temperature must be between 15 and 35°C.")

    if not isinstance(event["humidity"], (int, float)):
        errors.append("humidity must be numeric.")
    elif not 30.0 <= event["humidity"] <= 80.0:
        errors.append("humidity must be between 30 and 80%.")

    if not isinstance(event["pressure"], (int, float)):
        errors.append("pressure must be numeric.")
    elif not 990.0 <= event["pressure"] <= 1030.0:
        errors.append("pressure must be between 990 and 1030 hPa.")

    if not isinstance(event["battery_level"], int):
        errors.append("battery_level must be an integer.")
    elif not 20 <= event["battery_level"] <= 100:
        errors.append("battery_level must be between 20 and 100%.")

    if event["status"] not in VALID_STATUSES:
        errors.append(
            f"status must be one of: {sorted(VALID_STATUSES)}."
        )

    if event["location"] not in VALID_LOCATIONS:
        errors.append(
            f"location must be one of: {sorted(VALID_LOCATIONS)}."
        )

    try:
        datetime.fromisoformat(event["event_time"])
    except (ValueError, TypeError):
        errors.append("event_time must be a valid ISO timestamp.")

    return len(errors) == 0, errors