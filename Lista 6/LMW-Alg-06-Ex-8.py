import string
def return_list (words):
    clean_str = ''.join(caractere for caractere in words if caractere not in string.punctuation)
    lst = clean_str.split()
    return lst

def main ():
    words = input("Digite uma frase com símbolos de pontuação:")
    print(return_list(words))

main()
