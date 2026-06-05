# Cellular IoT MQTT Pipeline

Simulated SIM800L GSM module telemetry pipeline over MQTT to cloud broker.

## Architecture
[Sensor Data] → [SIM800L GSM Module] → [GPRS Network] → [MQTT Broker] → [Cloud]

## What It Does
- Simulates SIM800L GPRS bring-up using AT commands (AT, AT+CSQ, AT+CREG, AT+SAPBR)
- Publishes structured JSON telemetry every 5 seconds to HiveMQ cloud broker
- Mirrors real automotive TCU/IoT module data pipeline architecture

## Telemetry Graph
[Telemetry](results/telemetry_graph.png)

## Technologies
| Layer | Technology |
|---|---|
| Module Interface | SIM800L AT Commands (UART) |
| Network | GPRS/EDGE cellular |
| Protocol | MQTT (paho-mqtt) |
| Broker | HiveMQ Cloud (broker.hivemq.com) |
| Language | Python 3 |

## How to Run
```bash
pip install -r requirements.txt
cd src
python3 mqtt_publisher.py
```

## Sample Output
```json
{
  "device_id": "SIM800L-Node-01",
  "temperature_c": 27.06,
  "humidity_pct": 54.04,
  "battery_v": 3.74,
  "signal_strength_dbm": -62,
  "network": "GPRS/EDGE",
  "timestamp": "2026-06-05T13:45:50"
}
```

## Author
**Pawan Kumar** — M.Eng. Autonomous Driving, Hochschule Coburg
