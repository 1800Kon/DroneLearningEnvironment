#this are comments in the docker file. With the comments I will explain how the docker file should work
#and what should be included.

#We first need to add the image we want to use for our different docker images. In this case, pyhton 3.9.0
FROM python:3

RUN pip install --no-cache-dir -r requirements.txt
#Upadate the image into the latest packages
RUN apt-get update

COPY requirements.txt ./


#CMD to run the docker container
CMD [ "python","DroneLearningEnvironment/Challenge1.py"]