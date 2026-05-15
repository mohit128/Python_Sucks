c=input().lower()
a=[0]*1000001
r=[]
d={}

for i in c:
    "d[i]=d.get(i,0)+1"
    a[ord(i)]+=1
    r.append(a[ord(i)])

print(r)
