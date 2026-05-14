def CWords(s):
    c=1
    if(s==""): return 0
    if(len(s)-1==0 and s!=""): return 1
    for i in s:
        if i==" ":
            c+=1
    return c
print(CWords("Mohit is a good boy"))
        