def ride ():
    km = float(input("Digite a distância percorrida em km:"))
    m = km * 1000
    total = 4 + ((m / 140) * 0.25)
    return total

ride_price = ride ()
print("O valor total da corrida é de: R${:.2f}" .format(ride_price))