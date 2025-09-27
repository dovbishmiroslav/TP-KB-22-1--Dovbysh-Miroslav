def dis(a, b, c):
    D = b**2 - 4*a*c
    return D

a = float(input("Введіть a (число перед x²): "))
b = float(input("Введіть b (число перед x): "))
c = float(input("Введіть c (третє число): "))

print(dis(a, b, c))