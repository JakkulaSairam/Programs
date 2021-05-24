"""from collections import deque
n=int(input())
l=list(map(int,input().split(" ")))
q=int(input())
qu=list(map(int,input().split(" ")))
for i in qu:
    h=deque(l)
    h.rotate(i)
    shifted=list(h)
    l=l+shifted
    print((sum(l)%1000000000)+7)  """
"""
for _ in range(int(input())):
    n=int(input())
    s=input()
    while(s[len(s)-1]=='0'):
        print("loop:",s)
        s=s[:len(s)-2]
    print(s)
    if s.count("1")//2>=n//2:
        print("YES")
    else:
        print("NO")
    """
"""def rotate(l, n):
    return l[n:] + l[:n]
n=int(input())
l=list(map(int,input().split(" ")))
q=int(input())
qu=list(map(int,input().split(" ")))
for i in qu:
    l=l+rotate(l,i)
    print(l)
    print(sum(l))"""

"""
n=int(input())
l=list(map(int,input().split(" ")))
q=int(input())
qu=list(map(int,input().split(" ")))
ls=sum(l)
qs=sum(qu)
li=[ls]
for i in range(len(qu)):
    li.append(li[len(li)-1]*qs)
    print(li[len(li)-1])
"""
"""
n=int(input())
l=list(map(int,input().split(" ")))
q=int(input())
qu=list(map(int,input().split(" ")))
ls=sum(l)
for i in range(len(qu)):
    h=ls*2
    print(h)
    ls=h



"""

t=int(input())
for _ in range(t):
    L=int(input())
    s=input()
    x=s.count('1')
    if (x*100)//L==50:
        print("YES")
    else:
        f=0
        st=s.rstrip('0')
        x=st.count('1')
        if (x*100)//len(st)==50:
            print("YES")
        else:
            print("NO")