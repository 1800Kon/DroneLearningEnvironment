#this are comments in the docker file. With the comments I will explain how the docker file should work
#and what should be included.

#We first need to add the image we want to use for our different docker images. In this case, pyhton 3.9.0
FROM python:lastest

#Upadate the image into the lastest packages
RUN apt-get update

#expose a port to run the docker container
EXPOSE 80

#CMD to run the docker container
CMD["py.test"]
#py.test is incorrect should be changed. It does not work.