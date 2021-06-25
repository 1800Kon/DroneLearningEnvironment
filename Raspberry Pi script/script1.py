#!/usr/bin/python3.7
import os
import sys
import docker
import time
time.sleep(5)
client = docker.from_env()
client.login(username="sandersass", password="sandersass")
os.system("sudo docker pull pepeloperena/dockertest:testtag")
os.system(r"/home/pi/Desktop/realvnc-vncserveui-user.desktop")
os.system("sudo docker images")
os.system("sudo docker run hello-world")
os.system("sudo iwconfig")
print ("Script Worked!")