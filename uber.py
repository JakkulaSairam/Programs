n,m=list(map(int,input().split()))
l=[list(map(int,input().split(" "))) for i in range(n)]
#print("l=",l)
pick=[]
drop=[]
for i in l:
    #print("i=",i)
    pick.append(i[1])
    drop.append(i[2])
size=max(drop)
#print("size",size)
arr=[0 for i in range(size+1)] 
for i in l:
    arr[i[1]]+=i[0]
    arr[i[2]]-=i[0]
sum=0
f=0
for i in arr:
    sum+=i
    if sum>m:
        f=1
        break
if f==0:
    print("true")
else:
    print("false")