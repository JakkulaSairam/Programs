ans1=[]
def called(l,n,i):
    if i==n:
        s=l.copy()
        ans1.append(s)
        return
    l[i]=0
    called(l,n,i+1)
    l[i]=1
    called(l,n,i+1)
    return
n=int(input())
l=[0]*(n)
k=[]
called(l,n,0)
print(ans1)
for i in range(2**n):
    ans=[]
    s=ans1[i]
    ans=[str(s[0])]
    for j in range(1,len(s)):
        ans.append(str(s[j]^s[j-1]))
    k.append("".join(ans))
p=[]
for i in k:
    print(int(i,2))
    p.append(int(i,2))
print(p)