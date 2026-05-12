n=5
c='h'

for i in range(n):
    print((c*i).rjust(n-1)+c+(c*i).ljust(n+1))
for i in range(n):
    print((c*n).center(n*2-1,'-')+(c*n).center(n*4-1,'-'))
for i in range(n-2):
    print((c*n*n))
for i in range(n):
    print((c*n).center(n*2-1,'-')+(c*n).center(n*4-1,'-'))
for i in range(4,-1,-1):
    print(((c*i).rjust(n-1)+c+(c*i).ljust(n+1)).center(n*n+n*3))