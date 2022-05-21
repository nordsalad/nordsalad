from cmath import pi
from math import sqrt

def pifagor(a,b):
    a*=a
    b*=b
    return sqrt(a+b)

a = int(input('Введите первый катет: '))
b = int(input('Введите второй катет: '))
print(pifagor(a,b))
