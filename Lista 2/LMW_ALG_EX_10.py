matricula = int(input("Digite o número de matrícula: "))
ano = matricula // 10000
sem = (matricula // 1000) % 10

print("Ano:", ano)
print("Semestre:", sem)