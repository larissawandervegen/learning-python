list = []

while True:
    integer = int(input("Digite o número inteiro:"))
    if integer == 0:
        break
    list.append(integer)
    organized_list = sorted(list)
for number in organized_list:    
    print(number)
