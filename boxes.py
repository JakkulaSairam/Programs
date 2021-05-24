""" Vijay is playing with set of boxes, each box is printed a number on it.
all the boxes placed in a row.

You are given the numbers printed on the boxes in the row.
Your task is to find the maximum sum of the numbers when one box is removed 
from the sub-set of boxes, and the sub-set is selected as a contiguous set of 
boxes from the row. 

Note: The sub-set should not be empty after removal of a box.

Input Format:
-------------
Single line of space separated integers, number on the boxes.

Output Format:
--------------
Print an integer, Maximum sum of sub-set of boxes,
after removal of a box.


Sample Input-1:
---------------
-2 -3 4 -1 -2 1 5 -3

Sample Output-1:
----------------
9

Sample Input-2:
---------------
-2 -3 -4 -1 -2 1 5 -3 8

Sample Output-2:
----------------
14 
"""
try:
    l=list(map(int,input().split()))
    n=len(l)
    fw=[0 for i in range(n)]
    bw=[0 for i in range(n)]
    fw[0]=l[0]
    bw[n-1]=l[n-1]
    for i in range(n):
        fw[i]=max(fw[i-1]+l[i],l[i])
    for i in range(n-2,-1,-1):
        bw[i]=max(bw[i+1]+l[i],l[i])
    k=max(max(fw),max(bw))
    i=1
    while i<n-1:
        k=max(fw[i-1]+bw[i+1],k)
        i=i+1
    print(k)
except:
    pass
