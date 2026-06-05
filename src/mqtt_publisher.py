import time
import json
import paho.mqtt.client as mqtt
from sim800l_simulator import SIM800L
from sensor_data import get_sensor_readings

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "eagle-wireless/pawan/telemetry"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT broker: {BROKER}")
    else:
        print(f"Connection failed: {rc}")

def main():
    # Step 1 - simulate SIM800L GPRS setup
    modem = SIM800L()
    modem.setup_gprs(apn="internet")

    # Step 2 - connect MQTT
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "pawan-iot-node")
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    time.sleep(1)

    # Step 3 - publish sensor data
    print(f"Publishing to topic: {TOPIC}\n")
    for i in range(20):
        payload = json.dumps(get_sensor_readings())
        client.publish(TOPIC, payload)
        print(f"[{i+1}/20] {payload}\n")
        time.sleep(5)

    client.loop_stop()
    print("--- Done ---")

if __name__ == "__main__":
    main()

