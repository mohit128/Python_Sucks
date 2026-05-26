a=[]
n=int(input())
for i in range(n):
    a.append(int(input()))
print(a)
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]==a[j]:
            a.pop(j)
        else:
            j+=1
    i+=1

def fun_rem(a=None):
    if a is not None:
        a.sort()
        i=0
        while i<len(a):
            j=i+1
            if a[i]==a[j]: 
                a.pop(j)
            else:j+=1
            i+=1
        return a
    else : return "Array empty hai"




print(a)
print(fun_rem(a))


