s=input()
a=list(s)

def dupCh(s):
    s=""
    for c in a:
        if c==" " :s+=c
        if a.count(c)==1 and c!=" ": s+=c
    return s
print(dupCh(s))