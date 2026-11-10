# IoT Smart Burglar Alarm System

## Project Overview

This project is an Internet of Things (IoT) based burglar alarm system designed to improve traditional burglar alarms by notifying homeowners when movement is detected.

The system uses a Raspberry Pi Pico W, Raspberry Pi 5, PIR motion sensor and camera to detect movement, record footage and send email notifications.

## Hardware Components

- Raspberry Pi Pico W
- Raspberry Pi 5
- HC-SR501 PIR Motion Sensor
- Raspberry Pi Camera Module
- Breadboard
- Jumper wires
- Micro USB cable

## Software and Technologies

- Python
- MicroPython
- MQTT
- Mosquitto Broker
- Thonny IDE
- Raspberry Pi OS
- SMTP Email Notifications

## How It Works

1. The PIR motion sensor detects movement.
2. The Raspberry Pi Pico W reads the sensor.
3. The Pico W publishes a message to the MQTT broker.
4. The Raspberry Pi 5 receives the message.
5. The camera starts recording when motion is detected.
6. An email notification is sent to the homeowner.

## System Architecture

The system uses two Raspberry Pi devices connected through Wi-Fi and MQTT communication.

- Pico W: Handles motion detection.
- Raspberry Pi 5: Handles camera recording and email notifications.

## Project Objectives

- Detect movement using a PIR sensor.
- Capture video footage when movement is detected.
- Notify homeowners through email.
- Demonstrate communication between IoT devices using MQTT.
- Improve traditional burglar alarm functionality.

## Disclaimer

This project is an educational prototype and should not be relied upon as a complete commercial security system.
