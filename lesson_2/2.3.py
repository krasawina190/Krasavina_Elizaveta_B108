a = int(input("Введите число "))
max = 0
n = int
while a !=0:
    n = a % 10
    if n > max:
        max = a%10
    a = a//10
print(max)
