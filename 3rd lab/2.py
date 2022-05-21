from math import ceil

def taxi(a):
    m = a*1000
    n = ceil(m/140)
    return(4+n*0.25)

a = float(input('Введите колличество километров: '))
print(taxi(a))