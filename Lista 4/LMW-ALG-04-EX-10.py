palavra = input("Digite a palavra:")

for letra in palavra:
    palavra_invertida = palavra [::-1]
    if palavra == palavra_invertida:
        print("A palavra", palavra, "é um palíndromo.")
    else:
        print("A palavra", palavra, "não é um palíndromo.")
    