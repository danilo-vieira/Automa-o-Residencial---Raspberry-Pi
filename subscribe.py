import paho.mqtt.client as mqtt

import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("teste/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msg.payload
    
    if(str(msg.payload) == "b'ligar'"):
        print("Algo ligou")

    elif(str(msg.payload) == "b'10ligar'"):
        print("Algo desligou")
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("qtxbakah", "nJZTyLHKm6pV")
client.connect("soldier.cloudmqtt.com", 15788, 60)


client.loop_forever()
