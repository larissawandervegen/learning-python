lado_1 = float(input("Digitie o comprimento do primeiro lado:"))
lado_2 = float(input("Digitie o comprimento do segundo lado:"))
lado_3 = float(input("Digitie o comprimento do terceiro lado:"))

if lado_1 == lado_2 == lado_3:
    tipo = "equilátero"
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    tipo = "isóceles"
else:
    tipo = "escaleno"

print(f"O trinângulo é um {tipo}.")

