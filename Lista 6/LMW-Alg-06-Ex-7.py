def verify_perfect_num(number):
    numbers_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)
    return numbers_sum == number

def main():
    for number in range(1, 10001):
        if verify_perfect_num(number):
            print(number)

main()
