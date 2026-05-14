def isPal(s,n=0):
    if(n>=len(s)):return ""
    if(s==""): return s
    return isPal(s,n+1)+s[n]

def palChk(s):
    if s==isPal(s):return "String is palimndrome" 
        
    return "Non-Palindrome String"
    
print(palChk("121"))