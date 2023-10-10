def countRange (lst, min_value, max_value):
    count = 0
    for value in lst:
        if min_value >= value < max_value:
            count += 1
    return count

def  main():
    lst = []
    while True:
        values = input("Digite uma valor:")
        value = int(values)
        lst.append(value)
        min_value = int(input("Digite um valor mínimo:"))
        max_value = int(input("Digite um valor máximo:"))
        resultado = countRange(lst, min_value, max_value)
        print(f"A quantidade de elementos na lista entre {min_value} e {max_value} é: {resultado}")

main()
