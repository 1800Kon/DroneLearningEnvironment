import numpy as np
from djitellopy import tello
import cv2

# Variables
whT = 320
width = 400
height = 400
debug_enabled = 0
counter = 0
minConfidence = 0.5
nms_threshold = 0.3
modelConfiguration = 'yolov3-320.cfg'
modelWeights = 'yolov3.weights'
classesFile = 'coco.names'
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

net = cv2.dnn.readNet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Which camera to use for the image recognition
capture = cv2.VideoCapture(0)

drone = tello.Tello()
drone.connect()
drone.streamon()
print(drone.get_battery())

while True:
    if counter == 1:
        drone.takeoff()
        counter = 1

    frame_read = drone.get_frame_read()
    frame = frame_read.frame
    img = cv2.resize(frame, (width, height))
        
    cv2.imshow("Drone", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break
