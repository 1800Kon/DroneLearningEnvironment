#this are comments in the docker file. With the comments I will explain how the docker file should work
#and what should be included.

#We first need to add the image we want to use for our different docker images. In this case, pyhton 3.9.0
FROM python:lastest

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
#Upadate the image into the latest packages
RUN apt-get update

#expose a port to run the docker container
EXPOSE 80

#CMD to run the docker container
CMD["python","Challenges/Challenge1_test/Challenge1.py"]