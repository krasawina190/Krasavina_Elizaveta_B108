def my_filter(f_for_filter, list_for_filter):
    new_list = []
    for i in list_for_filter:
        if f_for_filter(i)==True:
            new_list.append(i)
    return new_list

list_f = [2, 4, 5, 7, 9, 4]

print(my_filter(lambda x: x%2==0, list_f))