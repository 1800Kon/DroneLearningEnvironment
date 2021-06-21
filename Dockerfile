#this are comments in the docker file. With the comments I will explain how the docker file should work
#and what should be included.

#We first need to add the image we want to use for our different docker images. In this case, pyhton 3.9.0

FROM python:3

COPY Tello_Library/tello.py .
COPY requirements.txt ./
COPY Challenge/Challenges.py .

#Upadate the image into the latest packages
 
RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y 
RUN pip install djitellopy 
#RUN pip install -r requirements.txt && apt-get update && pip install djitellopy && pip install opencv-python --no-cache-dir
#CMD to run the docker container
CMD [ "python","Challenges.py"]