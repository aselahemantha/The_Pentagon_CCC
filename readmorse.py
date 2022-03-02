# import modules from Pyfirmata

from turtle import st
from pyfirmata import Arduino, util, INPUT
import morse_code

# import inbuilt time module

import time

# initial configurations

board = Arduino("COM5")
ldr_pin = 0
board.analog[ldr_pin].mode = INPUT
button_pin = 9
board.digital[button_pin].mode = INPUT

# start the utilization service
# this service will handle communication overflows while communicating with the Arduino board via USB intrface .

it = util . Iterator(board)
it . start()

board.analog[ldr_pin].enable_reporting()

'''
def get_time(ldr_val):

    global count_value

    if ldr_val > 0.1:
        start = time.process_time()
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
'''
ldr_on = False
vaule_list = []
morse = ''


while True:
    print("READ VALUE")
    ldr_val = board.analog[ldr_pin].read()  # read the value
    if ldr_val == None:
        ldr_val = 0

    if isinstance(ldr_val, float):
        print('Analog value :', ldr_val)

        if ldr_val > 0.1:
            vaule_list.append(ldr_val)

            '''
            if ldr_on == False:
                vaule_list.append(ldr_val)
                ldr_on = True
            '''
        else:
            if 6 >= len(vaule_list) >= 3:
                morse = morse + '-'
            elif 3 > len(vaule_list) >= 1:
                morse = morse + '.'
            else:
                morse = morse + ' '

            vaule_list = []

            '''
            if ldr_on == True:
                print(len(vaule_list))
                ldr_on = False
            '''
        print(morse)

        time.sleep(1)

'''
morse = ''
pre_val = 0
count_value = 0
ldr_on = False
start, end = time.time(), time.time()

while True:
    print("READ VALUE")
    ldr_val = board.analog[ldr_pin].read()  # read the value
    if ldr_val == None:
        ldr_val = 0

    if isinstance(ldr_val, float):
        print('Analog value :', ldr_val)

        if ldr_val > 0.1:
            if ldr_on == False:
                start = time.time()
                ldr_on = True
        else:
            if ldr_on == True:
                end = time.time()
                ldr_on = False

        time_duration = abs(end-start)
        print(time_duration)

        if 2 < time_duration < 4:
            morse = morse + '-'
        elif 0.5 < time_duration < 2:
            morse = morse + '.'
        else:
            morse = morse + ' '

        print(morse)
        start, end = time.time(), time.time()
        time.sleep(0.5)

'''
'''
        morse = morse + get_time(ldr_val)
        print(morse)
        print(morse_code.decrypt(morse))
        time.sleep(1)

        if button_value == False:
            morse = morse + get_time(ldr_val)
            print(morse)
        else:
            print(morse_code.decrypt(morse))
            break
'''
