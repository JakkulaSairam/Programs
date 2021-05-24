def getmaxlength1(l,i,j,m,n,c):
    if i<0 or j<0 or i>m-1 or j>n-1 or l[i][j]==0:
        return c
    return getmaxlength1(l,i,j+1,m,n,c+1)
def getmaxlength2(l,i,j,m,n,c):
    if i<0 or j<0 or i>m-1 or j>n-1 or l[i][j]==0:
        return c
    return getmaxlength2(l,i+1,j+1,m,n,c+1)
def getmaxlength3(l,i,j,m,n,c):
    if i<0 or j<0 or i>m-1 or j>n-1 or l[i][j]==0:
        return c
    return getmaxlength3(l,i+1,j,m,n,c+1)
def getmaxlength4(l,i,j,m,n,c):
    if i<0 or j<0 or i>m-1 or j>n-1 or l[i][j]==0:
        return c
    return getmaxlength4(l,i+1,j-1,m,n,c+1)

m,n=map(int,input().split(" "))
l=[list(map(int,input().split(" "))) for i in range(m)]
ans=[]
for i in range(m):
    for j in range(n):
        if l[i][j]==1:
            ans.append(max(getmaxlength1(l,i,j,m,n,0),getmaxlength2(l,i,j,m,n,0),getmaxlength3(l,i,j,m,n,0),getmaxlength4(l,i,j,m,n,0)))
print(max(ans))

