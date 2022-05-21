def prime(a):
    flag = True
    if a>1:
        for i in range(2,a):
            if a%i==0:
                flag = False
                break
        return flag
    else: return(False)         

def nextPrime(a):
    flag = False
    while flag == False:
        a+=1
        if prime(a) == True:
            return a
            flag = True

print(nextPrime(2))
