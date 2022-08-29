import os
def print_help():
    print('1. Перейти в папку')
    print('2. Посмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')

def folder_change():
    try:
        folder = os.path.abspath(folder_name)
        os.chdir(folder)
        print('Успешно перешел в', os.getcwd())
    except:
        print(f'{folder_name} папка не найдена')

def folder_here():
    my_folder = os.getcwd()

    print(f'Содержимое папки:')
    for i in os.listdir(my_folder):
        print(i)

def folder_delete():
    new_path = os.path.join(os.getcwd(), folder_name)
    try:
        os.rmdir(folder_name)
        print(f'{folder_name} успешно удалена')
    except FileNotFoundError:
        print(f'{folder_name} папка не найдена')

def folder_make():
    new_path = os.path.join(os.getcwd(), folder_name)
    try:
        os.mkdir(folder_name)
        print(f'{folder_name} успешно создана')
    except FileExistsError:
        print(f'{folder_name} папка уже существует')


do = {
    "help": print_help()
}

menu = input('Выберите пункт 1-4. Что делаем с папками? ')
try:
    menu = int(menu)
    if menu == 1 or menu == 3 or menu == 4:
        folder_name = input('Введите имя папки ')
except ValueError:
    print('Введите число')

if menu == 1:
    folder_change()

if menu == 2:
    folder_here()

if menu == 3:
    folder_delete()

if menu == 4:
    folder_make()