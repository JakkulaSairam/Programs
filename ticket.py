
l=input()
s=[str(i) for i in l]
i=0
c=0
while(i<len(s)-1):
    if s[i]==s[i+1] and s[i]=='0':
        s[i+1]='1'
        c=c+1
    elif s[i]==s[i+1] and s[i]=='1':
        s[i+1]='0'
        c=c+1
    i=i+1
print(c)
