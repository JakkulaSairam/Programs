"""
Problem Statement: There is a unique ATM in Wonderland. Imagine this ATM as an array of numbers. You can withdraw cash only from either ends of the array. Sarah wants to withdraw X amount of cash from the ATM. What are the minimum number of withdrawals Sarah would need to accumulate X amount of cash. If it is not possible for Sarah to withdraw X amount , return -1.
Input Format: The first line contains an integer N, denoting the number of elements in ATM.
Each line I of  the N subsequent lines (Where 0 <= I <N) contains an integer describing the cash in ATM.
The next line contains an integer X, denoting the total amount to withdraw.
Constrains:
1 <= N <= 10^5
1 <= ATM[i] <= 10^5
1 <= X <=10^5
Sample Input/Output:
Sample Input	Sample Output	Explanation
2 1 1 3	-1	The total amount of cash in the ATM is 2, hence Sarah cannot withdraw an amount of 3.
Let’s understand the problem first: In this problem you have given a ATM as a array of numbers every element in the array is the amount of money that can be withdrawn at a particular time. A person can withdraw money from either of the both ends of the array. You can’t take any fractional amount and in this problem the main objective is to get the minimum no of withdrawals to withdraw a certain amount of money from the ATM now understand it with a example.

Suppose the array is [1, 1, 1, 1, 1, 3, 2, 2]. And we want to withdraw 5 . we can withdraw from any side of end. Let’s attempt it from the end side after withdrawing 3 times we get amount of 7. But we can’t get 5. Important thing we can not take 1 from 3 to make it 5. So by attempting from end side we can’t get 5. Now lets try it from start end. After withdrawing 5 times we get 5.

But there is another way to make 5. We can withdraw amount 4 from end side and amount 1 from beginning of the array to make total amount of 5 . 5=2+2+1.

But in this way we need only 3 withdrawals to make it 5. So minimum withdrawals needed is 3.  
Tricks to solve the problem: First try to make the desired amount from one side of the array. Then check whether amount can be withdrawal from that side and if possible then store the no of withdrawals required.

Then start adding from the other side removing one by one elements from the firstly chosen side. Means we will remove elements from the first side and start adding elements from the other side until all the elements of the beginning side is removed in this process continue checking the no of withdrawals and compare with the minimum value of withdrawals. It will be more clear if you observe the code.

Before moving to the solution we recommend you to attempt the problem first from yourself then move to the solution part.
Here, is our solution to the answer in Python."""
a=int(input())
b=[]
 
for i in range(a):
    temp=int(input())
    b.append(temp)
 
c=int(input())
if(sum(b)<c):
    print(-1)
    exit(0)
 
d=b[::-1]
sum1=0
i=0
j=0
minv=99999
 
while(i<len(b) and sum1<=c):
    sum1=sum1+b[i]
    i=i+1
i=i-1
r=i+1
flag=0
 
if(sum1==c and r<minv):
    flag=1
    minv=r
 
while(1):
    if(j<len(b) and sum1+d[j]<=c):
        sum1=sum1+d[j]
        j=j+1
        r=r+1
    elif(i>=0):
        sum1=sum1-b[i]
        i=i-1
        r=r-1
    else:
        break
    if(sum1==c and r<minv):
        minv=r
 
if(sum1==c and r<minv):
    minv=r
if(minv==99999):
    print(-1)
else:
    print(minv)