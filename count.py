n=int(input("Length : "))
a=()
for i in range(n):
    v=input("Grades of students :")
    a=a+(v,)
    
print("No of students who got 'A' grade : ",a.count('A'))
