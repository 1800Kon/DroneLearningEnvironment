import cv2
import numpy as np

# The camera to use
capture = cv2.VideoCapture(0)
# Width and height of the blob target
whT = 320

# List which stores all the objects you can recognize
classesFile = 'coco.names'
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfiguration = 'yolov3-320.cfg'
modelWeights = 'yolov3.weights'

net = cv2.dnn.readNet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Loop to show the camera feed
while True:
    success, img = capture.read()
    # The DNN requires blob types to read camera output
    blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(outputNames)
    print(len(outputs))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
