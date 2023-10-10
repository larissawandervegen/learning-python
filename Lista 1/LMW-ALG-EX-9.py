v_inicial = float(input("Qual valor você irá depositar inicialmente? "))
v_um = v_inicial * 0.12 + v_inicial
v_dois = v_um * 0.12 + v_um
v_tres = v_dois * 0.12 + v_dois

print("O valor final no primeiro ano é de {:.2f}".format(v_um))
print("O valor final no primeiro ano é de {:.2f}".format(v_dois))
print("O valor final no primeiro ano é de {:.2f}".format(v_tres))
