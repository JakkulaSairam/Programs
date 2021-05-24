c=0
l={'0','1','6','8','9'}
n=int(input())
if n<=10:
    for i in range(6,n+1):
        k=str(i)
        if all(j in l for j in k) and k!='8':
            print(k)
            c=c+1
    print(c)
else:
    c=3
    for i in range(11,n+1):
        k=str(i)
        if all(j in l for j in k) and k!=k[::-1]:
            print(k)
            c=c+1
    print(c)
