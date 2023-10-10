n = int(input("Digite um númeor de 3 algarismos: "))

c = n // 100
d = (n % 100) // 10
u = (n % 10)

c_inver = u * 100
d_inver = d * 10
u_inver = c 

m= c_inver + d_inver + u_inver

print("O número inverso é igual a", m)