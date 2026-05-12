def floatAvg(a,b):
    return float(a+b/2)
a=float(input("Enter number a: "))
b=float(input("Enter number b: "))
print("a and b avg is : ",floatAvg(a,b))

if a > b:
    print("A is greater", a)
elif b > a:
    print("B is greater", b)
else:
    print("A==B")
def sq_area(a):
    return float(a**2)

print("Area of square side a: ",sq_area(a))
