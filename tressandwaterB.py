"""
Imagine the field is a 2D plane. Each cell is either water 'W' or a tree 'T'. 
A forest is a collection of connected trees. Two trees are 
connected if they share a side i.e. if they are adjacent to each other.

Your task is, given the information about the field, print the size of the largest forest.

Size of a forest is the number of trees in it. See the sample case for clarity

INPUT:

First line contains the size of the matrix N. 
The next N lines contain N characters each, either 'W' or 'T'.

OUTPUT:

Print the size of the biggest forest.

CONSTRAINTS:

1<=N<=1000

Sample Input
5
TTTWW
TWWTT
TWWTT
TWTTT
WWTTT
Sample Output
10

"""
a=[]
def check(l,i,j,m,n,c,vis):
    
    if i>=m or j>=n or i<0 or j<0 or vis[i][j]==1 or l[i][j]=="W":
        if c not in a:
            a.append(c)
        return 
    vis[i][j]=1
    check(l,i,j+1,m,n,c+1,vis)
    check(l,i+1,j,m,n,c+1,vis)
    check(l,i,j-1,m,n,c+1,vis)
    check(l,i-1,j,m,n,c+1,vis)
def help(l,n):
    vis=[[0]*(n) for i in range(n)]
    ans=[]
    for i in range(n):
        for j in range(n):
            if l[i][j]=="T":
                check(l,i,j,n,n,0,vis)

n=int(input())
l=[]
for i in range(n):
    k=[i for i in input()]
    z=[0 for i in range(n)]
    l.append(k)

help(l,n)
print(max(a))