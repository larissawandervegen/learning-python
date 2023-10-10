def isInteger(string):
    string = string.strip()
    if len(string) <1:
        return False
    
    if string[0] in ["+","-"]:
        if len(string) ==1:
            return False
        string = string[1:]

    if not string.isdigit():
        return False
    
    return True 
   
string = input("Digite uma string para verificar se é inteiro ou não: ")
if isInteger(string):
    print(f'A string "{string}" é um número inteiro válido.')
else:
    print(f'A string "{string}" não é um número inteiro válido.')
