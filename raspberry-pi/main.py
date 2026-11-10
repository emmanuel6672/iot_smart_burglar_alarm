
from picamera2 import Picamera2
import paho.mqtt.client as mqtt
import datetime
import smtplib
import os
import time
from email.message import EmailMessage

# MQTT settings
MQTT_HOST = "YOUR_RASPBERRY_PI_IP"
MQTT_PORT = 1883
MQTT_TOPIC = "hello"

# Email settings
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_APP_PASSWORD")

# Recording duration in seconds
RECORDING_DURATION = 12

picam2 = Picamera2()
camera_config = picam2.create_video_configuration()
picam2.configure(camera_config)

def send_email(video_name):
    if not all([SENDER_EMAIL, RECEIVER_EMAIL, EMAIL_PASSWORD]):
        print("Email settings are missing. Email not sent.")
        return

    message = EmailMessage()
    message["Subject"] = "Motion Detected"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message.set_content(
        f"Motion was detected. Video saved as {video_name}."
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.send_message(message)

    print("Email sent successfully")

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker:", rc)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    motion = msg.payload.decode()
    print("Received:", motion)

    if motion == "1":
        timestamp = datetime.datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )
        video_name = f"motion_{timestamp}.mp4"

        try:
            picam2.start()
            picam2.start_recording(
                # Recording API depends on the installed Picamera2 version.
                # This starter uses the standard H.264 encoder.
                __import__("picamera2.encoders", fromlist=["H264Encoder"]).H264Encoder(),
                __import__("picamera2.outputs", fromlist=["FfmpegOutput"]).FfmpegOutput(video_name)
            )
            time.sleep(RECORDING_DURATION)
            picam2.stop_recording()
            picam2.stop()

            print("Video saved:", video_name)
            send_email(video_name)

        except Exception as error:
            print("Camera or recording error:", error)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Starting burglar alarm receiver...")
client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_forever()

