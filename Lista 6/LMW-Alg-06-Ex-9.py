def calculate_average (numbers):
    numbers = []  
    num_list = numbers.split()
    amount = 0
    for numero in num_list:
        amount += int(numero)
    average = amount / len(num_list)
    return average

def main():
    while True:
        numbers = input("Digite uma sequência de números (ou tecle enter para parar): ")
        if numbers == "":
            break
    print("A média dos numéros é:", calculate_average(numbers))

main()