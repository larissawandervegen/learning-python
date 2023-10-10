def remove_extremes(new_values_list, initial_values, last_values):
    values_to_remove = last_values + initial_values
    new_values_list = [value for value in new_values_list if value not in values_to_remove]
    return new_values_list

def main():
    values_list = []

    while True:
        values = input("Digite um número (ou tecle enter para parar): ")

        if values == "":
            if len(values_list) < 4:
                print("São neccesários mais de 4 valores na lista.")
                continue
            else:
                break

        value = int(values)
        values_list.append(value)

    initial_values = values_list[:2]
    last_values = values_list[-2:]

    new_list = remove_extremes(values_list, initial_values, last_values)
    print("Nova lista de valores:", new_list)
    print("Lista de valores original:", values_list)

main()