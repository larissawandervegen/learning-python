#Escreva uma função que recebe como parâmetros os comprimentos dos dois
#lados menores de um triângulo retângulo. A função deve retornar como resultado o
import math 
def calculate_h (a, b):
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    return hypotenuse

def main():
    a = int(input("Digite o comprimento do primeiro lado:"))
    b = int(input("Digite o comprimento do segundo lado:"))
    hypotenuse = calculate_h(a, b)
    print("A hipotenusa é", hypotenuse)

main()