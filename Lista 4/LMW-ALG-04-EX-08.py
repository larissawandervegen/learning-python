mensagem = input("Digite a mensagem:")
deslocamento = int(input("Digite a distância do deslocamento:"))
resultado = ""

for letra in mensagem:
       if letra.isalpha():
            if letra.isupper():
                resultado += chr((ord(letra) + deslocamento - 65) % 26 + 65)
            else:
                resultado += chr((ord(letra) + deslocamento - 97) % 26 + 97)   
print(resultado)
