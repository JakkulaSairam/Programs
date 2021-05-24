"""
Naresh is working on expression of words.
If you give him an expression like, [p,q,r]s[t,u],
Naresh will form the words like as follows : [pst, psu, qst,qsu, rst, rsu]
Another example, [a,b]c[d,e] will be converted as: [acd, ace, bcd, bce].

Naresh will be given an expression as a string EXP, like the above format.
He needs to return all words that can be formed in like mentioned above, 
Can you help Naresh to convert iven expression into a list of words, in lexicographical order.

NOTE: 
Expression consist of lowercase alphabets, comma, and square brackets only.

Input Format:
-------------
A string EXP, expression.

Output Format:
--------------
Print list of words, formed from the expression.


Sample Input-1:
---------------
[b]c[e,g]k

Sample Output-1:
----------------
[bcek, bcgk]


Sample Input-2:
---------------
[a,b][c,d]

Sample Output-2:
----------------
[ac, ad, bc, bd]


Sample Input-3:
---------------
[xyz]a[b,c]

Sample Output-3:
----------------
[xyzab, xyzac]
"""

s=input()
l=[]
k=[]
left,right=-1,-1
for i in range(len(s)):
    if s[i]=='[':
        left=i
    elif s[i]==']':
        right=i
        l.append(s[left+1:right])
        left=-1
    if left==-1 and s[i]!=']':
        k.append(s[i])

h=[]
ans=[]
for i in l:
    h.append(i.split(","))

if len(k)==0:
    for i in h[0]:
        for j in h[1]:
            ans.append(i+j)
    print(ans)
else:
    for i in h[0]:
        for j in h[1]:
            ans.append(i+k[0]+j)
    if len(k)!=1:
        for i in range(len(ans)):
            ans[i]=ans[i]+k[1]
    print(ans)






    
