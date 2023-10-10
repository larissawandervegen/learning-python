letra = input("Digite a letra da posição:")
num = int(input("Digite o número da posição:"))

resultado = num % 2 

if resultado == 0:
    if letra == "b" or  letra == "d" or letra == "f" or letra == "h":
        print("O quadrado é preto.")
    elif letra == "a" or  letra == "c" or letra == "e" or letra == "g" :
        print("O quadrado é branco.")
else:
    if letra == "a" or  letra == "c" or letra == "e" or letra == "g":
        print("O quadrado é preto.")
    elif letra == "b" or  letra == "d" or letra == "f" or letra == "h":
        print("O quadrado é branco.")