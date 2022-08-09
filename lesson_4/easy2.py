def my_round(number, ndigits):
    number = number*10**ndigits
    if number%10>0.4:
        number+= 1
    number=int(number)
    number=number/10**ndigits
    return number
print(my_round(2.1234567, 5))