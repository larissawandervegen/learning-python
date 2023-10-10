def infix_para_posfixa(tokens_infixa):
    precedenciaOperadores = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    operadores = []
    postfix = []

    for token in tokens_infixa:
        if isinstance(token, int):
            postfix.append(token)
        elif token in precedenciaOperadores:
            while operadores and operadores[-1] != "(" and precedenciaOperadores[token] < precedenciaOperadores[operadores[-1]]:
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

expressao_infixa = [3, "+", 4, "*", 2, "/", "(", 1, "-", 5, ")", "^", 2]
expressao_posfixa = infix_para_posfixa(expressao_infixa)
print("Expressão pós-fixada:", expressao_posfixa)
