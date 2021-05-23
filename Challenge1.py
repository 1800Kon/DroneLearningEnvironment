from djitellopy import tello

from time import sleep


def challenge1Test():
    me = tello.Tello()

    me.connect()
    if me.get_battery() < 30:
        return "hello world! This is a test to see if the docker container is going to make the code work"

    me.takeoff()

    me.send_rc_control(0, 0, 50, 0)

    sleep(2)

    me.send_rc_control(0, 50, 0, 0)

    sleep(2)

    me.land()

