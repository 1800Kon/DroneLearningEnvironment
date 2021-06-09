from djitellopy import tello

from time import sleep

me = tello.Tello()

me.connect()
print('test 1')
me.takeoff()

me.send_rc_control(0, 0, 50, 0)

sleep(2)
print('test 2')
me.send_rc_control(0, 50, 0, 0)
sleep(2)
me.send_rc_control(0, 50, 0, 0)

me.land()
