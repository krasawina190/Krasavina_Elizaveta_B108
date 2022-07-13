import math
a = int(input("Первый коэффицент: "))
b = int(input("Второй коэффицент: "))
c = int(input("Третий коэффицент: "))
d = b*b - 4*a*c
if d > 0:
    x1 = (-b + math.sqrt(d))/2*a
    x2 = (-b - math.sqrt(d))/2*a
    print(x1, x2)
elif d == 0:
    x = (-b)/4
    print(x)
elif d < 0:
    print("Корней нет")

