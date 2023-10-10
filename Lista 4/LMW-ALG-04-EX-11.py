frase = input("Digite a frase: ")
frase = frase.lower() 
frase_junta = frase.replace(" ", "")  
frase_sem_pontuacao = ""

for letra in frase_junta:
    if letra.isalpha():
        frase_sem_pontuacao += letra
    frase_invertida = frase_junta[::-1]

if frase_sem_pontuacao == frase_invertida:
    print("A frase", frase, "é um palíndromo!")
else:
    print("A frase", frase, "não é um palíndromo.")
