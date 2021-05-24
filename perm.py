from itertools import combinations
n=int(input())
l=list(map(int,input().split(" ")))
p=[]
for i in range(1,n+1):
    p.append(list(map(set, combinations(l,i))))
su=0
print(p)
for i in p:
    for j in i:
        su=su+sum(j)
print(su)

