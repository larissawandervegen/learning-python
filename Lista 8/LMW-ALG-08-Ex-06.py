def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)

num_1 = int(input("Digite o primeiro inteiro positivo: "))
num_2 = int(input("Digite o segundo inteiro positivo: "))
mdc = euclidean_gcd(num_1, num_2)

print(f"O MDC de {num_1} e {num_2} é {mdc}")
