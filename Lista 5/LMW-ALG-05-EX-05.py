def ordinal_num(number):
    if number < 1 or number > 12:
        return ""

    ordinals = ["primeiro", "segundo", "terceiro", "quarto", "quinto",
                "sexto", "sétimo", "oitavo", "nono", "décimo", "onze", "doze"]

    return ordinals[number-1]

for number in range(1, 13):
    ordinal = ordinal_num(number)
    if ordinal:
        print(f"{number}º: {ordinal}")
    else:
        print(f"{number} está fora do intervalo de 1 a 12.")