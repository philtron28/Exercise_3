import paho.mqtt.client as mqtt
import requests

broker = "test.mosquitto.org"
port = 1883
topic = "http/post"

url = "https://httpbin.org/post"
headers = {"Content-Type": "application/json"}
payload = {"key": "Filippos Stratis HMTY"}

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.publish(topic, str(payload))

def on_publish(client, userdata, mid):
    print("Message published to topic")
    send_http_request()

def send_http_request():
    response = requests.request("POST", url, headers=headers, data=str(payload))
    print("HTTP response: " + str(response.status_code))

client = mqtt.Client()

client.on_connect = on_connect
client.on_publish = on_publish

client.connect(broker, port, 60)

client.loop_forever()
