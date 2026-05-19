def subset(n,s,a=None):
    if a==None:
        a=[]
    if n>=len(s): 
        print(a)
        return 
    a.append(s[n])
    subset(n+1,s,a)
    a.pop()
    subset(n+1,s,a)

s=input()

subset(0,s)