def anagrams(word_1, word_2):
    word_1 = word_1.replace(" ", "").lower()
    word_2 = word_2.replace(" ", "").lower()
    if len(word_1) != len(word_2):
        return False
    for letter in word_1:
        if letter not in word_2:
            return False
    return True

def main():
    word_1 = input("Digite a primeira palavra: ")
    word_2 = input("Digite a segunda palavra: ")
    result = anagrams(word_1, word_2)
    print(result)

main()