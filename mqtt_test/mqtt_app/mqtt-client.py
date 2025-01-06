import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe("lora/data")  # Topic to listen to
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")
    # Process and store the message in Django (e.g., save to database)

def start_mqtt_client():
    broker = "broker.emqx.io"
    port = 1883

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port, 60)

    client.loop_start()  # Start the MQTT loop in a non-blocking way

