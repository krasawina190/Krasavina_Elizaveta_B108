fruit = ["яблоко", "киви", "банан", "арбуз"]
k = len(fruit)
n = 0
for i in fruit:
    n+=1
    print(n, "{0:>10}".format(i))