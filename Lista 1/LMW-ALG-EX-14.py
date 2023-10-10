l1 = int(input("Qual é o tamanho do lado 1 do triângulo? "))
l2 = int(input("Qual é o tamanho do lado 2 do triângulo? "))
l3 = int(input("Qual é o tamanho do lado 3 do triângulo? "))

lado = (l1 + l2 + l3) / 2
area = lado * (lado - l1) * (lado - l2) * (lado - l3)

print("A área do triândfulo é √", area)