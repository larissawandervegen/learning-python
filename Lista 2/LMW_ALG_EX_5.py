centavos = int(input("Digite a quantidade de centavos:"))

m_50 = centavos // 50
m_25 = (centavos % 50) // 25
m_10 = (centavos % 25) // 10
m_5 = (centavos % 10) // 5
m_1 = (centavos % 5) // 1

print(f"O seu troco será composto por {m_50} moedas de 50 centavos, {m_25} moedas de 25 centavos, {m_10} moedas de 10 centavos, {m_5} moedas de 5 centavos e {m_1} moedas de 1 centavo.")