l=['a','e','i','o','u','A','E','I','O','U']
s=""
k=input()
for i in k:
    if i not in l:
        s=s+i
print(s)