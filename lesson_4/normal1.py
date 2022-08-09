def fibonachi(n, m):
    fibonachi_list = [1, 1]
    iter = 1
    next_value = 0
    value_0 = fibonachi_list[0]
    value_1 = fibonachi_list[1]

    while iter<m:
        next_value = value_1+value_0
        fibonachi_list.append(next_value)
        iter+= 1
        value_0 = fibonachi_list[iter]
        value_1 = next_value
    print(fibonachi_list[n:m])

fibonachi(0, 5)