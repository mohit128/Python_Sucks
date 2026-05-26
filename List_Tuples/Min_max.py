import sys
mi=sys.maxsize
ma=-sys.maxsize-1
n=int((input("Size : ")))
a=[]

for i in range(n):
    a.append(int(input()))
    mi=min(a[i],mi)
    ma=max(a[i],ma)

print("Max :",ma,"\nMin : ",mi)
