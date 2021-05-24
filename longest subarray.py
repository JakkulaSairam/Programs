"""
Ismart Shankar is given a set of N pluck cards, each card labelled a number on it
and he is also given a difference value as ‘D’.
Now Ismart Shankar has to find out the length of the largest arithmetic set ‘S’.

A subset is called as arithmetic set, iff the difference between the numbers on 
any two adjacent cards is same as D.

A subset can be derived from the set of N pluck cads by deleting some or no cards 
without changing the order of the remaining cards.

Input Format:
------------- 
Line-1: Two space separated integers N, D, number of cards, difference.
Line-2: N space separated integers, numbers on the set of cards.

Output Format:
--------------
Print an integer, length of longest arithmetic subset.


Sample Input-1:
---------------
6 2
1 2 3 4 6 8

Sample Output-1:
----------------
4


Sample Input-2:
---------------
8 -2
8 1 2 6 5 4 2 0 

Sample Output-2:
----------------
5
"""

n,c=list(map(int,input().split()))
a=list(map(int,input().split()))
b=[0 for i in range(n)]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[j]-a[i]==c:
            b[i]+=1
            b[j]+=1
print(b)
print(n-max(b))
