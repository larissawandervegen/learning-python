numero = int(input("Digite um número:"))
resto = numero % 2
if(resto == 0):
    resultado = "par"
else:
   resultado = "ímpar"

print(f"O número {numero} é {resultado}.")