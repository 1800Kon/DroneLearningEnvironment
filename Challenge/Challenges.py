from time import sleep

from djitellopy import tello

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
sleep(2)

me.land()
