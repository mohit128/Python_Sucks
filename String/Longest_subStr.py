import sys
s=input()
b=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        sub=s[i:j+1]
        if len(sub)==len(set(sub)):
            b.append(s[i:j+1])
    

print(b)
m=-sys.maxsize-1
for i in range(len(b)):
    m=max(len(b[i]),m)

for i in range(len(b)):
    if(len(b[i])==m):
        print(b[i])
        break
    