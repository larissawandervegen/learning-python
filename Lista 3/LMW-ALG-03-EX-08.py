nota = input("Digite a nota:")
num = int(input("Digite o número da nota:"))

if nota ==  "C" or nota == "c":
    frequencia = 261.63 / 2 **(4 - num)
    print(f"A frequência é {frequencia}.")

elif nota == "D" or nota == "d":
    frequencia = 293.66/(2**(4-num))
    print(f"A frequência é {frequencia}.")

elif nota == "E" or nota == "e":
    frequencia = 329.63/(2**(4-num))
    print(f"A frequência é {frequencia}.")

elif nota == "F" or nota == "f":
    frequencia = 349.23/(2**(4-num))
    print(f"A frequência é {frequencia}.")

elif nota == "G" or nota == "g":
    frequencia = 392.00/(2**(4-num))
    print(f"A frequência é {frequencia}.")

elif nota == "A" or nota == "a":
    frequencia = 440.00/(2**(4-num))
    print(f"A frequência é {frequencia}.")
    
elif nota == "B" or nota == "b":
    frequencia = 492.88/(2**(4-num))
    print(f"A frequência é {frequencia}.")
