x = int(input("Digite o valor de x:"))
raiz = x/2
precisao = 0.0001

while (raiz * raiz - x) > precisao:
    raiz = (raiz + (x/raiz)) / 2
print("A raíz quadrada é", raiz)