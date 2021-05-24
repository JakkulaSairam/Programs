n=int(input())
l=list(map(int,input().split()))
h=sorted(l)
k=len(l)
for i in range(len(l)):
    if l[i]==h[i]:
        k=k-1
    else:
        break
for j in range(len(l)-1,0,-1):
    if l[j]==h[j]:
        k=k-1
    else:
        break
if h==l:
    print("0")
else:
    print(k)