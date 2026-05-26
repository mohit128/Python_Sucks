
a=[]
n=int(input("Array length "))
k=int(input("No of Rotation "))
for i in range(n):
    a.append(int(input("Enter elemnts ")))

def rotate(k,a=None):
    if a is not None:
        b=[]
        len(a)
        if k==0:
            return a
        elif k>len(a):
            k=k%len(a)
        while k>0:
            last=a.pop()
            b.insert(0,last)
            k-=1
        for i in a:
            b.append(i)
        return b
    else: return []   
print(a)     
print("printing by pythonic way")
print(a[-k:] + a[:-k])
print("Printing by function")
print(rotate(k,a))


