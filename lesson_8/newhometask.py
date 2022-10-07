import random

# ввести карточку
# вывести карточку
# посчитать длину

class Card:
    def __init__(self):
        self.numbers = list()

    # вводим карточку:
    def filling_card(self):
        list_1 = list()
        list_2 = list()
        list_3 = list()
        count = 0

        while count <5:
            num = random.randint(1, 90)
            num = str(num)
            if num not in list_1:
                list_1.append(num)
                count+= 1
        count = 0
        list_1.sort()
        list_1 = list(list_1) + list(' ' * 16)
        random.shuffle(list_1)
        self.numbers.append(list_1)

        while count <5:
            num = random.randint(1, 90)
            num = str(num)
            if num not in list_1 and num not in list_2:
                list_2.append(num)
                count+= 1
        count = 0
        list_2.sort()
        list_2 = list(list_2) + list(' ' * 16)
        random.shuffle(list_2)
        self.numbers.append(list_2)

        while count <5:
            num = random.randint(1, 90)
            num = str(num)
            if num not in list_1 and num not in list_2 and num not in list_3:
                list_3.append(num)
                count+= 1
        count = 0
        list_3 = list(list_3) + list(' ' * 16)
        random.shuffle(list_3)

        self.numbers.append(list_3)

    # печатаем карточку:
    def print_card(self):
        print('- '*24)
        for i in self.numbers:
            print(' '.join(i))
        print('- ' * 24)

    def len_card(self):
        count = 0
        for i in self.numbers:
            for j in i:
                count += 1
        return count

    def delete_keg(self, n):
        n = str(n)
        count_i = -1
        count_j = -1
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if self.numbers[i][j] == n:
                    count_i = i
                    count_j = j
        self.numbers[count_i][count_j] = ' '

def choice_keg():
    flag = False
    while flag is False:
        keg = str(random.randint(1, 90))
        if keg not in list_of_keg:
            #print('if')
            flag = True
            list_of_keg.append(keg)
    return keg

list_of_keg = list()

card_of_computer = Card()
card_of_computer.filling_card()
print('Карточка компьютера:')
card_of_computer.print_card()

computer_one = list()
for i in card_of_computer.numbers:
    for j in i:
        if j!= ' ':
            #j = int(j)
            computer_one.append(j)


print()

card_of_person = Card()
card_of_person.filling_card()
print('Карточка пользователя:')
card_of_person.print_card()

person_one = list()
for i in card_of_person.numbers:
    for j in i:
        if j!= ' ':
            #j = int(j)
            person_one.append(j)


len_computer = len(computer_one)
len_person = len(person_one)

print(len_computer)
print(len_person)

print()

flags = True

while flags:
    keg = choice_keg()
    print('Выпал бочонок с номером {}'.format(keg))
    print()

    if keg in computer_one:
        computer_one.remove(keg)
        card_of_computer.delete_keg(keg)
        len_computer -= 1
    print('Карточка компьютера после шага:')
    card_of_computer.print_card()

    if len_computer == 0:
        print('Компьютер победил!')
        break

    print()

    print()

    print()
    print('Зачернуть число {} или продолжить?'.format(keg))
    print('1 - зачеркнуть, 2 - продолжить')
    print()
    step = int(input())

    if step == 1:
        if keg not in person_one:
            print('Вы были невнимательны и проиграли1')
            break
        if keg in person_one:
            person_one.remove(keg)
            card_of_person.delete_keg(keg)
            len_person -= 1

    if step == 2:
        if keg in person_one:
            print('Вы были невнимательны и проиграли2')
            break

    if len_person == 0:
        print('Пользователь победил!')
        break

    print('Карточка пользователя после шага:')
    card_of_person.print_card()
    print()

    print()

