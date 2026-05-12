i=int(input("length of list : "))

a=[]

for k in range(i):    
    a.append(input("Enter valuese here for list a :"))

print(a)

def pal_check(arr):
    j=len(arr)-1
    i=0
    while(i<j):
        
        if(arr[i]==arr[j]):
            i+=1
            j-=1
        else:
            return False
            break
    return True 

if(pal_check(a)==True):
    print("Palindrome")
else:
    print("Not Palindrome")