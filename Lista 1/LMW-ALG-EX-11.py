import math

t1 = float(input("Qual a latitude do ponto 1? "))
g1 = float(input("Qual a longitudde do ponto 1? "))

t2 = float(input("Qual a latitude do ponto 2? "))
g2 = float(input("Qual a longitudde do ponto 2? "))

t1r = (t1 * math.pi) / 180
g1r = (g1 * math.pi) / 180

t2r = (t2 * math.pi) / 180
g2r = (g2 * math.pi) / 180

distancia = 6371.01 * math.acos(math.sin(t1r) * math.sin(t2r) + math.cos(t1r) * math.cos(t2r) * math.cos(g1r - g2r))

print("A distância é de", distancia)
