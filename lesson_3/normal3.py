import random
numbers = []
n = int(input("Количество элементов в списке: "))
for i in range (n):
    numbers.append(random.randint(-100, 100))
print(numbers)