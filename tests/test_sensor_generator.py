from producer.sensor_generator import generate_sensor_event


def test_sensor_event_contains_required_fields():

    event = generate_sensor_event()

    required_fields = [
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
    ]

    for field in required_fields:
        assert field in event


def test_temperature_range():

    event = generate_sensor_event()

    assert 15.0 <= event["temperature"] <= 35.0


def test_humidity_range():

    event = generate_sensor_event()

    assert 30.0 <= event["humidity"] <= 80.0


def test_pressure_range():

    event = generate_sensor_event()

    assert 990.0 <= event["pressure"] <= 1030.0


def test_battery_range():

    event = generate_sensor_event()

    assert 20 <= event["battery_level"] <= 100


def test_sensor_id_format():

    event = generate_sensor_event()

    assert event["sensor_id"].startswith("SENSOR-")


def test_event_id_is_unique():

    event_1 = generate_sensor_event()
    event_2 = generate_sensor_event()

    assert event_1["event_id"] != event_2["event_id"]