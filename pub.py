import paho.mqtt.client as mqtt
 
mqtt_server = "localhost"
mqtt_topic = "test_channel"
def on_message(client, obj, msg):
    print(msg.topic+ "" + str(msg.payload))
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect(mqtt_server)
f = open("test.wav","rb")
audiostring = f.read()
f.close()
byteArray = bytearray(audiostring)
mqttc.publish(mqtt_topic, byteArray)

rc = 0
while rc == 0:
    rc = mqttc.loop()
