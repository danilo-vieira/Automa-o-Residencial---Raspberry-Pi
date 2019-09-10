import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("teste/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	msg.payload
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("qtxbakah", "nJZTyLHKm6pV")
client.connect("soldier.cloudmqtt.com", 15788, 60)


#client.loop_forever()
client.loop_start()
time.sleep(3)

while True:
	try:
		a = int(input("Digite op: "))
		if(a == 1):
			v = "ligar"
			print ("Sensor Ativado!")
			client.publish("teste", v)
		if(a == 0):
			v = "10ligar"
			print("Sensor 10Ativado!")
			client.publish("teste", v)
		time.sleep(1)
	except KeyboardInterrupt:
		client.loop_stop()
		client.disconnect()