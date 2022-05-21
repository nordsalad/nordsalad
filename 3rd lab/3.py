def shop(a):
    a-=1
    if a<0:
        return('ошибка')
    elif a == 1: return(13.9)
    else:
        return(10.95 + a*2.95)

a = int(input('Введите колличество товаров: '))
print(shop(a))