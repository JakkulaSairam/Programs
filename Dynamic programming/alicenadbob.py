s=input()
k=int(input())
ans=[i for i in s]
ans1=[i for i in s]
c=0
for i in range(0,len(s)-k):
    if ans[i]!=ans[i+k]:
        ans[i+k]=ans[i]
        c=c+1

z=0
for i in range(0,len(s)-k):
    if ans1[i]!=ans1[i+k]:
        ans1[i]=ans1[i+k]
        z=z+1
print(min(c,z))

