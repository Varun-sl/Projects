# Pedestrian Detection on CCTV Video
import time  
import RPi.GPIO as GPIO 
import paho.mqtt.client as mqtt
# Import Computer Vision package - cv2
import cv2

# Import Numerical Python package - numpy as np
import numpy as np

# Import Time Python package - time which contains sleep() function
import time

def on_connect(client, userdata, flags, rc): 
   print("Connected with result code " + str(rc)) 
   # Subscribing in on_connect() means that if we lose the connection and 
   # reconnect then subscriptions will be renewed. 
   client.subscribe("/esp8266/pi") 
# Load pedestrain cascade file using cv2.CascadeClassifier built-in function
# cv2.CascadeClassifier([filename]) 
pedestrian_detect = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Initializing video capturing object for video file 
capture = cv2.VideoCapture('walking.avi')

client = mqtt.Client() 
client.on_connect = on_connect 

client.connect('iot.eclipse.org', 1883, 60) 

# Initialize While Loop and execute until Esc key is pressed
#VideoCapture.isOpened returns True if the video is successfully opened
while capture.isOpened():
   
  	#time.sleep(secs) 
	# secs- The number of seconds the Python program should pause execution
    time.sleep(.05)

    # Start capturing frames
    ret, frame = capture.read()
    #canny = cv2.Canny(frame, 300, 100)
    #cv2.imshow('Canny Edge Detection', canny)
    # Resize the frame using cv2.resize built-in function
    # cv2.resize(capturing, output image size, x scale, y scale, interpolation)
    frame = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)

    # Convert RGB to gray using cv2.COLOR_BGR2GRAY built-in function
	# BGR (bytes are reversed)
	# cv2.cvtColor: Converts image from one color space to another
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect pedestrians of different sizes using cv2.CascadeClassifier.detectMultiScale
    # cv2.CascadeClassifier.detectMultiScale(gray, scaleFactor, minNeighbors)
   
    # scaleFactor: Specifies the image size to be reduced
    # Pedestrians closer to the camera appear bigger than those pedestrians in the back.
    
    # minNeighbors: Specifies the number of neighbors each rectangle should have to retain it
    # Higher value results in less detections but with higher quality
    
    pedestrian_detected = pedestrian_detect.detectMultiScale(gray, 1.2, 3)
        
    
    # Extract bounding boxes for any bodies identified
    # Rectangles are drawn around the cars using cv2.rectangle built-in function
	# cv2.rectangle(frame, (x1,y1), (x2,y2), color, thickness)
    for (x,y,w,h) in pedestrian_detected:
        if (x>0)&(y>0)&(w>0)&(h>0):
            client.publish('/esp8266/pi','infapedestr:plat:13.055500lon:77.604546') 
            
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
        
        # Display pedestrians detected using imshow built-in function
        cv2.imshow('Pedestrian Detection', frame)

    # Check if the user has pressed Esc key
	c = cv2.waitKey(1)
	if c == 27:
		break

# Close the capturing device
capture.release()

# Close all windows
cv2.destroyAllWindows()


