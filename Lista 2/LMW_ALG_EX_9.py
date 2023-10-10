data = int(input("Digite a data no formato DDMMAA: "))

a = data % 100
m = (data // 100) % 100
d = data // 10000

data_inver = a * 10000 + m * 100 + d
print("Data no formato AAMMDD:", data_inver)