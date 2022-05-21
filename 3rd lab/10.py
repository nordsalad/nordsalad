from random import randint
from string import ascii_lowercase
from string import ascii_uppercase

def passcheck(a):
    a = str(a) #на случай если в функцию попадёт int
    flag_num, flag_up, flag_low = False, False, False
    nums = '0123456789'
    ups = ascii_uppercase
    lows = ascii_lowercase
    
    if len(a)>=8:
        for i in range(0, len(a)):
            if a[i] in nums: flag_num = True
            if a[i] in ups: flag_up = True
            if a[i] in lows: flag_low = True
            if (flag_num == True) and (flag_low == True) and (flag_up == True): break
        if (flag_num == False) or (flag_up == False) or (flag_low == False): return False
        else: return True
    else: return False

def password():
    flag = False
    while flag == False:
        l = randint(7,10)
        pw = ''
        for i in range (1, l+1):
            pw += chr(randint(33,126))
        if passcheck(pw): flag = True
    return pw


print(password())