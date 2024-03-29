from time import sleep

from djitellopy import tello

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
