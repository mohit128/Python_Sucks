def reverseNo(n):
    s=0
    while(n>0):
        
        s=int(s*10)+n%10
        n//=10
    return s

def reverse_rec(n,s=0):
    
    if(n>0):return s
    return reverse_rec(n//10,s*10+n%10)



print(reverseNo(132))