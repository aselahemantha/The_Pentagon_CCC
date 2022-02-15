# import modules from Pyfirmata

from pyfirmata import Arduino, util, INPUT
import morse_code

# import inbuilt time module

import time

# initial configurations

board = Arduino("COM5")
ldr_pin = 0
board.analog[ldr_pin]. mode = INPUT
button_pin = 9
board.digital[button_pin].mode = INPUT

# start the utilization service
# this service will handle communication overflows while communicating with the Arduino board via USB intrface .

it = util . Iterator(board)
it . start()

board.analog[ldr_pin].enable_reporting()


def get_time(ldr_val):
    global count_value

    if ldr_val > 0.7:
        count_value = count_value + 1
        print(count_value)
    else:
        count_value = 0
    return get_morse(count_value)


def get_morse(count_value):
    temp_morse = ''
    if count_value >= 2:
        temp_morse = temp_morse + '-'
    elif 1 <= count_value < 2:
        temp_morse = temp_morse + '.'
    else:
        temp_morse = temp_morse + ' '
    return temp_morse


count_value = 0
morse = ''


while True:
    print("READ VALUE")
    ldr_val = board.analog[ldr_pin].read()  # read the value
    if ldr_val == None:
        ldr_val = 0
    print('Analog value :', ldr_val)
    time.sleep(1)

    button_value = board.digital[button_pin].read()
    print(button_value)

    if button_value == False:
        morse = morse + get_time(ldr_val)
        print(morse)
    else:
        print(morse_code.decrypt(morse))
        break
