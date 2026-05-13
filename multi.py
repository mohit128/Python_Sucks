a=[]
def multiply_no( n,i):
    if(i==0): 
        a.reverse()
        return a
    a.append(n*i)
    return multiply_no(n,i-1)

print(multiply_no(110,15))
