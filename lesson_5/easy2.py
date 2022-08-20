fruit_1 = ["банан", "яблоко", "апельсин"]
fruit_2 = ["яблоко", "апельсин", "мандарин"]
fruit = [fruit_1[i] for i in range(len(fruit_1)) for j in range(len(fruit_2)) if fruit_1[i] is fruit_2[j]]
print(fruit)