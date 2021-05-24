"""
Prof. Neil Gogte asked Mr.Nagi Reddy to create a grid with set of words in
such a way that if you read the word in i-th row and the word in i-th column
should be equal.
Mr. Nagi Reddy created the grid accordingly.

Now it’s your aim to check whether Mr.Nagi Reddy’s grid has satisfied
conditions given by Prof. Neil Gogte.

If satisfied, print "true". Otherwise print "false"

Constraints:
-------------
 N should be a positive integer.
 0 < word[i].length <= N
word[i+1].length <= word[i].length

Input Format:
-------------
Line-1 -> an integer N, number of words
Line-2 -> N space separated words.

Output Format:
--------------
Print a boolean result.


Sample Input-1:
---------------
4
kmit made idol tell

Sample Output-1:
----------------
true

Explanation:
-------------
Given grid looks as follows:
k m i t
m a d e
i d o l
t e l l
if you read the words in every i-th row and i-th column,
both the words are same. so return true.


Sample Input-2:
---------------
5
abcde bcde cde de e

Sample Output-2:
----------------
true
"""


n=int(input())
l=[input() for i in range(n)]
h=[len(i) for i in l]
m=max(h)
for i in range(n):
    while len(l[i])<m:
        l[i]=l[i]+"o"
c=0
for i in range(n):
    for j in range(n):
        if l[i][j]!=l[j][i]:
            c=1
            break
if c==0:
    print("true")
else:
    print("false")

