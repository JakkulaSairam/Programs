"""
Manoj is working on sets and relations.
He is given a set S consist of N integers from 1 to N, without dupliactes.
The set S may contain any shuffled order of 1 to N numbers.
And also P number of subsets also given where each subset of size Q.
Each subset is a subsequence of shuffled set S.

Manoj has to check whether the given subsets can form the set S uniquely or not.
i.e., the order of numbers in the subsets remains unchanged and can form 
only one unique super set using the subsets, and the unique super set should be S.

Your task is to help Manoj to check whether it is possible to form 
the shuffled set S uniquely from the given subsets.

For example: 
-----------
If given shuffled set is [1,2,3] and subsets are [1,2] [1,3].
You can form the following sets, [1,2,3] or [1,3,2].

So, you should return false, as the given subsets form more than 1 set.

Simply, there should be always only one unique super set can be formed.
and that set should be equal to S.


Input Format:
-------------
Line-1: An integer N, size of the shuffled array.
Line-2: N space separated integers, shuffled set S.
Line-3: Two space separated integers P and Q, number of subsets, and size of subsets.
Next P lines: Q space separated integers, non repeated integers from [1-N]

Output Format:
--------------
Print a boolean value, can you form the shuffled set S uniquely or not.


Sample Input-1:
---------------
4
1 3 2 4
3 2
1 2
3 2
3 4

Sample Output-1:
----------------
false

Explanation: 
------------
The subsets are [1,2], [3,2] and [3,4] cannot
form the given shuffled set [1,3,2,4].
It can form another set as [1,3,4,2] also.


Sample Input-2:
---------------
4
1 3 2 4
4 2
1 2
3 2
1 3
2 4

Sample Output-2:
----------------
true

Explanation: 
------------
The subsets are [1,2], [3,2], [1,3] and [2,4] can uniquely 
form the given shuffled set [1,3,2,4].


Sample Input-3:
---------------
5
1 3 5 4 2
3 3
3 4 2
5 4 2
1 3 5

Sample Output-3:
----------------
true

Explanation: 
------------
The subsets are [3,4,2], [5,4,2], and [1,3,5] can uniquely 
form the given shuffled set [1,3,5,4,2].
"""

from itertools import permutations
n=int(input())
l=list(map(int,input().split()))
q,p=map(int,input().split())
qu=[]
for i in range(q):
    qu.append(list(map(int,input().split())))
co=[i for i in range(q)]
com=list(permutations(co,q))
flag=0
for i in range(len(com)):
    ans=[]
    for j in com[i]:
        kil=qu[j]
        for k in kil:
            if k not in ans:
                ans.append(k)
    if ans==l:
        flag=1
        print("true")
        break
if flag==0:
    print("false")