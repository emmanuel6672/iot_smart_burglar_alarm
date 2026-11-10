
# Hardware

## Components used

| Component | Purpose |
|---|---|
| Raspberry Pi Pico W | Reads the motion sensor and sends data over Wi-Fi |
| Raspberry Pi 5 | Receives motion alerts, controls the camera and sends email notifications |
| HC-SR501 PIR Motion Sensor | Detects movement |
| Raspberry Pi Camera Module 1 | Captures video footage |
| Breadboard | Connects the electronic components |
| Jumper wires | Connect the sensor and Pico W |
| Micro USB cable | Powers and connects the Pico W |

## PIR Motion Sensor Connections

The HC-SR501 motion sensor connects to the Raspberry Pi Pico W:

- Power (red) to the positive power strip.
- Data (blue) to GP28 (physical pin 34).
- Ground (brown) to the negative power strip.

## Pico W Breadboard Connections

- Physical pin 38 (GND) to the negative strip.
- Physical pin 36 (3V3 OUT) to the positive strip.

## How the Hardware Works

1. The PIR sensor detects movement.
2. The Pico W reads the sensor output.
3. The Pico W sends a message to the MQTT broker over Wi-Fi.
4. The Raspberry Pi 5 receives the message.
5. The camera records footage when motion is detected.
6. The system sends an email notification.

