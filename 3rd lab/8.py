from random import randint
def password():
    l = randint(7,10)
    pw = ''
    for i in range (1, l+1):
        pw += chr(randint(33,126))
    return pw


print(password())