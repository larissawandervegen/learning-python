numero = int(input("Digite um número inteiro:"))
fator = 2
while fator <= numero:
    if numero % fator == 0:
        fatoracao = numero / fator
    print(fator)

