from microbit import *


uart.init(9600)

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    msg = str(x) + ',' + str(y) + '\n'
    uart.write(msg)
    sleep(50)
