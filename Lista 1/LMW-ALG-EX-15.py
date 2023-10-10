import math

l = int(input("Qual é o comprimento do lado? "))
n = int(input("Qual é o número de lados? "))

area = (n * l**2)/(4 * math.tan(math.pi/n))

print("A área é igual a", area)