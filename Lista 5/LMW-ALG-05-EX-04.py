def calculate_median(num1,num2,num3):
    n_bigger = max(num1, num2, num3)
    n_smaller = min(num1, num2, num3)
    median = (num1, num2, num3) - n_bigger - n_smaller 
    return median

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    median = calculate_median(num1, num2, num3)
    print("A mediana é", median)

main()