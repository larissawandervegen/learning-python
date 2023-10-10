def fibonacci(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

def main():
    number = int(input("Digite um valor inteiro:"))
    result = fibonacci(number)
    print(result)

main()