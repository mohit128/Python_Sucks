import sys
sec=-sys.maxsize-1
ma=-sys.maxsize-1
n=int((input("Size : ")))
a=[]

for i in range(n):
    a.append(int(input()))
    sec=ma
    ma=max(a[i],ma)
    

for i in range(n):
    if(sec<a[i] and a[i]!=ma):
        sec=a[i]


if sec == -sys.maxsize - 1:
    print("No second maximum")
else:
    print("Second Max :", sec)