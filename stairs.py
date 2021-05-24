"""
Simran is running up a staircase with N steps, and can hop(jump) either 1 step, 2 steps or 3 steps at a time.You have to count, how many possible ways Simran can run up to the stairs.

Input Format:
Input contains integer N that is number of steps

Output Format:
Output for each integer N the no of possible ways w.

Constraints

 

 

Sample Input
4
Sample Output
7
"""
"""memo={}
def check(n,i):
    if n==i:
        return 1
    if i>n:
        return 0
    return check(n,i+1)+check(n,i+2)+check(n,i+3)
n=int(input())
print(check(n,0))"""

n=int(input())
l=[0]*(n+1)
l[1]=1
l[2]=2
l[3]=4
for i in range(4,n+1):
    l[i]=l[i-1]+l[i-2]+l[i-3]
print(l[n])