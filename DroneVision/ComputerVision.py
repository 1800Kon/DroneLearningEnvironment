# flake8: noqa

from time import sleep

import numpy as np
from djitellopy import tello
import cv2



# Variables
whT = 320
width = 720
height = 720
debug_enabled = True
webcam_mode = True
minConfidence = 0.5
nms_threshold = 0.3
modelConfiguration = 'yolov3-320.cfg'
modelWeights = 'yolov3.weights'
classesFile = 'coco.names'
classNames = []
takeoff = False
# The object to recognize, put the name in all caps and make sure it matches the format in the coco.names file
objectToRecognize = "CUP"
# Used to check for centering in object recognition

# THIS IS THE CAMERA TO USE WHEN NOT CONNECTED TO THE DRONE
if webcam_mode:
    capture = cv2.VideoCapture(0)

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# VISION STUFF BELOW
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

# Parse all the objects to recognize, DONT DELETE THE CLASSNAMES VARIABLE EVEN THOUGH PYTHON SAYS ITS UNUSED,
# ITS USED BY THE SDK WRAPPER
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Set up the neural network with the model configuration we specified in the variables
net = cv2.dnn.readNet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


# Find the coordinates of the object and check if it is centered
def checkCenter(x, y, w, h):
    global fullCenter, centerX, centerY
    if (x + (w / 2)) < 250:
        # drone.rotate_counter_clockwise(100)
        centerX = False
    if (x + (w / 2)) > 450:
        # drone.rotate_clockwise(100)
        centerX = False

    if ((x + (w / 2)) < 450) and ((x + (w / 2)) > 250):
        centerX = True

    if (y + (h / 2)) < 200:
        # drone.move_up(20)
        centerY = False
    if (y + (h / 2)) > 300:
        # drone.move_down(20)
        centerY = False

    if ((y + (h / 2)) > 200) and ((y + (h / 2)) < 300):
        centerY = True

    if not centerX or not centerY:
        fullCenter = False
        print("Not centered")
    if centerX and centerY:
        fullCenter = True
        print("Centered")


# Finds objects in the image
def findObject(outputsValue, imgValue):
    hT, wT, cT = imgValue.shape
    bbox = []
    classIds = []
    confidence = []

    # Loop that prints the boxes in the image
    for output in outputsValue:
        for detection in output:
            scores = detection[5:]
            classId = np.argmax(scores)
            conf = scores[classId]
            if conf > minConfidence:
                w, h = int(detection[2] * wT), int(detection[3] * hT)
                x, y = int((detection[0] * wT) - w / 2), int((detection[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confidence.append(float(conf))
    indices = cv2.dnn.NMSBoxes(bbox, confidence, minConfidence, nms_threshold)

    # Loop that prints the boxes in the image
    # This only detects a person now instead of a bunch of other things
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        if classNames[classIds[i]].upper() == objectToRecognize:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confidence[i] * 100)}%', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 1)
            cv2.putText(img, f'X: {x + (w / 2)} Y: {y + (h / 2)}', (x, y - 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 1)
            # Draw a circle in the middle of the image to serve as a tracker
            checkCenter(x, y, w, h)
            if fullCenter:
                cv2.putText(img, "O", (round(x + (w / 2)), round(y + (h / 2))),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            else:
                cv2.putText(img, "X", (round(x + (w / 2)), round(y + (h / 2))),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# END OF VISION STUFF
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

if not webcam_mode:
    drone = tello.Tello()
    drone.connect()
    drone.streamoff()
    drone.streamon()
    print(drone.get_battery())
    # Keep debug_enabled as true, otherwise the drone will just slam into a wall XD
    while True:
        if not debug_enabled:
            if not takeoff:
                drone.takeoff()
                takeoff = True

        frame_read = drone.get_frame_read()
        finalFrame = frame_read.frame
        # Added try catch to ignore "ugly" frames
        try:
            img = cv2.resize(finalFrame, (width, height))

            # The DNN requires blob types to read camera output
            blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
            net.setInput(blob)

            layerNames = net.getLayerNames()
            outputNames = [layerNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            outputs = net.forward(outputNames)

            # Run the image detection
            findObject(outputs, img)

            cv2.imshow("Drone", img)

            # Press Q to close the program and destroy all windows (Might or might not work idk honestly)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                if takeoff:
                    drone.land()
                cv2.destroyAllWindows()
                break
        except Exception as e:
            e
else:
    while True:
        success, img = capture.read()
        # The DNN requires blob types to read camera output
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
        net.setInput(blob)
        layerNames = net.getLayerNames()
        outputNames = [layerNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        outputs = net.forward(outputNames)

        # Run the image detection
        findObject(outputs, img)

        # Show the camera image
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        # BOTTOM LEFT 0,400
        # BOTTOM RIGHT 500,400
        # TOP RIGHT 500, 0
        # TOP LEFT 0 ,0
