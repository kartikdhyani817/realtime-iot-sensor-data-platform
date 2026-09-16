# Real-Time IoT Sensor Data Platform b

A real-time IoT data engineering project that simulates sensor devices continuously sending data, streams those events through Apache Kafka, processes and validates the incoming data, and stores the results in PostgreSQL for analytics.

The project is designed to demonstrate practical **Data Engineering, real-time streaming, data quality, and analytics** skills through an end-to-end pipeline.

---

## 📌 Project Overview

IoT devices generate huge amounts of data continuously.

This project simulates that environment by creating realistic sensor events such as:

* Temperature
* Humidity
* Pressure
* Device status
* Battery level
* Location
* Sensor timestamp

The generated data will be streamed in real time using Apache Kafka, processed using Python, and stored in PostgreSQL.

The final stage will provide an analytics layer and dashboard for monitoring sensor behaviour.

---

## 🏗️ Architecture

```text
                  IoT Sensor Devices
                         │
                         ▼
                Sensor Data Simulator
                         │
                         ▼
                  Kafka Producer
                         │
                         ▼
                   Apache Kafka
                         │
                         ▼
                  Kafka Consumer
                         │
                         ▼
              Data Validation Layer
                         │
                         ▼
            Data Transformation Layer
                         │
                         ▼
                    PostgreSQL
                         │
                         ▼
                  Analytics Layer
                         │
                         ▼
                    Dashboard
```

---

## 🛠️ Tech Stack

| Technology   | Purpose                               |
| ------------ | ------------------------------------- |
| Python       | Sensor simulation and data processing |
| Apache Kafka | Real-time data streaming              |
| PostgreSQL   | Data storage                          |
| SQL          | Data analysis and querying            |
| Pandas       | Data transformation and analysis      |
| Pytest       | Automated testing                     |
| Docker       | Containerization                      |
| Streamlit    | Analytics dashboard                   |
| Git & GitHub | Version control                       |

---

## 🎯 Project Objectives

The main objectives of this project are:

* Build a real-time streaming pipeline
* Simulate IoT sensor data
* Work with Apache Kafka
* Implement data validation
* Transform streaming data
* Store sensor data in PostgreSQL
* Perform analytical SQL queries
* Build a monitoring dashboard
* Implement automated testing
* Apply production-style data engineering practices

---

## 📊 Example Sensor Event

A future sensor event will look similar to:

```json
{
  "sensor_id": "SENSOR-1001",
  "device_type": "Temperature Sensor",
  "temperature": 27.4,
  "humidity": 61.2,
  "pressure": 1012.5,
  "battery_level": 87,
  "status": "active",
  "location": "Dublin",
  "event_time": "2026-09-14T16:00:00"
}
```

---

## 📂 Planned Project Structure

```text
realtime-iot-sensor-data-platform/
│
├── producer/
├── consumer/
├── processing/
├── database/
├── analytics/
├── dashboard/
├── tests/
├── config/
├── data/
│
├── README.md
├── requirements.txt
├── pytest.ini
└── .gitignore
```

---

## 📅 Development Roadmap

### Phase 1 — Data Generation & Streaming

* [ ] Day 1 — Project setup and documentation
* [ ] Day 2 — IoT sensor event generator
* [ ] Day 3 — Kafka setup
* [ ] Day 4 — Kafka producer
* [ ] Day 5 — Kafka consumer

### Phase 2 — Data Engineering

* [ ] Day 6 — Data validation
* [ ] Day 7 — Data transformation
* [ ] Day 8 — PostgreSQL integration
* [ ] Day 9 — Database optimization

### Phase 3 — Analytics

* [ ] Day 10 — SQL analytics
* [ ] Day 11 — Real-time aggregations
* [ ] Day 12 — Streamlit monitoring dashboard

### Phase 4 — Production Improvements

* [ ] Day 13 — Testing and data quality
* [ ] Day 14 — Docker and final documentation

---

## 💡 What This Project Will Demonstrate

By the end of the project, it will demonstrate practical experience with:

* Real-time data ingestion
* Event streaming
* Apache Kafka
* Python data processing
* Data validation
* Data transformation
* PostgreSQL
* SQL analytics
* Data quality
* Automated testing
* Docker
* Dashboard development
* Git/GitHub workflows

---

## 🚧 Project Status

**Current Status: Day 1 — Project Setup**

The project architecture and development roadmap have been defined.

The next step is to build the IoT sensor data generator and start producing realistic streaming events.

---

## 👨‍💻 Author

**Kartik Dhyani**

Built as a practical Data Engineering portfolio project.
