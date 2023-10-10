import string

def anagrams(phrase_1, phrase_2):
    phrase_1 = phrase_1.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    phrase_2 = phrase_2.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    if len(phrase_1) != len(phrase_2):
        return False
    for letter in phrase_1:
        if letter not in phrase_2:
            return False
    return True

def main():
    phrase_1 = input("Digite a primeira frase: ")
    phrase_2 = input("Digite a segunda frase: ")
    result = anagrams(phrase_1, phrase_2)
    print(result)
    
main()