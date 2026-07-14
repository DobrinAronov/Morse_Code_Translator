import time

import winsound


def decode_morse_code(morse_code: list, morse_alphabet_rev: dict) -> str:
    # Checking the morse code and prepare morse_code to decode!
    prepare_message_list = []
    for morse_letter in morse_code:
        for symbol in morse_letter:
            if symbol not in ('.', '-', ' ', '|'):
                return f'Attention, this code: "{morse_letter}" is wrong!!!'
        if '|' in morse_letter:
            # Subtracting '|' as a separate symbol from morse_code!
            while '|' in morse_letter:
                pipe_index = morse_letter.index('|')
                prepare_message_list.append(morse_letter[:pipe_index])
                prepare_message_list.append('|')
                if not '|' in morse_letter[pipe_index + 1:]:
                    prepare_message_list.append(morse_letter[pipe_index + 1:])
                morse_letter = morse_letter[pipe_index + 1:]
        else:
            prepare_message_list.append(morse_letter)

    # Decode Morse code message
    output_message = ''

    for morse_letter in prepare_message_list:
        if morse_letter == '|':
            output_message += ' '
        else:
            if morse_letter in morse_alphabet_rev.keys():
                output_message += morse_alphabet_rev[morse_letter]
    return output_message


def coding_text_message(text_for_coding: str, morse_alphabet: dict) -> str:
    output_morse_code = ''

    for idx in range(len(text_for_coding)):
        symbol = text_for_coding[idx]
        if symbol == ' ':
            output_morse_code += '|'
        else:
            # Checking for next symbol
            if (idx + 1) < len(text_for_coding):
                next_symbol = text_for_coding[idx + 1]
                if symbol.upper() in morse_alphabet.keys():
                    if next_symbol != ' ':
                        output_morse_code += morse_alphabet[symbol.upper()] + ' '
                    else:
                        output_morse_code += morse_alphabet[symbol.upper()]
            elif idx == len(text_for_coding) - 1:
                output_morse_code += morse_alphabet[symbol.upper()]

    return output_morse_code


def sound(morse_code: str):
    # Adding the "p" symbol between Morse code characters into one letter.
    message_for_send = ''

    for morse_letter in morse_code:
        if morse_letter == ' ' or morse_letter == '|':
            message_for_send += morse_letter
        else:
            for index in range(len(morse_letter)):
                if index < len(morse_letter) - 1:
                    message_for_send += morse_letter[index] + 'p'
                else:
                    message_for_send += morse_letter[index]

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

while command != "end":

    if command == 'D':
        morse_codes_message = input("Please, enter Morse code: ").split()
        text_message = decode_morse_code(morse_codes_message, morse_code_alphabet_reverse)
        print(f"Decoded message:\n{text_message}")

    elif command == 'C':
        text = input("Please enter a text message in Latin!\n")
        code_message = coding_text_message(text, morse_code_alphabet)
        print(f"Morse code:\n{code_message}\n")
        # If the user wants to hear the message
        sound_command = input('Please, press "Y" if you want to hear the message\n'
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
