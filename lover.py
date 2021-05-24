"""Sham wants to express his Love. For that, he has to reach exactly at some particular place. The distance of that place from his current location is D . He can reach there by taking a jump of distance k or k−1.

You have to say whether he can reach at that particular position using the jumps of described length.

Input:
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, two integers D,K.
Output:
For each testcase, output in a single line "YES" if possible else "NO" if not possible.

Constraints
1≤T≤1000
2≤D,K≤105
Sample Input:
1
7 3
Sample Output:
YES
EXPLANATION:
He will first take the Jump of distance 2 then 3 then 2.
"""
def posible(n,l,memo={}):
    if n in memo.keys():
        return memo[n]
    if n<0:
        return False
    if n==0:
        return True
    for i in l:
        j=n-i
        if posible(j,l,memo):
            memo[n]=True
            return True
    memo[n]=False
    return False

n,k=list(map(int,input().split()))
h=[k,k-1]
print(posible(n,h))