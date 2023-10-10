def prime_num(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

number = int(input("Digite um número para verificar se é primo: "))

if prime_num(number):
    print("O número inserido é primo!")
else:
    print("O número inserido não é primo!")
