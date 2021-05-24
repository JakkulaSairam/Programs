"""Anchal:23581,Aman:57568,Sonakshi:34848
[['Anchal', '23581'], ['Aman', '57568'], ['Sonakshi', '34848']]
# axi
"""

l=list(map(str,input().split(",")))
a=[ i.split(":") for i in l]
print(a)
ans=''
for i in a:
    f=0
    le=len(i[0])
    p=[]
    for j in i[1]:
        p.append(int(j))
    p.sort(reverse=True)
    for k in p:
        if k<=le:
            ans=ans+i[0][k-1]
            f=1
            break
    if f==0:
        ans=ans+'X'
print(ans)
        