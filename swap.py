def swap(a,b):
    
    a^=b
    b^=a
    a^=b
    print(a,b)

a=1
b=2
print(a,b)
swap(a,b)