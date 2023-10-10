def verify_characters(text):
    return len(set(text)) == len(text)
    
def main():
    text = input("Digite uma palavra:")
    result = verify_characters(text)
    print(result)

main()