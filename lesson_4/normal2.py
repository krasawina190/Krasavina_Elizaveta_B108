def sort_to_max(origin_list):
    n = len(origin_list)
    flag = False

    for i in range(n - 1):
        for j in range(n - i - 1):
            flag = False
            if origin_list[j] > origin_list[j + 1]:
                flag = True
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
        if flag == False:
            break

    print(origin_list)
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])