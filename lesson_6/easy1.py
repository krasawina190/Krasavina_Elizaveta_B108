def avg(a, b):
    return (a*b)**0.5

try:
    a = float(input('a= '))
    b = float(input('b= '))
    c = avg(a, b)
    print('Среднее геометрическое = {:.2f}'.format(c))
except ValueError:
    print('Ошибка, проверьте введеные числа')