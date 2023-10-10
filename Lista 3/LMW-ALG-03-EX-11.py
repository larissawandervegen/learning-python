import math

def calcular_raizes(a, b, c):
    # calcula o discriminante
    delta = b*2 - 4ac

    # verifica quantas raízes a função possui
    if delta < 0:
        print("A função não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2a)
        print("A função possui uma raiz real: {:.2f}".format(raiz))
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2a)
        raiz2 = (-b - math.sqrt(delta)) / (2a)
        print("A função possui duas raízes reais: {:.2f} e {:.2f}".format(raiz1, raiz2))

# solicita os valores de a, b e c ao usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# chama a função para calcular as raízes
calcular_raizes(a, b, c)