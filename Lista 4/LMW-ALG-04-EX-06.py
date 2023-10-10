while True:
    # le a palavra binaria
    bits = input("Digite um valor de 8 bits:") 
    if bits == "":
        break

    # percorrer a palavra para contar quantos 1s tem la dentro
    n_1 = bits.count("1")
    n_zeros = bits.count("0")

    if n_1 + n_zeros != 8:
        print("Erro: digite uma sequência válida.")
        continue


    # se total de 1s for par, entao o bit de paridade defve ser 1
    if n_1%2==0:
        print("O bit de paridade é 1")
    else:
        print("O bit de paridade é 0")







    """if bits  or bits%2 != 0:
        print("Erro: digite uma sequência válida.")
    elif bits%2 == 0:
        print("O bit de paridade é 0")
    elif bits%2 != 0:
        print("O bit de paridade é 1") """