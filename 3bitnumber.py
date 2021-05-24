ans1=[]
def called(l,n,i):
    if i==n:
        ans1.append(l)
        return
    l[i]=0
    called(l,n,i+1)
    l[i]=1
    called(l,n,i+1)
    return

n=int(input())
l=[0]*(n)
called(l,n,0)