def subsetsum(l,n):
    if n<0:
        return 0
    if n==0:
        return []
    for i in range(len(l)):
        k=subsetsum(l,n-l[i])
        if k!=0:
            return [k,l[i]]
    return 0


n=int(input())
l=list(map(int,input().split(" ")))
print(subsetsum(l,n))