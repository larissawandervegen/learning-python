numbers = []

while True:
    original_numbers = input("Digite um número inteiro:")
    if original_numbers == "":
        break
    numbers.append(int(original_numbers))

negatives = []
zeros = []
positives = []

for number in numbers:
    if number < 0:
        negatives.append(number)
    elif number == 0:
        zeros.append(number)
    else:
        positives.append(number)

for number in negatives:
    print(number)

for number in zeros:
    print(number)
    
for number in positives:
    print(number)