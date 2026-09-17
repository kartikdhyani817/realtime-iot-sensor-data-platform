import json
import time
from datetime import datetime
from pathlib import Path

from producer.sensor_generator import generate_sensor_event


OUTPUT_FILE = Path("data") / "sensor_events.jsonl"
EVENT_INTERVAL = 2


def save_event(event):
    """Save one sensor event to the JSON Lines file."""

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event) + "\n")


def stream_events(number_of_events=10, interval=EVENT_INTERVAL):
    """Generate and save sensor events continuously."""

    print("=" * 70)
    print("Real-Time IoT Sensor Event Stream")
    print("=" * 70)
    print()
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Event interval: {interval} seconds")
    print()

    for event_number in range(1, number_of_events + 1):

        event = generate_sensor_event()

        save_event(event)

        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] "
            f"Event {event_number}: "
            f"{event['sensor_id']} | "
            f"{event['location']} | "
            f"{event['temperature']}°C | "
            f"Battery: {event['battery_level']}%"
        )

        if event_number < number_of_events:
            time.sleep(interval)


if __name__ == "__main__":
    stream_events()