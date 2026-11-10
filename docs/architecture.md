
# System Architecture

## Overview

The burglar alarm system uses two Raspberry Pi devices connected through Wi-Fi and MQTT communication.

The Raspberry Pi Pico W is connected to an HC-SR501 PIR motion sensor. It detects movement and publishes the sensor state to an MQTT broker.

The Raspberry Pi 5 subscribes to the MQTT topic. When movement is detected, it activates the camera to record footage and sends an email notification to the homeowner.

## System Communication

1. The PIR sensor detects movement.
2. The Pico W reads the sensor output.
3. The Pico W publishes a message to the MQTT topic `hello`.
4. The MQTT broker receives and distributes the message.
5. The Raspberry Pi 5 subscribes to the topic and receives the message.
6. If the message is `1`, the Raspberry Pi 5 starts recording.
7. The system saves the video and attempts to send an email notification.

## Communication Technologies

| Technology | Purpose |
|---|---|
| Wi-Fi | Connects the Pico W and Raspberry Pi 5 to the network |
| MQTT | Allows the devices to exchange motion messages |
| Mosquitto | Acts as the MQTT message broker |
| SMTP | Sends email notifications through Gmail |

## Security Considerations

- Wi-Fi credentials should not be stored in public source code.
- Email passwords and app passwords should be stored securely.
- The MQTT broker should be protected against unauthorised access.
- Camera recordings should be stored securely.
- Camera use should respect the privacy of people who may be recorded.

## Future Improvements

- Add a buzzer or warning light.
- Prevent the program from crashing after recording.
- Automatically delete older recordings when storage space is low.
- Add an event logging system.
- Create a protective case for the hardware.

