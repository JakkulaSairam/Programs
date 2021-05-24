"""
You've been given a permutation of containing N distinct elements between 1 and N, both included. (1<=N<=10^3)
The rank of an element in this array is the number of elements to it's left which are strictly lesser than it.
You have been given array,formulate it's rank array.
Seems tough right? Let's make the question a bit simpler :P

Instead of the actual array, you would be given a rank array. Formulate the initial array from it. It is guaranteed that the solution would be unique.

Input Format
In the first line input N(1<=N<=10^3)
In the next line input rank array 0<=Rank[i]

Output Format
Print the N integers of the actual array.

NOTE : All elements in the rank array may or may not be distinct

Sample Input 0

3
0 1 2
Sample Output 0

1 2 3
Explanation 0

If the actual array is : 1 2 3
Rank array will be : 0 1 2 Thus it satisfies the provided input.
Because there are 0 elements to the left of 1 which are lesser than 1, 1 element to the left of 2 which is lesser than 2 and 2 elements to the left of 3 which are lesser than 3.
"""
n=int(input())
l=list(map(int,input().split()))
k=[0 for i in range(len(l))]
m=len(set(l))
while(len(l)!=0 and m!=0):
    h=max(l)
    for i in range(l.count(h)):
        inde=l.index(h)
        l[l.index(h)]=-1
        k[inde]=str(m)
    m=m-1
print(" ".join(k))