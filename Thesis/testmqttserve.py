import time
import matplotlib.pyplot as plt 
import RPi.GPIO as GPIO 
import paho.mqtt.client as mqtt
import cv2
from matplotlib.animation import FuncAnimation
import numpy as np 
allvehicles=[]
timevehi=[]
z=0
#i=1
y=[]
# Setup callback functions that are called when MQTT events happen like 
# connecting to the server or receiving data from a subscribed feed. 
def on_connect(client, userdata, flags, rc): 
   print("Connected with result code " + str(rc)) 
   # Subscribing in on_connect() means that if we lose the connection and 
   # reconnect then subscriptions will be renewed. 
   client.subscribe("/esp8266/pi") 
# The callback for when a PUBLISH message is received from the server. 
def on_message(client, userdata, msg):
    print("received message:")
    x=time.ctime();
    res=msg.payload
    fin=str( msg.payload)+" "+str(x)+':'+'\n'
    print(fin)
    data=res.split(":")[0];
    if data=='infaTraffic' or data=='infacaution':
        with open("infalog.txt","a") as g:
            g.write(str(fin))
    else:
        with open("DataLog.txt","a") as f:
            f.write(str(fin))
        
    
    #if data not in allvehicles:
     #   if data!='infaTraffic':
      #      allvehicles.append(data)
    #def animate(i):
        #timevehi=[]
        #y=[]
        #x=time.ctime();
        #print(x)
        #timevehi.append(float(x[17:19]))
        #y.append(len(allvehicles))
    ##time.sleep(1)
        #ax1.clear()
        #ax1.plot(timevehi,y,'go-')
    #ani = FuncAnimation(fig, animate, interval=1000)
    #plt.show()

    
    


    
   
    
            
   # Check if this is a message for the Pi LED. 
        
# Create MQTT client and connect to localhost, i.e. the Raspberry Pi running 
# this script and the MQTT server. 
client = mqtt.Client() 
client.on_connect = on_connect 

client.connect('iot.eclipse.org', 1883, 60) 
# Connect to the MQTT server and process messages in a background thread. 
client.loop_start() 
# Main loop to listen for button presses. 
print('Script is running, press Ctrl-C to quit...') 
while True: 
   # Look for a change from high to low value on the button input to 
   # signal a button press.
    client.on_message = on_message
    

    
            
    #time.sleep(2) 
     
