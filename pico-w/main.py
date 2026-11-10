
from machine import Pin
from time import sleep
import machine
import network
import time
import ubinascii
from umqtt.simple import MQTTClient

# Wi-Fi settings
# Add your own details when running the program.
wifi_ssid = "YOUR_WIFI_NAME"
wifi_password = "YOUR_WIFI_PASSWORD"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(wifi_ssid, wifi_password)

# Wait for Wi-Fi connection
while not wifi.isconnected():
    time.sleep(1)

print("Connected to Wi-Fi:", wifi.ifconfig())

# MQTT broker settings
# Replace this with the IP address of your Raspberry Pi 5.
mqtt_broker = "YOUR_RASPBERRY_PI_IP"
mqtt_port = 1883
mqtt_client_id = ubinascii.hexlify(machine.unique_id())
mqtt_topic = b"hello"

# Connect to MQTT broker
mqtt_client = MQTTClient(
    mqtt_client_id,
    mqtt_broker,
    port=mqtt_port
)
mqtt_client.connect()

print("Connected to MQTT broker")

# Initialise the HC-SR501 motion sensor
motion_sensor = Pin(28, Pin.IN, Pin.PULL_UP)

# Publish initial state
mqtt_client.publish(mqtt_topic, b"0")

# Main loop: check for movement
while True:
    move = motion_sensor.value()

    if move == 1:
        print("Motion detected")
        mqtt_client.publish(mqtt_topic, b"1")
    else:
        print("No motion detected")
        mqtt_client.publish(mqtt_topic, b"0")

    sleep(1)

