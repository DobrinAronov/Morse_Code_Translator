import time

import winsound


def morse_code_translator(morse_code: list, morse_alphabet: dict) -> str:
    # Checking the morse code
    for morse_letter in morse_code:
        for sign in morse_letter:
            if sign not in ('.', '-', '|', ' '):
                return "Това не е морзов код !!!"

    list_with_morse_codes = []
    # Subtracting '|' as a separate symbol from morse_code!
    for morse_letter in morse_code:
        if '|' in morse_letter:
            while '|' in morse_letter:
                pipe_index = morse_letter.index('|')
                list_with_morse_codes.append(morse_letter[:pipe_index])
                list_with_morse_codes.append('|')
                if not '|' in morse_letter[pipe_index + 1:]:
                    list_with_morse_codes.append(morse_letter[pipe_index + 1:])
                morse_letter = morse_letter[pipe_index + 1:]
        else:
            list_with_morse_codes.append(morse_letter)

    output_message = ''
    # Decoding the morse code
    for morse_letter in list_with_morse_codes:
        if morse_letter == '|':
            output_message += ' '
        else:
            for letter, code in morse_alphabet.items():
                if morse_letter == code:
                    output_message += letter
                    break
    return output_message


def message_morse_coding(text_for_coding: str, morse_alphabet: dict) -> str:
    output_morse_code = ''

    for idx in range(len(text_for_coding)):
        symbol = text_for_coding[idx]
        if symbol == ' ':
            output_morse_code += '|'
        else:
            if (idx + 1) < len(text_for_coding):
                next_symbol = text_for_coding[idx + 1]
                if next_symbol != ' ':
                    if symbol.upper() in morse_alphabet:
                        output_morse_code += morse_alphabet[symbol.upper()] + ' '
                else:
                    if symbol.upper() in morse_alphabet:
                        output_morse_code += morse_alphabet[symbol.upper()]
            elif idx == len(text_for_coding) - 1:
                output_morse_code += morse_alphabet[symbol.upper()]

    return output_morse_code


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
    # Sound message
    # With the unit_time variable we can adjust the speed of message transmission!
    unit_time = 100  # in mS !!!
    pause_time = unit_time / 1000  # 1 unit_time in seconds !!!
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
                       '7': '--...', '8': '---..', '9': '----.'
                       }

command = input("\nМоля, изберете действие:\n"
                "'C' за кодиране на съобщение\n"
                "'D' за декодиране на съобщение\n"
                "За изход от програмата въведете End\n").lower()

while command != "end":

    if command == 'd':
        morse_codes_message = input("Моля, въведете морзов код: ").split()
        text_message = morse_code_translator(morse_codes_message, morse_code_alphabet)
        print(f"Декодирано съобщение:\n{text_message}")

    elif command == 'c':
        text = input("Моля, въведете текстово съобщение на латиница!\n")
        code_message = message_morse_coding(text, morse_code_alphabet)
        print(f"Морзов код:\n{code_message}\n")
        # If the user wants to hear the message
        sound_command = input("Моля, въведете Y ако искате да чуете съобщението\n"
                              "или произволен клавиш за да продължите\n"
                              "Потвърдете с Enter: ").lower()
        if sound_command == 'y':
            sound(code_message)

    else:
        print("Грешна команда!")

    command = input("\nМоля, изберете действие:\n"
                    "'C' за кодиране на съобщение\n"
                    "'D' за декодиране на съобщение\n"
                    "За изход от програмата въведете End\n").lower()

