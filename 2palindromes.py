"""
p,q=map(str,input().split())
n=len(p)
flag=0
for i in range(1,n):
    p1=p[:i]
    p2=p[i:]
    q1=q[:i]
    q2=q[i:]
    if p1+q2==(p1+q2)[::-1] or q1+p2==(q1+p2)[::-1]:
        print("true")
        #print(p1+q2,(p1+q2)[::-1] , q1+p2,(q1+p2)[::-1])
        flag=1
        break
if flag==0:
    print("false")
    """


p, q = map(str, input().split())
n = len(p)
flag = 0
for i in range(1, n):
    p1 = p[:i]
    p2 = p[i:]
    q1 = q[:i]
    q2 = q[i:]
    if p1+q2 == (p1+q2)[::-1] or q1+p2 == (q1+p2)[::-1]:
        print("true")
        #print(p1+q2,(p1+q2)[::-1] , q1+p2,(q1+p2)[::-1])
        flag = 1
        break
if flag == 0:
    print("false")
