s=input()
"""a=[0]*100001
print(a)"""
def DupCount(s):
    
    k=""
    for i in range(len(s)):
        
        if(s.count(s[i])==1):
            k+=s[i]
    return len(k),list(k)
print(DupCount(s))