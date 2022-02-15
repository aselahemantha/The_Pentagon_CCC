import pyfirmata
from time import sleep
import time

board = pyfirmata.Arduino('COM4')
pin = board.get_pin('a:0:i')

it = pyfirmata.util.Iterator(board)
it.start()

while True:
    analog_value = pin.read()
    print(analog_value)
    if isinstance(analog_value, float):
        if float(analog_value) > 0.9:
            fire = 1
            print('Fire Alarm On')
        else:
            fire = 0
            print('Fire Alarm Off')
        print(fire)
    time.sleep(1)


