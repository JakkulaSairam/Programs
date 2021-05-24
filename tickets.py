l=list(map(str,input().split()))
k=l.index('BZA')
if k==0:
    h=set(sorted(l[1:]))
else:
    m=sorted(l[0:k])
    n=sorted(l[k+1:])
    h=['BZA']
    for i in m:
        if i not in h:
            h.append(i)
    for j in n:
        if j not in h:
            h.append(j)
print(h)
