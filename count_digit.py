
def count_rec(n ,s=0):
    if(n==0):return 1 if s==0 else s
    return count_rec(n//10,s+1)
print(count_rec(0))