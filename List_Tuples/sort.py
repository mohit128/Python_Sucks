
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

print(a)

for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)