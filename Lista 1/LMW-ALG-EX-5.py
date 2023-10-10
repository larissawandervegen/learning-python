vasilha_menor = float(input("Quantos vasilhames de 1L ou mais quer reciclar?") )
vasilha_maior = float(input("Quantos vasilhames de 2L ou mais quer reciclar?"))

cred_menor = vasilha_menor * 0.10
cred_maior = vasilha_maior * 0.25

total = cred_maior + cred_menor 

print("O seu crédito total é de R$ {:.2f}".format(total))