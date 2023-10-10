import random

def ramdom_pass():
    lenth = random.randint(7, 10)
    password = ""
    for _ in range(lenth):
        ascii_code = random.randint(33, 126)
        password += chr(ascii_code)
    return password

print(ramdom_pass())
