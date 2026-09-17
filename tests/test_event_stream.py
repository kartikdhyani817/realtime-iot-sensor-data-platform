import json

import stream.event_stream as event_stream


def test_save_event(tmp_path, monkeypatch):

    output_file = tmp_path / "sensor_events.jsonl"

    monkeypatch.setattr(
        event_stream,
        "OUTPUT_FILE",
        output_file,
    )

    event = {
        "event_id": "test-event-1",
        "sensor_id": "SENSOR-1001",
        "temperature": 25.5,
    }

    event_stream.save_event(event)

    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as file:
        saved_event = json.loads(file.readline())

    assert saved_event["event_id"] == "test-event-1"
    assert saved_event["sensor_id"] == "SENSOR-1001"
    assert saved_event["temperature"] == 25.5