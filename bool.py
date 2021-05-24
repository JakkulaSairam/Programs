"""You are provided a string of characters(lowercase only),
You can change the order of the characters of the string.
After changing the order, the resultant string should be 
no two immidiate characters equal.

Return true, if you are able to find such resultant string, 
Otherwise false.

Input Format:
-------------
A String S

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
aaabd

Sample Output-1:
----------------
true

Sample Input-2:
---------------
aaab

Sample Output-2:
----------------
false"""

s=input()
d={}
for i in range(len(s)):
    d[s[i]]=s.count(s[i])
c=0
k=0
h=len(d.values())
for p,v in d.items():
    if v==1:
        c=c+1
    else:
        k=k+v
if k-c==1:
    print("true")
else:
    print("false")

