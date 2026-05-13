import math

def primeChk(n):
    if(n<2):return False
    for k in range(2,int(math.sqrt(n))+1):
        if(n%k==0): 
            return False
            break
    return True

def primeRec(n,d=2):
    if(n<2):return False
    if(d>int(math.sqrt(n))): return True
    if(n%d==0):
        return False
    return primeRec(n,d+1)


n=int(input("Enter no to check :"))

if(primeRec(n)):print(n," is a Prime")
else:print(n," is a Non-Prime")
