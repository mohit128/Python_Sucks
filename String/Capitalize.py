b=input().lower()
a=list(b)
f=False
for idx, ch in enumerate(a):

    if(a.index(ch)==0 and not f):
        i=ord(ch)-32
        a[0]=chr(i)
        f=True
    
    if(ch==" "):
        i=idx+1
        j=ord(a[i])-32
        a[i]=chr(j)
print(a)
        




        

