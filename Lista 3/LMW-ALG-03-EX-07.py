volume = float(input("Digite um nível de volume em decibéis:"))

if volume < 40 or volume > 130:
    print("O nível informado não é válido!")
else:
    if volume == 130:
        print("O nível de volume inserido corresponde a: britadeira.")
    elif volume == 106:
        print("O nível de volume inserido corresponde a: cortador de grama.")
    elif volume == 70:
        print("O nível de volume inserido corresponde a: despertador.")
    elif volume == 40:
        print("O nível de volume inserido corresponde a: sala sileciosa.")
    elif volume > 106  and volume < 130:
        print("O nível de volume inserido está entre: britadeira e cortador de grama.")
    elif volume > 70 and volume < 106:
        print("O nível de volume inserido está entre: cortador de grama e despertador.")
    elif volume  > 40 and volume < 70:
         print("O nível de volume inserido está entre: despertador e sala sileciosa.")

