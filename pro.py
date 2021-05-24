def Solution(A):
    maxi,flag=0,0
    for i in A:
        if -1*i in A and i>maxi:
            flag=1
            maxi=i
    if flag==1:
        return(maxi)
    else:
        return("0")
