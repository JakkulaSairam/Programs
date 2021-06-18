l=list(map(str,input().split()))
arr=list(map(str,input().split()))
for i in l:
    if all( j in arr for j in i ):
        print(i)
    