d=""
def reverse(s,n=0):
    if(n>=len(s)): return ""
    if(s==""): return s
    return reverse(s,n+1)+s[n]
print(reverse("123"))
