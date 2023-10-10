def fibonacci(number, memory={}):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    elif number in memory:
        return memory[number]
    else:
        result = fibonacci(number-1, memory) + fibonacci(number-2, memory)
        memory[number] = result
        return result

def main():
    number = int(input("Digite um valor inteiro:"))
    result = fibonacci(number)
    print(result)

main()