#Escreva um programa Python que mostre uma tabela
#de conversão de temperaturas em graus Celsius e graus Fahrenheit. A tabela deve incluir em
#suas linhas todas as temperaturas entre 0 e 100 graus Celsius que sejam múltiplas de 10
#graus Celsius. Inclua os cabeçalhos apropriados e tabulações para suas colunas. Pesquise na
#internet sobre a fórmula de conversão de temperaturas Celsius para Fahrenheit.

for temperatura in range(0,101,10):
    fahrenheit = temperatura * 1.8 + 32
    print(f"A temperatura em graus Celcius é {temperatura} e em Fahrenheit {fahrenheit}")