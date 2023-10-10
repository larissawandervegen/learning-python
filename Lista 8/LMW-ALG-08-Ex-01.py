def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    
def main():
    number = int(input("Digite um número inteiro:"))
    result = factorial(number)
    print(f"O fatorial de {number} é: {result}")

main()