import random
import uuid
from datetime import datetime


LOCATIONS = [
    "Dublin",
    "Cork",
    "Galway",
    "Limerick",
    "Waterford",
]

DEVICE_TYPES = [
    "Temperature Sensor",
    "Humidity Sensor",
    "Environmental Sensor",
    "Industrial Sensor",
]


def generate_sensor_event():
    """Generate a realistic IoT sensor event."""

    device_type = random.choice(DEVICE_TYPES)

    temperature = round(random.uniform(15.0, 35.0), 2)
    humidity = round(random.uniform(30.0, 80.0), 2)
    pressure = round(random.uniform(990.0, 1030.0), 2)
    battery_level = random.randint(20, 100)

    event = {
        "event_id": str(uuid.uuid4()),
        "sensor_id": f"SENSOR-{random.randint(1000, 9999)}",
        "device_type": device_type,
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure,
        "battery_level": battery_level,
        "status": "active",
        "location": random.choice(LOCATIONS),
        "event_time": datetime.now().isoformat(),
    }

    return event


def generate_events(number_of_events=10):
    """Generate multiple IoT sensor events."""

    events = []

    for _ in range(number_of_events):
        events.append(generate_sensor_event())

    return events


if __name__ == "__main__":

    print("=" * 70)
    print("IoT Sensor Data Generator")
    print("=" * 70)
    print()

    events = generate_events(10)

    for event in events:
        print(event)