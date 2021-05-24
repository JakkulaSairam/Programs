"""
Somesh is working on Number Strings.
He got an idea to find the smallest possible number by 
deleting some digits from the number without changing 
the relative order of digits in it.

You will be given a integer String 'num', and an integer n.
Find the smallest number possible after deleting n digits from 'num'.

Note: If the number string 'num' turns to empty, print 0.

Input Format:
-------------
Line-1 : A string num, consist of digits only.
Line-2 : An integer n, number of digits to delete.

Output Format:
--------------
Print the smallest possible number.


Sample Input-1:
---------------
1432219
3

Sample Output-1:
----------------
1219

Explanation: 
------------
Delete the three digits 4, 3, and 2 to form the smallest number 1219.

Sample Input-2:
---------------
10200
1

Sample Output-2:
----------------
200

Explanation:
------------
Delete the leading 1 and the smallest number is 200. 
Note that the output must not contain leading zeroes
"""
s=input()
l=[int(i) for i in s]
n=int(input())
k=[]
k.append(l[0])
i,j,top=0,1,0
while(i<n and j<len(l)):
    if k[top]<l[j]:
        k.append(l[j])
        j+=1
        top+=1
    else:
        k[top]=l[j]
        j+=1
        i+=1
pil=k+l[j:]
while pil[0] == 0 :
    pil = pil[1:]
ans=[str(m) for m in pil]
print(''.join(ans))