a = input("Четные или нечетные? ")
i = 0
if a == "четные":
    for i in range(21):
        if i%2 == 0:
            print(i)
elif a == "нечетные":
    for i in range(21):
        if i%2 == 1:
            print(i)
else:
    print("Я не понимаю, что вы от меня хотите")
