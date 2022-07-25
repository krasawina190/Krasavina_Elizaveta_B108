import math
numbers = [2, -5, 8, 9, -25, 25, 4]
new_numbers = []
n = len(numbers)
for i in range(n):
    if numbers[i] > 0:
        s = math.sqrt(numbers[i])
        s = int(s)
        if s*s == numbers[i]:
            new_numbers.append(int(math.sqrt(numbers[i])))
print(new_numbers)