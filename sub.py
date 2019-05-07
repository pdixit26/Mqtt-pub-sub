import paho.mqtt.client as mqtt
 
mqtt_server = "localhost"
mqtt_topic = "test_channel"
  
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(mqtt_topic,0)
              
              # The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    f = open('new.wav', 'wb')
    f.write(msg.payload)
    f.close()
                        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
                         
client.connect(mqtt_server, 1883, 60)

rc = 0
while rc == 0:
    rc = client.loop()
print("rc:" + str(rc)) 
