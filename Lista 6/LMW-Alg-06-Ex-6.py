def calculate_divisors(number):
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def main():
    number = int(input("Digite um número inteiro positivo: "))
    divisors_list = calculate_divisors(number)
    print(f"Os divisores de {number} são: {divisors_list}")

main()
