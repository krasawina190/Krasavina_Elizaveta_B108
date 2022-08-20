my_list = [1, 4, -3, -4, 9, 15, -15]
my_list = [my_list[i] for i in range(len(my_list)) if my_list[i]%3==0 and my_list[i]>=0 and my_list[i]%4!=0]
print(my_list)