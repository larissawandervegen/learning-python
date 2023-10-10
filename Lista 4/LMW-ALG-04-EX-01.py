contador = 0
soma = 0

while True:
   numero = int(input("Digite um número inteiro:"))
   if numero == 0 and contador == 0:
      print("Erro: o primeiro valor inserido não pode ser 0.")
      continue
   if numero == 0 and contador > 0:
      break
   contador = contador + 1
   soma = soma + numero
   media = soma / contador
print(media)