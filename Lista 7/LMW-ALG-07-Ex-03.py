def buscaReversa(dictionary, value):
    found_keys = []
    for key, crrnt_value in dictionary.items():
        if crrnt_value == value:
            found_keys.append(key)
    return found_keys

def main():
    dictionary = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    srch_value = input("Digite um valor a ser procurado:")
    found_keys = buscaReversa(dictionary, srch_value)
    if found_keys:
        print(f"As chaves encontradas para o valor {srch_value} são: {found_keys}")
    else:
        print(f"Nenhuma chave encontrada para o valor {srch_value}.")

main()
