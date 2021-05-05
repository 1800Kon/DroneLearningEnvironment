import numpy as np
from djitellopy import tello
import cv2

# Variables
whT = 320
width = 720
height = 720
debug_enabled = True
minConfidence = 0.5
nms_threshold = 0.3
modelConfiguration = 'yolov3-320.cfg'
modelWeights = 'yolov3.weights'
classesFile = 'coco.names'
classNames = []
takeoff = False

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
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confidence[i] * 100)}%', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 1)


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# END OF VISION STUFF
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


drone = tello.Tello()
drone.connect()
drone.streamon()
print(drone.get_battery())

# Keep debug_enabled as true, otherwise the drone will just slam into a wall XD
while True:
    if not debug_enabled:
        if not takeoff:
            drone.takeoff()
            takeoff = True

    frame_read = drone.get_frame_read()
    frame = frame_read.frame
    img = cv2.resize(frame, (width, height))

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

# https://www.youtube.com/watch?v=S7WSBntj3IA
