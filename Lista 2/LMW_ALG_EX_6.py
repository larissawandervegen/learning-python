número = int(input("Digite um número com 4 algarismos: "))

milhar = número // 1000
centena = (número % 1000) // 100
dezena = (número % 100) // 10
unidade = (número % 10)

soma = milhar + centena + dezena + unidade
print ("A soma dos algarismos é igual a ", soma)
