mes = input("Dgite o mês:")

if mes == "janeiro" or mes == "março" or  mes == "maio"  or mes == "julho" or mes == "agosto" or mes == "outubro" or mes == "dezembro":
    dias = "31 dias"
elif mes == "abril" or mes == "junho" or mes == "setembro" or mes== "novembro":
    dias = "30 dias"
elif mes == "fevereiro":
    dias = "28 ou 29 dias"

print(f"O mês de {mes} tem {dias}.") 