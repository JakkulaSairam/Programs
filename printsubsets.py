def call(l,n):
    for i in range(n+1):
        for j in range(i):
            print(l[j:i])

l=list(map(int,input().split()))
n=len(l)
call(l,n)