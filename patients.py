for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    h=sorted(l)
    ans=[0 for i in range(n)]
    print(ans)
    print("sort",h)
    for j in range(n-1,-1,-1):
        inl=l.index(h[j])
        print("value and index",h[j],inl)
        p=n-j
        l[inl]=-1
        print(l)
        print("indx",inl)
        ans[inl]=str(p)
    print(" ".join(ans))