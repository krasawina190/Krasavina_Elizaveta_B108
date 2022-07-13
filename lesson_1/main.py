name = "Лиза"
age = int(input("Ваш возраст: "))
new_age = age - 18
if age > 18:
    if new_age >= 5:
        print(name, "на", new_age, "лет старше 18")
    elif new_age == 1:
        print(name, "на", new_age, "год старше 18")
    elif new_age >= 2 and new_age < 5:
        print(name, "на", new_age, "года старше 18")
else:
    new_age *= (-1)
    print(new_age)
    if new_age >= 5:
        print(name, "на", new_age, "лет младше 18")
    elif new_age == 1:
        print(name, "на", new_age, "год младше 18")
    elif new_age >= 2 and new_age < 5:
        print(name, "на", new_age, "года младше 18")








