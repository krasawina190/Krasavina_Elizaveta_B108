import os
import shutil

file = os.path.relpath(__file__)
file_name = file + '.copy'

try:
    shutil.copy(file, file_name)
    print(f'{file_name} файл создан')
except FileExistsError:
    print(f'{file_name} файл уже существует')