#this are comments in the docker file. With the comments I will explain how the docker file should work
#and what should be included.

#We first need to add the image we want to use for our different docker images. In this case, pyhton 3.9.0

FROM python:3

COPY Tello_Library/tello.py .
COPY requirements.txt ./
COPY Challenge/Challenges.py .

ENV DOCKER_BUILDKIT=1
ENV BUILDKIT_PROGRESS=plain
ENV DOCKER_CLI_EXPERIMENTAL=enabled

ARG BUILDX_URL=https://github.com/docker/buildx/releases/download/v0.4.2/buildx-v0.4.2.linux-amd64

RUN mkdir -p $HOME/.docker/cli-plugins && \
wget -O $HOME/.docker/cli-plugins/docker-buildx $BUILDX_URL && \
chmod a+x $HOME/.docker/cli-plugins/docker-buildx


#Upadate the image into the latest packages
 
RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y 
RUN pip install djitellopy 
#RUN pip install -r requirements.txt && apt-get update && pip install djitellopy && pip install opencv-python --no-cache-dir
#CMD to run the docker container
CMD [ "python","Challenges.py"]