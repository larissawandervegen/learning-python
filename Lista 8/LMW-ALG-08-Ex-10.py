def unzip_lst(lst):
    unzipped_lst = []
    i = 0

    while i < len(lst):
        value = lst[i]
        if isinstance(value, int):
            if i + 1 < len(lst):  
                element = lst[i+1]
                unzipped_lst.extend([element] * value)
                i += 2
            else:
                break
        else:
            unzipped_lst.append(value)
            i += 1

    return unzipped_lst


def main():
    cod_lst = ["A", 12, "B", 4, "A", 6, "B", 1]
    unzipped_lst = unzip_lst(cod_lst)
    print("Lista Codificada:", cod_lst)
    print("Lista Descompactada:", unzipped_lst)


main()