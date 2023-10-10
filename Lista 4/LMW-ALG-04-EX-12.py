print("   ", end="")
for numero in range(1,11):
     print(f"{numero:4}", end="")
print()
for numero in range(1, 11):
    print(f"{numero:4}", end="")
    for multiplicadores in range(1, 11):
        print(f"{numero*multiplicadores:4}", end="")
    print()