def precedencia(operador):
    operadores_precedencia = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    if operador in operadores_precedencia:
        return operadores_precedencia[operador]
    else:
        return -1

def infix_para_posfixa(tokens_infixa):
    operadores = []
    postfix = []

    for token in tokens_infixa:
        if isinstance(token, int):
            postfix.append(token)
        elif token in ("+", "-", "*", "/", "^"):
            while operadores and operadores[-1] != "(" and precedencia(token) <= precedencia(operadores[-1]):
                postfix.append(operadores.pop())
            operadores.append(token)
        elif token == "(":
            operadores.append(token)
        elif token == ")":
            while operadores and operadores[-1] != "(":
                postfix.append(operadores.pop())
            if operadores and operadores[-1] == "(":
                operadores.pop()
            else:
                raise ValueError("Expressão inválida: parênteses desbalanceados")

    while operadores:
        postfix.append(operadores.pop())

    return postfix

def avaliar_posfixa(tokens_posfixa):
    valores = []

    for token in tokens_posfixa:
        if isinstance(token, int):
            valores.append(token)
        else:
            direita = valores.pop()
            esquerda = valores.pop()
            resultado = None
            if token == "+":
                resultado = esquerda + direita
            elif token == "-":
                resultado = esquerda - direita
            elif token == "*":
                resultado = esquerda * direita
            elif token == "/":
                resultado = esquerda / direita
            elif token == "^":
                resultado = esquerda ** direita
            valores.append(resultado)

    return valores[0]

def tokenizacao(expressao):
    tokens = []
    numero = ""

    for caracter in expressao:
        if caracter.isdigit():
            numero += caracter
        elif caracter in ("+", "-", "*", "/", "^", "(", ")"):
            if numero:
                tokens.append(int(numero))
                numero = ""
            tokens.append(caracter)

    if numero:
        tokens.append(int(numero))

    return tokens

def main():
    expressao = input("Digite uma expressão matemática: ")
    tokens_infixa = tokenizacao(expressao)
    tokens_posfixa = infix_para_posfixa(tokens_infixa)
    resultado = avaliar_posfixa(tokens_posfixa)
    print("Resultado:", resultado)

main()