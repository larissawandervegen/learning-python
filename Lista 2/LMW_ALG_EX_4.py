primeiro = int(input("Digite o primeiro número inteiro:"))
segundo = int(input("Digite o segundo número inteiro:"))
terceiro = int(input("Digite o terceiro número inteiro:"))

n_maior = max(primeiro, segundo, terceiro)
n_menor = min(primeiro, segundo, terceiro)
meio = (primeiro + segundo + terceiro) - n_maior - n_menor

print(f"A sequência crescente é {n_menor}, {meio}, {n_maior}.")