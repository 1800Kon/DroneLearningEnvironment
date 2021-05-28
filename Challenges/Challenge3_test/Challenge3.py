from djitellopy import tello
from time import sleep
# flake8: noqa

def challenge3Test():
    me = tello.Tello()

    me.connect()

    if me.get_battery() < 30:
        return False

    me.takeoff()

    me.send_rc_control(0, 0, 50, 0)

    sleep(2)

    me.flip

    sleep(2)

    me.land()

