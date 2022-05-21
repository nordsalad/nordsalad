def chisl(a):
    if a == 1: return('1st')
    if a == 2: return('2nd')
    if a == 3: return('3rd')
    if a > 3: return(str(a)+'th')
    if a>12 or a<1: return()

for i in range(1,13):
    print(chisl(i))
