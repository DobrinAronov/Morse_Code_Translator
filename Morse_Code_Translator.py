import time

import winsound


def check_morse_code(test_code: str) -> tuple[bool, list, str]:
    test_code_list = test_code.split()
    for test_letter in test_code_list:
        for symbol in test_letter:
            if symbol not in ('.', '-', ' ', '|'):
                return False, [], f'Attention, this Morse code: "{test_letter}" is wrong!!!'
    return True, test_code_list, ''


def decode_morse_code(morse_code: str, morse_alphabet_rev: dict) -> str | None:
    is_morse_code, morse_code_list, message = check_morse_code(morse_code)
    # Checking and preparing morse_code for decode!
    if is_morse_code:
        prepared_message_list = []
        for morse_letter in morse_code_list:
            if '|' in morse_letter:
                # Subtracting '|' as a separate symbol from morse_code!
                while '|' in morse_letter:
                    pipe_index = morse_letter.index('|')
                    prepared_message_list.append(morse_letter[:pipe_index])
                    prepared_message_list.append('|')
                    if not '|' in morse_letter[pipe_index + 1:]:
                        prepared_message_list.append(morse_letter[pipe_index + 1:])
                    morse_letter = morse_letter[pipe_index + 1:]
            else:
                prepared_message_list.append(morse_letter)

        # Decode Morse code message
        output_message = ''

        for morse_letter in prepared_message_list:
            if morse_letter == '|':
                output_message += ' '
            else:
                if morse_letter in morse_alphabet_rev.keys():
                    output_message += morse_alphabet_rev[morse_letter]
        return output_message
    return message


def coding_text_message(text_for_coding: str, morse_alphabet: dict) -> tuple[bool, str]:
    output_morse_code = ''

    for idx in range(len(text_for_coding)):
        symbol = text_for_coding[idx].upper()
        if symbol == ' ':
            output_morse_code += '|'
        else:
            # Checking text symbol
            if symbol not in morse_alphabet.keys():
                return True, f'ERROR: the program does not support such a symbol: "{symbol}"!'
            is_morse_code, _, _ = check_morse_code(text_for_coding)
            if is_morse_code:
                return True, f'ERROR: This is Morse code"!'

            # Checking for next symbol
            if (idx + 1) < len(text_for_coding):
                next_symbol = text_for_coding[idx + 1]
                if next_symbol != ' ':
                    output_morse_code += morse_alphabet[symbol] + ' '
                else:
                    output_morse_code += morse_alphabet[symbol]
            elif idx == len(text_for_coding) - 1:
                output_morse_code += morse_alphabet[symbol]

    return False, output_morse_code


def sound(morse_code: str):
    # Adding the "p" symbol between Morse code characters into one letter.
    message_for_send = ''

    for idx in range(len(morse_code)):
        symbol = morse_code[idx]
        if idx == len(morse_code) - 1 or symbol == ' ' or symbol == '|':
            message_for_send += symbol
        elif (idx + 1) < len(morse_code):
            next_symbol = morse_code[idx + 1]
            if next_symbol == ' ' or next_symbol == '|':
                message_for_send += symbol
            else:
                message_for_send += symbol + 'p'

    # With the unit_time variable we can adjust the speed of message transmission!
    unit_time = 100  # in mS !!!
    pause_time = unit_time / 1000  # 1 unit_time in seconds !!!

    # Sound message
    for symbol in message_for_send:
        if symbol == '.':
            # point - frequency 600 Hz, duration 1 unit_time
            winsound.Beep(600, unit_time)
        elif symbol == '-':
            # dash - frequency 600 Hz, duration 3 unit_time
            winsound.Beep(600, 3 * unit_time)

        # I replace the "p" symbol with a pause,
        # to separate the Morse code characters into one letter.

        elif symbol == 'p':
            # duration pause between characters 1 unit_time (in seconds)!
            time.sleep(pause_time)
        elif symbol == ' ':
            # duration pause between letters 3 pause_time
            time.sleep(3 * pause_time)
        elif symbol == '|':
            # duration pause between words 7 pause_time
            time.sleep(7 * pause_time)


morse_code_alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                       'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                       'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '—–',
                       '1': '.—-', '2': '..—', '3': '...–', '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
                       "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                       ':': '---...', ';': '-.-.-.', '=': '-...-', '-': '-....-', '_': '..--.-', '"': '.-..-.',
                       '$': '...-..-', '@': '.--.-.'
                       }

morse_code_alphabet_reverse = {value: key for key, value in morse_code_alphabet.items()}

command = input("\nPlease, select an action:\n"
                'Press "C" to code text message\n'
                'Press "D" to decode Morse code\n'
                'For escape enter "End"\n').upper()

while command != "END":

    if command == 'D':
        morse_codes_message = input("Please, enter Morse code: ")
        text_message = decode_morse_code(morse_codes_message, morse_code_alphabet_reverse)
        print(f"Decoded message:\n{text_message}")

    elif command == 'C':
        text = input("Please enter a text message in Latin!\n")
        error, code_message = coding_text_message(text, morse_code_alphabet)
        if error:
            print(code_message)
        else:
            print(f"Morse code:\n{code_message}\n")
            # If the user wants to hear the message
            sound_command = input('Please, press "Y", if you want to hear the message\n'
                                  'press any key to continue\n'
                                  'end press "Enter": ').upper()
            if sound_command == 'Y':
                sound(code_message)

    else:
        print("Wrong command!")

    command = input("\nPlease, select an action:\n"
                    'Press "C" to code text message\n'
                    'Press "D" to decode Morse code\n'
                    'For escape enter "End"\n').upper()
