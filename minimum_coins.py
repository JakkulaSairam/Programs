"""Pramod bhaiya of Pramod Juice Centre have coins with denominations 1, 5, and 10. He wants to return the minimum 
number of coins needed to return to his customers as the returning amount.

The goal of this problem is to find the minimum number of coins needed to change the input value i.e the returning 
amount (an integer) into coins with denominations 1, 5, and 10.

Input:
The input consists of a single integer m (the returning amount).
Output:
Print a single line containing one integer ― the minimum number of coins with denominations 1, 5, 10 that changes m.
Constraints
1 ≤ m ≤ 103
Sample Input:
28
Sample Output:
6
EXPLANATION:
Example case 1: 
Pramod bhaiya has to return Rs m=28 to the customer. 
The minimum coins of 1,5 and 10 that can be returned to the customer 10 + 10 + 5 + 1 + 1 + 1, 
so the minimum number of coins to be returned are 6. Hence the output is 6."""
try:
    n=int(input())
    ans=0
    if n%10==0:
        ans=n/10
    else:
        ans=ans+(n//10)
        k=n%10
        if k%5==0:
            ans=ans+(k//5)
        else:
            h=k%5
            ans=ans+(k//5)+h
    print(ans)
except:
    pass
            
            
                