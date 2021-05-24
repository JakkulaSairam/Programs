"""
Deepthi loves cruises and she runs a catering service on Cruises. The cruise she is onboard today is going to Africa and her job is to prepare lunch for all the passengers onboard on the cruise. She has given an ID number to each of the food items she can prepare, each ID number is denoted by an integer.

The cruise manager provides her with the number of food items a meal box can hold. A meal box contains exactly A food items. She has a list of food items with her denoted by an integer array B. A lunch box can contain multiple same kinds of food items but the content of each lunch box should be the same.

Your task is to help her assist her with the maximum number of lunchboxes she can prepare of the same type containing the same food ID.

Input:
First argument of input is an integer A
Second argument of the input sequence of integers for the array B
Output:
Return a single integer denoting the maximum number of lunch boxes that can be prepared.
Constraints
1≤A≤B.length≤100000
1≤B[i]≤100000
Sample Input:
3
1 2 3 2 6 1 3
Sample Output:
2
EXPLANATION:
She can choose the content to be [1, 2, 3] and prepare 2 lunchboxes."""
from collections import Counter
try:
    n=int(input())
    l=list(map(int,input().split()))
    d=Counter(l)
    lh=d.values()
    k=Counter(lh)
    ans=0
    for i,j in k.items():
        if j==n:
            ans=i
            break
    print(ans)
except:
    pass
    