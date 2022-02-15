# Python program to implement Morse Code Translator


# Dictionary representing the morse code chart

MORSE_CODE_DICT = {'.-': 'A', '-...': 'B',
                   '-.-.': 'C', '-..': 'D', '.': 'E',
                   '..-.': 'F', '--.': 'G', '....': 'H',
                   '..': 'I', '.---': 'J', '-.-': 'K',
                   '.-..': 'L', '--': 'M', '-.': 'N',
                   '---': 'O', '.--.': 'P', '--.-': 'Q',
                   '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W',
                   '-..-': 'X', '-.--': 'Y', '--..': 'Z',
                   '.----': '1', '..---': '2', '...--': '3',
                   '....-': '4', '.....': '5', '-....': '6',
                   '--...': '7', '---..': '8', '----.': '9',
                   '-----': '0', '--..--': ', ', '.-.-.-': '.',
                   '..--..': '?', '-..-.': '/', '-....-': '-',
                   '-.--.': '(', '-.--.-': ')'}


# Decrypt the string

def decrypt(message):

    code = ''
    temp_morse = ''
    for letter in message:

        # checks for space
        if letter != ' ':
            temp_morse = temp_morse + str(letter)
            print(temp_morse)

        else:
            code = code + str(MORSE_CODE_DICT.get(temp_morse, ''))
            temp_morse = ''

    return code
