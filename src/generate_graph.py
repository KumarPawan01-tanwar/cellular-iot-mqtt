import matplotlib.pyplot as plt
import json
import random
import time

# Simulate 20 readings (same as mqtt_publisher)
readings = []
for i in range(20):
    readings.append({
        "packet": i + 1,
        "temperature_c": round(random.uniform(20.0, 35.0), 2),
        "humidity_pct": round(random.uniform(40.0, 80.0), 2),
        "signal_strength_dbm": random.randint(-90, -50)
    })

packets = [r["packet"] for r in readings]
temps = [r["temperature_c"] for r in readings]
humidity = [r["humidity_pct"] for r in readings]
signal = [r["signal_strength_dbm"] for r in readings]

fig, axes = plt.subplots(3, 1, figsize=(10, 8))
fig.suptitle("SIM800L IoT Node — Live Telemetry\nTopic: eagle-wireless/pawan/telemetry", fontsize=13)

axes[0].plot(packets, temps, color="red", marker="o")
axes[0].set_ylabel("Temperature (°C)")
axes[0].set_title("Temperature over 20 MQTT Packets")
axes[0].grid(True)

axes[1].plot(packets, humidity, color="blue", marker="s")
axes[1].set_ylabel("Humidity (%)")
axes[1].set_title("Humidity over 20 MQTT Packets")
axes[1].grid(True)

axes[2].plot(packets, signal, color="green", marker="^")
axes[2].set_ylabel("Signal (dBm)")
axes[2].set_title("GSM Signal Strength over 20 MQTT Packets")
axes[2].grid(True)

plt.tight_layout()
plt.savefig("results/telemetry_graph.png", dpi=150)
print("Graph saved to results/telemetry_graph.png")
