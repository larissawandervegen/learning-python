def precedencia(operador):
    if operador in ['+', '-']:
        return 1
    elif operador in ['*', '/']:
        return 2
    elif operador == '^':
        return 3
    else:
        return -1

def main():
    operador = input("Digite um operador matemático: ")
    resultado = precedencia(operador)

    if resultado == -1:
        print("O valor inserido não é um operador matemático.")
    else:
        print(f"A precedência do operador {operador} é {resultado}.")

main()

