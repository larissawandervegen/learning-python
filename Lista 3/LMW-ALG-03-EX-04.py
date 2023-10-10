lados = int(input("Digite a quantidade de lados do polígono:"))

if lados < 3 or lados > 10:
    print("A quantidade de lados é inválida!")
else:
    if lados == 3:
        nome = "triângulo"
    elif lados == 4:
        nome = "quadrângulo"
    elif lados == 5:
        nome = "pentágono"
    elif lados == 6:
        nome = "hexágono"
    elif lados == 7:
        nome = "heptágono"
    elif lados == 8:
        nome = "octágono"
    elif lados == 9:
        nome = "eneágono"
    else:
        nome = "decágono"
    print(f"O polígono com {lados} chama-se {nome}.")