def prime(a):
    flag = True
    if a>1:
        for i in range(2,a):
            if a%i==0:
                flag = False
                break
        return flag
    else: return(False)         

print(prime(-10))