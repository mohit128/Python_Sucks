b=input().lower()
a=list(b)
z=[]

for i in range(len(a)):
    if((ord(a[i])>=97 and ord(a[i])<=122) or (ord(a[i])>=48 and ord(a[i])<=57)):
        z.append(a[i])
print("".join(z))