s=input().lower()
k=input().lower()
f=False
for i in range(len(s)-len(k)+1):
    m=True
    for j in range(len(k)):
        if s[i+j]!=k[j]:
            m=False
            break
    if not m:
        f=True

if f:
    print("It's matched")
else:
    print("Unmatched")