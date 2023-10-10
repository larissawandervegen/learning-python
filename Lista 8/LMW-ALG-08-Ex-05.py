def main():
    def add():
        values = input("Digite um valor e tecle ENTER para parar: ")
        if values == "":
            return 0.0
        value = int(values)
        add_rest = add()
        return value + add_rest
    
    total = add()
    print(total)

main()