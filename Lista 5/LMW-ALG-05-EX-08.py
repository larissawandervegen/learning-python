def capitalize_string(text):
    capitalized_text = text.capitalize()  
    punctuation_indices = [i for i in range(len(text)) if text[i] in ".!?"]
    for index in punctuation_indices:
        if index + 1 < len(text):
            capitalized_text = capitalized_text[:index + 1] + text[index + 1].capitalize() + capitalized_text[index + 2:]

    return capitalized_text

text = input("Digite uma frase: ")

capitalized_text = capitalize_string(text)
print(capitalized_text)

