from time import sleep

from djitellopy import tello

me = tello.Tello()

me.connect()

print(me.get_battery())

me.takeoff()

sleep(2)

me.send_rc_control(0, 0, 0, 50)

sleep(2)

me.land()
