# import modules from Pyfirmata

from pyfirmata import Arduino, util, INPUT

# import inbuilt time module

import time

# initial configurations

board = Arduino("COM5")
b_pin = 2
board.digital[b_pin].mode = INPUT


it = util . Iterator(board)
it . start()

board.analog[b_pin].enable_reporting()

while True:
    print("READ VALUE")
    b_val = board.digital[b_pin].read()  # read the value
    print('Analog value :', b_val)
    time.sleep(1)
