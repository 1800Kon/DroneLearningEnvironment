from djitellopy import tello

from time import sleep

def challenge1():
    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    me.send_rc_control(0, 0, 50, 0)

    sleep(2)

    me.send_rc_control(0, 50, 0, 0)

    sleep(2)

    me.land()

def challenge2():
    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.send_rc_control(0, 0, 50, 0)

    sleep(2)

    me.send_rc_control(0, 0, 0, 50)

    sleep(2)

    me.land()

def challenge3():
    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    me.send_rc_control(0, 0, 50, 0)

    sleep(2)

    me.flip

    sleep(2)

    me.land()

def challenge4():
    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    me.send_rc_control(0, 0, 50, 0)
    """up 50"""
    sleep(2)

    me.send_rc_control(0, 25, 0, 0)
    """forward 25"""

    sleep(2)

    me.send_rc_control(0, 0, 0, 50)

    """turn clockwise 50"""

    sleep(2)

    me.send_rc_control(0, 50, 0, 0)

    """forward 50"""

    sleep(2)

    me.send_rc_control(0, 0, 0, 50)

    """turn clockwise 50"""

    sleep(2)

    me.send_rc_control(0, 25, 0, 0)

    """forward 25"""

    sleep(2)

    me.send_rc_control(0, 0, 0, 50)
    """turn clock wise 50"""

    sleep(2)

    me.send_rc_control(0, 50, 0, 0)
    """forward 50"""

    sleep(2)

    me.send_rc_control()

    me.land()

def challenge5():
    me.connect()

    print(me.get_battery())

    me.takeoff()

    me.send_rc_control(0, 0, 50, 0)

    sleep(2)

    me.flip_back()

    sleep(2)

    me.land()