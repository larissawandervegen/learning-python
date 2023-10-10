import re

def s_lst(strings_list):
    return [words for item in strings_list for words in item.split()]

def main():
    strings_list = []

    while True:
        item = input("Digite uma palavra (ou tecle enter para parar): ")

        if item == "":
            break
        strings_list.append(item)

        lst = s_lst(strings_list) 
    print(lst)
main()
