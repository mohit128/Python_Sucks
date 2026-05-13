def digits_sum(n,s=0):
    if(n==0): return s
    return s+digits_sum(n//10,n%10)
print(digits_sum(123456789))