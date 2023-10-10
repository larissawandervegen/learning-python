def valid_password(password):
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_number = False
    
    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower:
            has_lower = True
        elif character.isdigit():
            has_number = True

password = input("Digite a senha: ")

if valid_password(password):
    print("A senha é válida!")
else:
    print("A senha é inválida!")

  