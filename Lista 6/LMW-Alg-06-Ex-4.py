words = []

while True:
        word = input("Digite alguma palvra:")
        if word == "":
            break
        if word not in words:
            words.append(word)

for word in words:
    print(word)