
# System Diagrams

## System Communication Diagram

The diagram below shows how the different parts of the burglar alarm system communicate.

```text
+----------------------+
| HC-SR501 PIR Sensor  |
+----------------------+
           |
           v
+----------------------+
| Raspberry Pi Pico W  |
| Reads motion sensor  |
+----------------------+
           |
           | Wi-Fi / MQTT
           v
+----------------------+
| MQTT Broker          |
| Mosquitto            |
+----------------------+
           |
           | MQTT message
           v
+----------------------+
| Raspberry Pi 5       |
| Receives motion data |
+----------------------+
           |
           v
+----------------------+
| Raspberry Pi Camera  |
| Records video        |
+----------------------+
           |
           v
+----------------------+
| Email Notification   |
| Alerts homeowner     |
+----------------------+
```

## Diagram Explanation

1. The PIR sensor detects movement.
2. The Pico W publishes the motion status.
3. Mosquitto distributes the MQTT message.
4. The Raspberry Pi 5 receives the message.
5. The camera records footage when movement is detected.
6. An email notification is sent to the homeowner.

