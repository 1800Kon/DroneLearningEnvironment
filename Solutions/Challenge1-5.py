from djitellopy import tello

from time import sleep
# flake8: noqa
def challenge1():

    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    sleep(1)

    me.send_rc_control(0, 50, 0, 0)

    sleep(2)

    me.send_rc_control(0, -50, 0, 0)

    sleep(2)

    me.land()

def challenge2():

    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    sleep(2)

    me.send_rc_control(0, 0, 0, 50)

    sleep(2)

    me.land()

def challenge3():

    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    sleep(2)

    me.flip()

    sleep(2)

    me.land()

def challenge4():
    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    me.send_rc_control(0, 50, 0, 0)
    """forward 25"""
    sleep(3)

    me.send_rc_control(50, 0, 0, 0)
    sleep(1)

    me.send_rc_control(0, -40, 0, 0)
    sleep(3)

    me.send_rc_control(-40, 0, 0, 0)

    sleep(1)

    me.land()

def challenge5():

    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    sleep(1)

    me.flip_back()

    sleep(1)

    me.flip_forward()

    sleep(1)

    me.flip_left()

    sleep(1)

    me.flip_right()

    sleep(1)

    me.land()

def challenge6():

    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    sleep(1)

    me.send_rc_control(0, 50, 0, 25)

    sleep(4)

    me.land()

def challenge7():

    me = tello.Tello()

    me.connect()

    print(me.get_battery())

    me.takeoff()

    me.send_rc_control(0,50,0,25)

    sleep(2)

    me.send_rc_control(0,50,0,-25)

    sleep(2)

    me.land()

challenge1()