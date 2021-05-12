from djitellopy import tello

from time import sleep


def challenge2Test():
    me = tello.Tello()

    me.connect()

    if me.get_battery() < 30:
        return True

    me.takeoff()

    me.send_rc_control(0, 0, 50, 0)

    sleep(2)

    me.send_rc_control(0, 0, 0, 50)

    sleep(2)

    me.land()