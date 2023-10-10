from unidecode import unidecode
import re

def palindrome(characters):
    def erase_characters(characters):
        chr_w_accent = unidecode(characters)
        chr_w_punctuation = re.sub(r'[^a-zA-Z0-9]', '', chr_w_accent)
        clean_characters  = chr_w_punctuation.lower().replace(" ", "")
        return clean_characters 
    

    def checking(characters):
        if len(characters) <= 1:
            return "É um palíndromo"

        if characters[0] == characters[-1]:
            return checking(characters[1:-1])
        else:
            return "Não é um palíndromo"

    clean_characters = erase_characters(characters)
    return checking(clean_characters )

def main():
    characters = input("Digite uma palavra ou frase:")
    print(palindrome(characters))
main()