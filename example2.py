try:
    for _ in range(int(input())):
        n,m=map(int,input().split(" "))
        l=[list(map(int,input().split(" "))) for i in range(m)]
        a=[]
        for i in range(m):
            k=0
            for j in range(n):
                k.append(0)
            a.append(k)
                
        for i in range(m):
            for j in range(n):
                if j==n-1:
                    a[i][j]=0
                else:
                    sum=0    
                    for k in range(j+1,n):
                        sum=sum+a[i][k]
                    a[i][j]=sum
        for i in range(m):
            for j in range(n):
                print(a[i][j],end=" ")
            print()
except:
    pass

      
           