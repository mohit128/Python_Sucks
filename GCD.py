import math
def gcd(a,b):
    if(a==0): return b 
    if b==0: return a
    if(a%b==0):
        return b
    return gcd(b,a%b)

def lcm(a,b):
    if(a==0 or b==0):return 0
    return (a*b)//gcd(a,b)
print((12,37))



