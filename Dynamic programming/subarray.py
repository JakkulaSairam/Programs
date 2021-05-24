n=int(input())
l=list(map(int,input().split()))
ans=[]
for i in range(len(l)):
    k=l.count(l[i])+l.count(l[i]+1)
    print(l[i],l.count(l[i]),l.count(l[i]+1),l.count(l[i]-1))
    ans.append(k)
print(max(ans))