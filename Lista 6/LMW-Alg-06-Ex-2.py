original_list = []

while True:
    integer = int(input("Digite o número inteiro:"))
    if integer == 0:
        break
    original_list.append(integer)

organized_list = sorted(original_list)
# cria uma copia da organized_list
reversed_list = list(organized_list)
reversed_list.reverse()
print(reversed_list)

