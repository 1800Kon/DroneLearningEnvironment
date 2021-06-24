#DockerFile with the challenges

FROM python:3.9

COPY Tello_Library/tello.py .
COPY requirements.txt ./
COPY Challenge/Challenges.py .
#Upadate the image into the latest packages
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install djitellopy
#CMD to run the docker container
CMD [ "python","Challenges.py"]