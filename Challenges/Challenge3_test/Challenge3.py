from djitellopy import tello
from time import sleep


def challenge3Test():
    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    me.send_rc_control(0, 0, 50, 0)

    sleep(2)

    me.flip

    sleep(2)

    me.land()

