def zip(data, counter=1):
    if not data:
        return []

    fst = data[0]

    if len(data) > 1 and data[1] == fst:
        return zip(data[1:], counter + 1)
    else:
        result = [str(counter), fst]
        return result + zip(data[1:])


def main():
    data = input("Digite a string a ser compactada:")

    compact = zip(data)

    print("Resultado codificado em run-length:", "".join(compact))

main()