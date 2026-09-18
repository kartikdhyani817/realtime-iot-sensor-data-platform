from producer.sensor_generator import generate_sensor_event
from processing.validator import validate_sensor_event


def test_valid_sensor_event():

    event = generate_sensor_event()

    is_valid, errors = validate_sensor_event(event)

    assert is_valid is True
    assert errors == []


def test_missing_required_field():

    event = generate_sensor_event()

    del event["temperature"]

    is_valid, errors = validate_sensor_event(event)

    assert is_valid is False
    assert "Missing fields: ['temperature']" in errors


def test_invalid_temperature():

    event = generate_sensor_event()

    event["temperature"] = 100

    is_valid, errors = validate_sensor_event(event)

    assert is_valid is False
    assert "temperature must be between 15 and 35°C." in errors


def test_invalid_humidity():

    event = generate_sensor_event()

    event["humidity"] = 95

    is_valid, errors = validate_sensor_event(event)

    assert is_valid is False
    assert "humidity must be between 30 and 80%." in errors


def test_invalid_battery():

    event = generate_sensor_event()

    event["battery_level"] = 5

    is_valid, errors = validate_sensor_event(event)

    assert is_valid is False
    assert "battery_level must be between 20 and 100%." in errors


def test_invalid_location():

    event = generate_sensor_event()

    event["location"] = "London"

    is_valid, errors = validate_sensor_event(event)

    assert is_valid is False
    assert "location must be one of: ['Cork', 'Dublin', 'Galway', 'Limerick', 'Waterford']." in errors


def test_invalid_event_id():

    event = generate_sensor_event()

    event["event_id"] = "invalid-id"

    is_valid, errors = validate_sensor_event(event)

    assert is_valid is False
    assert "event_id must be a valid UUID." in errors