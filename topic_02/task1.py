def dis(a, b, c):
    D = b**2 - 4*a*c
    return D

def cor(a, b, c):
    D = dis(a, b, c)
    if D < 0:
        res = "корені відсутні"
    elif D == 0:
        x = (b*-1)/(2*a)
        res = f"корень рівняння: {x}"
    else:
        x1 = ((b*-1)+(D ** 0.5))/(2*a)
        x2 = ((b*-1)-(D ** 0.5))/(2*a)
        res = f"корень 1: {x1} корень 2: {x2}"
    return res


a = float(input("Введіть a (число перед x²): "))
b = float(input("Введіть b (число перед x): "))
c = float(input("Введіть c (третє число): "))

print(dis(a, b, c))
print(cor(a, b, c))