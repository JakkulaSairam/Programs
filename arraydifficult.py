"""
Shyam is given 3 numbers, where all are > 0. (n,index,Maximum Sum)

He is now supposed to create a group of numbers(nums) by using the following conditions.

nums.length == n
nums[i] is a positive integer where 0 <= i < n .
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1 .
The sum of all numbers of nums does not exceed maxSum .
nums[index] is maximized.

Return nums[index] of the newly constructed array.

Note that abs(x) equals x if x >= 0 , and -x otherwise.

The first line of input contains 'n' followed by 'index' followed by 'maximum sum'

Example 1:
Input: n = 4, index = 2, maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
"""
ans=[]
def check(l,i,m,n):
    if len(l)>=n:
        if sum(l)==m:
            ans.append(l.copy())
            return
        return
    l.append(i)
    check(l,i,m,n)
    l.pop()
    l.append(i+1)
    check(l,i,m,n)
    l.pop()
    return
l=[]
n,inp,m=map(int,input().split())
for i in range(1,n):
    check(l,i,m,n)
ma=0
for i in ans:
    if i[inp]>ma:
        ma=i[inp]
print(ma)

