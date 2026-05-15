a=input().lower()
b=input().lower()

result = "Anagram" if sorted(a)==sorted(b) else "Not Anagram"

print(result)
