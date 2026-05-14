s=input().lower()
v=0
c=0
for l in s:
    
    if l=='a'or l=='e'or l=='i' or l=='o'or l=='u':
        v+=1
        
    else: c+=1

print("Vowels: ",v)
print("Consonants: ",c)