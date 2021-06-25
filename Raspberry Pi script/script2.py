#!/usr/bin/python3.7
import os
import sys
import docker
import time
import socket
from djitellopy import tello
time.sleep(5)
client = docker.from_env()
client.login(username="sandersass", password="sandersass")
os.system("sudo docker pull pepeloperena/dockertest:testtag")
os.system(r"/home/pi/Desktop/realvnc-vncserveui-user.desktop")
os.system("sudo docker images")
os.system("sudo docker run hello-world")
os.system("sudo iwconfig")
# TELLO-80D485
me = tello.Tello()
me.connect()
print(me.get_battery)
#me.takeoff()