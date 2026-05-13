import math
a=[]
def isPrime(n):
    if(n<2):return False
    for k in range(2,int(math.sqrt(n))+1):
        if(n%k==0): 
            return False
            break
    return True

def NPrime(n):
    c=0
    i=2
    while c<n:
        if isPrime(i):
            print(i)
        c+=1
        i+=1
NPrime(77)