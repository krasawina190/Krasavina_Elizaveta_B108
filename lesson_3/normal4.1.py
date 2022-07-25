list_1 = [1,6,7,4,2,1,6,12]
list_2 = []
l = len(list_1)

for i in range(0,l-1):
    k=0
    for j in range(i+1, l):
        if (list_1[i]==list_1[j]):
            k=k+1
    if (k==0):
        list_2.append(list_1[i])
print(list_2)