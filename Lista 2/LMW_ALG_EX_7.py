n = int(input("Digite um númeor de 3 algarismos: "))

c = n // 100
d = (n % 100) // 10
u = (n % 10)

print("A centena é igual a", c)
print("A dezena é igual a ", d)
print("A unidade é igual a ", u)