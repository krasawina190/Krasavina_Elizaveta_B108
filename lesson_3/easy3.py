spisok = [1, 4, 8, 7, 16]
k = len(spisok)
for i in range(k):
    if (spisok[i]%2) == 0:
        spisok[i] = spisok[i]//4
    else:
        spisok[i] = spisok[i]*2
print(spisok)