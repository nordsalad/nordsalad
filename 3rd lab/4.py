def mediana(a,b,c):
    ar = [a,b,c]
    return(sum(ar) - max(ar) - min(ar))

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print(mediana(a,b,c))