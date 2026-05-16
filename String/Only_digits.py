def digits(s):
    for i in s:
        if not (ord(i)>= 48 and ord(i)<=57): 
            return "Not Digits"
            
        
    return "Digits"

s=input()
print(digits(s))
try:
    
    print(int(s))
    
except ValueError as e:
    print("This is Value Error")
