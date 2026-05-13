def arm(n):
    t=n
    c=0
    s=0
    while n>0:
        n//=10
        c+=1
    n=t
    while n>0:
        s+=(n%10)**c
        n//=10
    return s==t
print(arm(153))