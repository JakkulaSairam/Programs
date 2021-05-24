m,n=list(map(int,input().split()))
l=list(map(int,input().split()))
k=list(map(int,input().split()))
f=0
while(True):
    if sum(l)==sum(k):
        f=1
        print(sum(l))
        break
    if sum(l)>sum(k):
        l.remove(l[len(l)-1])
    else:
        k.remove(k[len(k)-1])
if f==0:
    print("Not possible")
    
