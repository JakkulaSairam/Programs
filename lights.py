"""
chef wants to turn on all the light in all N floors.
But chef doesn't want to climb stairs.

N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring
, a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all
 bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same 
 switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Input Format

First line contains an integer N.
Next line contains N binary integers (0 or 1).

Constraints

1 <= N <= 105

Output Format

Output the minimum number of switches you'll need to press.

Sample Input 0

4
0 1 0 1
Sample Output 0

4
"""

#n=int(input())
l=list(map(int,input().split()))
n=len(l)
k=[0]*n
if l[0]==0:
        k[0]=1
else:
        k[0]=0
for i in range(1,n):
    if l[i]==1:
        if k[i-1]%2!=0:
            k[i]=k[i-1]+1
        else:
            k[i]=k[i-1]
    elif l[i]==0:
        if k[i-1]%2==0:
            k[i]=k[i-1]+1
        else:
            k[i]=k[i-1]
        
print(k[n-1])
print(n)