""" CodeChef Chapter is organizing a community gets together. The community manager wants to serve pizza to every student of the community. The executive members are asked to go to the nearest restaurant and get P(P≤ 1000) pizzas packed for the function. The restaurant has L cooks(L ≤ 50) and each cook has a rank R(1 ≤ R ≤ 8). A cook with a rank R can cook 1 pizza in the first R minutes 1 more pizza in the next 2R minutes, 1 more pizza in 3R minutes, and so on(he can only cook a complete pizza)

For example, if a cook is ranked 2, he will cook one pizza in 2 minutes one more pizza in the next 4 mins a one more in the next 6 minutes hence in a total of 12 minutes he cooks 3 pizzas in 13 minutes also he can cook only 3 pizzas as he does not have enough time for the 4th pizza.
The manager wants to know the minimum time to get the order done. Can you help him out?

Input:
First-line will contain T, the number of test cases. Then the test cases follow.
Each test case contains of two lines of input.
In the first line of the test case we have P the number of pizza ordered.
In the next line the first integer denotes the number of cooks L and L integers follow in the same line each denoting the rank of a cook.
Output:
For each test case, print an integer that tells the number of minutes needed to get the order done.

Constraints
1≤T≤100
1≤P≤103
1≤L≤50
1≤R≤8
Sample Input:
  3
  10
  4 1 2 3 4
  8
  1 1
  8
  8 1 1 1 1 1 1 1 1
Sample Output:
  12
  36
  1"""
n=int(input())
l=list(map(int,input().split()))
h=[]
for i in range(len(l)):
    k=[]
    p=l[i]
    k.append(l[i])
    for j in range(2,n+2):
            k.append(k[len(k)-1]+j*p)
    h.append(k)
print(h)
ans=0
pizza=0
while(pizza<n):
    ans=ans+1
    for i in h:
        if ans in i:
            pizza=pizza+1
    #print("pizza",pizza)
print(ans)