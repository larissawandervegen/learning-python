segundos = int(input("Digite um valor em segundos:"))

dia = segundos // 86400
hora = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
segundo = segundos % 60

print (f"O valor formatado em D:HH:MM:SS, é {dia}:{hora : 02}:{minutos : 02}:{segundos : 02}")