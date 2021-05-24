"""
You are given a,b and c.You need to convert a to b.
You can perform following operations :-
1) Multiply a by c.
2) Decrease a by 2.
3) Decrease a by 1.
You can perform this operation in any order and any number of times.
You need to find and print minimum number of steps to convert a to b.

Constraints :-



Input : -

First line contains nuber of test cases.

Next  line for contains three space separated integer  .

Output : -

Print minimum no. of steps as output in new line for each test case.

Sample Input
2
3 10 2
11 6 2
Sample Output
3
3
"""
ans=[]
memo={}
def guess(a,b,c,co):
    if c==0 or c==1:
        if a==b:
            ans.append(co)
            return
        if a>b:
            return
        if a<b:
            guess(a,b-1,c,co+1)
            guess(a,b-2,c,co+1)
    else:

        #print("a b",a,b)
        #k=str(a)+str(b)
        if a==b:
            ans.append(co)
            return
        if a>b:
            return
        if a<b:
            guess(a*c,b,c,co+1)
            guess(a,b-1,c,co+1)
            guess(a,b-2,c,co+1)
        return

"""
def check(n,c,i,co):
    if i==n:
        ans.append(co)
        return co
    if i>n:
        return 0
    check(n,c,i*c,co+1)
    check(n,c,i+1,co+1)
    check(n,c,i+2,co+1)"""
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a<b:
        guess(a,b,c,0)
        #print(check(b-a,c,0,0))
    elif a>b:
        guess(b,a,c,0)
        #print(check(a-b,c,0,0))
    else:
        print("0")
        exit(0)
    print(min(ans))