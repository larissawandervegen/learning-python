dia = int(input("Digite o dia escolhido:"))
mes= input("Digite o mês escolhido:")

if dia == 1 and mes == "janeiro":
    print('O feriado nacional é "Confraternização universal".')
elif dia == 21 and mes == "abril":
    print('O feriado nacional é "Tiradentes".')
elif dia == 1 and mes == "maio":
    print('O feriado nacional é "Dia do trabalho".')
elif dia == 7 and mes == "setembro":
    print ('O feriado nacional é "Independência do Brasil".')
elif dia == 12 and mes == "outubro":
    print ('O feriado nacional é "Nossa Senhora Aparecida".')
elif dia == 2 and mes == "novembro":
    print ('O feriado nacional é "Finados".')
elif dia == 15 and mes == "novembro":
    print ('O feriado nacional é "Proclamação da República".')
elif dia == 25 and mes == "dezembro":
    print ('O feriado nacional é "Natal".')
else:
    print("A data inserida não conrresponde a um feriado nacional.")
