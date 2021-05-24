ans=[]
def call(l,n):
    for i in range(n+1):
        for j in range(i):
            if k==sum(l[j:i]):
                ans.append(len(l[j:i]))
n,k=map(int,input().split())
l=list(map(int,input().split()))
call(l,n)
"""ans=[]
for i in range(n):
    s=0
    for j in range(n):
        print(l[i:j])
        h=sum(l[i:j])
        if h==k:
            ans.append(len(l[i:j]))"""
if len(ans)==0:
    print("0")
else:
    print(max(ans))