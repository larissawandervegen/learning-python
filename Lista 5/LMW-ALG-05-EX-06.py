def centralize_string(word, lenth):
    espaces = ""

    for void in range(lenth):
        espaces += " "

    centralized_string = espaces + word
    return centralized_string

word = input("Digite a palavra que quer centralizar: ")
lenth = int(input("Digite a largura que palavra centralizada irá ter: "))

print(centralize_string(word, lenth))