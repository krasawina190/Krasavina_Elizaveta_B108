import os

my_folder = os.getcwd() #место, папка, где мы находимся
new_folder = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']
for i in range(len(new_folder)):
    new_path = os.path.join(my_folder, new_folder[i])
    try:
        os.mkdir(new_path)
    except FileExistsError:
        print(f"папка {new_folder[i]} уже создана")


for i in range(len(new_folder)):
    new_path = os.path.join(my_folder,new_folder[i])
    os.rmdir(new_folder[i])