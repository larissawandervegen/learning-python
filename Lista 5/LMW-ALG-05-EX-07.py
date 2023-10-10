def form_triangle(side_1, side_2, side_3):
    if side_1 > side_2 + side_3 or side_2 > side_1 + side_3 or side_3 > side_1 + side_2:
        return False
    else:
        return True
    
side_1 = int(input("Digite o comprimento do primeiro lado:"))
side_2 = int(input("Digite o comprimento do segundo lado:"))
side_3 = int(input("Digite o comprimento do terceiro lado:"))

if form_triangle(side_1, side_2, side_3):
    print("Com os comprimentos inseridos é possível formar um triângulo!")
else:
    print("Não é possível formar um triângulo com os comprimentos inseridos!")