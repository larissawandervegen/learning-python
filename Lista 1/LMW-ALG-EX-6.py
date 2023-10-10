p_principal = float(input("Qual o valor da prato principal? "))
suco = float(input("Qual o valor do suco? "))
sobremesa = float(input("Qual o valor da sobremesa? "))

conta = p_principal + suco + sobremesa
total = (conta / 100) * 10 + conta

print("O seu total é de: R$ {:.2f}".format(total))