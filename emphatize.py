s=input()
l=list(map(str,input().split()))
for i in range(len(l)):
    s=s.replace(l[i],"<i>"+l[i]+"</i>")
k=s.replace("</i><i>","")
print(k)
