n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
a=[]
k=1
for i in range(n-1,-1,-1):
    if k%2==0:
        for j in l[i]:
            a.append(j)
    else:
        for j in l[i]:
            a.append(j)
