"""
You are given a set of releases of a software and you are asked to find the most
recent release. There may be multiple checkins of the software in a given branch. 
Each branch may also have sub branches. For example release 3-5-4 refers to the 
fourth checkin in the fifth sub branch of the third main branch. 
This hierarchy can go upto any number of levels. 

If a level is missing it is considered as level 0 in that hierarchy. 
For example 3-5-7 is  same as 3-5-7-0 or even same as 3-5-7-0-0. 
The higher numbers denote more recent releases. 

For example 3-5-7-1 is more recent than 3-5-7 but less recent than 3-6.

Input Format:
-------------
A single line space separated strings, list of releases 

Output Format:
--------------
Print the latest release of the software.


Sample Input-1:
---------------
1-2 1-2-3-0-0 1-2-3

Sample Output-1:
----------------
1-2-3

Sample Input-2:
---------------
3-5-4 3-5-7 3-5-7-1 3-5-7-0-0 3-6

Sample Output-2:
----------------
3-6

"""
"""
s=list(map(str,input().split(" ")))
ans=[]
for i in s:
    k=i.split("-")
    p = int(("".join(k)).strip("0"))
    ans.append(p)
pol=[]
z=str(min(ans))
for i in ans:
    if str(i).startswith(z):
        pol.append(i)
pil=[i for i in str(max(pol))]
print("-".join(pil))

"""


s = list(map(str, input().split(" ")))
ans = []
for i in s:
    k = i.split("-")
    ans.append(int("".join(k)))
maxlen = 0
dict = {}
for i in range(len(ans)):
    if len(str(ans[i])) > maxlen:
        maxlen = len(str(ans[i]))
for i in range(len(ans)):
    ss = ans[i]
    if maxlen-len(str(ans[i])) > 0:
        # print(maxlen-len(str(ans[i])))
        ans[i] = ans[i](10*(maxlen-len(str(ans[i]))))
    if(ans[i] in dict.keys()):
        if(dict[ans[i]] > ss):
            dict[ans[i]] = ss
    else:
        dict[ans[i]] = ss

if(str(max(ans)).rstrip("0") in dict.values()):
    pull = str(max(ans).rstrip("0"))
else:
    pull = str(dict[max(ans)])
print("-".join(pull))
