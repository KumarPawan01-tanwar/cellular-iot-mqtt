import random
import time

def get_sensor_readings():
    return {
        "device_id": "SIM800L-Node-01",
        "temperature_c": round(random.uniform(20.0, 35.0), 2),
        "humidity_pct": round(random.uniform(40.0, 80.0), 2),
        "battery_v": round(random.uniform(3.7, 4.2), 2),
        "signal_strength_dbm": random.randint(-90, -50),
        "network": "GPRS/EDGE",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
    }
