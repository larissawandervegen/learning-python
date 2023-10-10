idade = int(input("Digite a idade cronológica do cachorro: "))

if idade < 0:
    print("Erro: a idade deve ser um número positivo.")
else:
    if idade <= 2:
        idade_c = idade * 10.5
    else:
        idade_c = 21 + (idade - 2) * 4
    print(f"A idade canina do cachorro é {idade_c} anos.")

