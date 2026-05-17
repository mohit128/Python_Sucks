s=input().lower()
k=input().lower()
f=False
for i in range(len(s)-len(k)+1):
    m=False
    for j in range(len(k)):
        if s[i+j]!=k[j]:
            m=True
            break
    if not m:
        f=True

if f:
    print("It's matched")
else:
    print("Unmatched")