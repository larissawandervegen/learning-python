def classify_list(lst):
    if lst == sorted(lst) or lst == sorted(lst, reverse=True):
        return True
    else:
        return False

def main():
    num_list = input("Digite os números da lista separados por vírgula: ")
    numbers = num_list.split(",")
    numbers = [int(num.strip()) for num in numbers]

    if classify_list(numbers):
        print("A lista está classificada.")
    else:
        print("A lista não está classificada.")
        
main()