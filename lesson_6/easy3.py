import os

my_folder = os.getcwd()
for i in os.listdir(my_folder):
    if os.path.isdir(i):
        print(i)