def tockenizacao(expressao):
    tokens = []
    numero = ""

    for caracter in expressao:
        if caracter.isdigit():
            numero += caracter
        elif caracter in ("+", "-"):
            if numero:
                tokens.append(int(numero))
                numero = ""
            if not tokens or tokens[-1] == "(":
                numero += caracter
            else:
                tokens.append(caracter)
        elif caracter in ("*", "/", "^", "(", ")"):
            if numero:
                tokens.append(int(numero))
                numero = ""
            tokens.append(caracter)

    if numero:
        tokens.append(int(numero))

    return tokens

def main():
    expressao = input("Digite uma expressão matemática: ")
    tokens = tockenizacao(expressao)
    print(tokens)

main()
