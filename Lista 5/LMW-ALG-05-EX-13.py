def get_num_days_in_month(month, year):
    if month == 2:  # fevereiro
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 29  # ano bissexto, fevereiro tem 29 dias
        else:
            return 28  # não é bissexto, fevereiro tem 28 dias
    elif month in [4, 6, 9, 11]:
        return 30  # meses com 30 dias
    else:
        return 31  # meses com 31 dias

# Programa principal
month = int(input("Digite o número do mês (1 a 12): "))
year = int(input("Digite o ano (AAAA): "))

num_days = get_num_days_in_month(month, year)
print(f"O mês {month} do ano {year} tem {num_days} dias.")
