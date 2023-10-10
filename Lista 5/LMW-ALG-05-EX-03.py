def calculate_shipping(items):
    if items <= 0:
        return 0.0 
    elif items == 1:
        return 10.95  
    else:
        shipping_cost = 10.95 + (2.95 * (items - 1))
        return shipping_cost

def main():
    items = int(input("Digite a quantidade de itens: "))
    shipping_cost = calculate_shipping(items)
    print("O custo do envio é R$ {:.2f}".format(shipping_cost))

main()