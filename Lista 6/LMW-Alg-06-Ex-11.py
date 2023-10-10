import random 

def generate_numbers():

    numbers = []

    while len(numbers) < 6:
        num = random.randint(1, 60)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    return numbers

def main():
    ticket = generate_numbers()
    print("Os números sorteados são:")
    
    for num in ticket:
        print(num)
main()