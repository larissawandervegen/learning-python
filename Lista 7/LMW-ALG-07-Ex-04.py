def translate_morse(msg):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'}
    translated_msg = ''
    for character in msg:
        if character.isalnum():
            character_up = character.upper()
            if character_up in morse_code:
                code = morse_code[character_up]
                translated_msg += code + ' '
    return translated_msg.strip()

def main():
    msg = input("Digite uma mensagem: ")
    tramslated_msg = translate_morse(msg)
    print(tramslated_msg)

main()
