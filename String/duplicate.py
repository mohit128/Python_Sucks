s=input()
i=s.count("M")
print(i)

def DupCount(s):
    
    k=""
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(s[i]==s[j]):

                if s[i] not in k:
                    k+=s[i]
                        
    return len(k),list(k)
print(DupCount(s))