s=input()
a=list(s)
for i in range(len(a)):
    for j in range(i+1,len(a),1):
        if(ord(a[i])>ord(a[j])):
            t=a[i]
            a[i]=a[j]
            a[j]=t
print(a)
