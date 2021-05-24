
c=0
def find8(l,i,j,n):
    global c
    if i>n or j>n or i<0 or j<0 or l[i][j]==2:
        return 
    c=c+1
    find8(l,i-1,j-1,n)
def find7(l,i,j,n):
    global c
    if i>n or j>n or i<0 or j<0 or l[i][j]==2:
        return 
    c=c+1
    find7(l,i,j-1,n)
def find6(l,i,j,n):
    global c
    if i>n or j>n or i<0 or j<0 or l[i][j]==2:
        return 
    c=c+1
    find6(l,i-1,j-1,n)
def find5(l,i,j,n):
    global c
    if i>n or j>n or i<0 or j<0 or l[i][j]==2:
        return 
    c=c+1
    find5(l,i+1,j,n)
def find4(l,i,j,n):
    global c
    if i>n or j>n or i<0 or j<0 or l[i][j]==2:
        return 
    c=c+1
    find4(l,i+1,j+1,n)

def find3(l,i,j,n):
    global c
    if i>n or j>n or i<0 or j<0 or l[i][j]==2:
        return 
    c=c+1
    find3(l,i,j+1,n)
def find2(l,i,j,n):
    global c
    if i>n or j>n or i<0 or j<0 or l[i][j]==2:
        return 
    c=c+1
    find2(l,i-1,j+2,n)

def find1(l,i,j,n):
    global c
    if i>n or j>n or i<0 or j<0 or l[i][j]==2:
        return 
    c=c+1
    find1(l,i-1,j,n)
    
def call(l,i,j,n):
    find1(l,i,j,n-1)
    find2(l,i,j,n-1)
    find3(l,i,j,n-1)
    find4(l,i,j,n-1)
    find5(l,i,j,n-1)
    find6(l,i,j,n-1)
    find7(l,i,j,n-1)
    find8(l,i,j,n-1)

def help(l,n):
    for i in range(n):
        for j in range(n):
            if l[i][j]==1:
                call(l,i,j,n)
                break


def queensAttack(n, k, r_q, c_q, obstacles):
    l=[[0]*n for _ in range(n)]
    l[r_q-1][c_q-1]=1
    for i in obstacles:
        l[i[0]-1][i[1]-1]=2
    for i in range(n):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
    help(l,n)

n,k=map(int,input().split())
ro,co=map(int,input().split())
p=[]
for i in range(k):
    p.append(list(map(int,input().split())))
queensAttack(n,k,ro,co,p)
print(c)
