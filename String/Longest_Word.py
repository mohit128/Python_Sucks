import sys
s=input()
a=list(s)
a.append(" ")
m=-sys.maxsize-1
r=""
i=0
j=0
while(j<len(a)):
    c=0
    if(a[j]==" "):
        c=j-i
        
        if(c>m):
            m=c
            r=s[i:j]
        i=j
        i+=1
    j+=1

print(r)