for f in range(int(input())):
    d={'p':0,'q':0,'r':0,'s':0,'t':0}
    s=input()
    c=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            c=c+1
        else:
            if c>d[str(s[i])]:
                d[str(s[i])]=c
            c=1
    print(max(d.values()),end=" ")
    for k,v in d.items():
        if v==max(d.values()):
            print(k)
            break