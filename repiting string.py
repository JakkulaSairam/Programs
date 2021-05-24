s=input()
for i in range(0,len(s)):
    k=s[0:i+1]
    h=0
    flag=0
   # print("k=",k)
    while(h<len(s)):
        if k==s[h:h+len(k)]:
            h=h+len(k)
            continue
        else:
            flag=1
            break
    if flag==0:
        print(k)
        break
        