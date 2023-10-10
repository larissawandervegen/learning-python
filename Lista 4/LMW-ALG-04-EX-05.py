soma = 0

while True:
    idade = input("Digite a idade dos visitantes: ")
    if idade == "":
        break
    idade = int(idade)
    if idade <= 2:
        valor = 0
    elif idade <= 12: 
        valor = 14
    elif idade >= 65:
        valor = 18
    else:
        valor = 23
    soma = soma + valor
print("O preço total das entradas é de R${:.2f}".format(valor))
#{:2f}