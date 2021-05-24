"""
Pabbi wants to play a game with his little brother, Mouk. The game starts with an array of distinct integers and the rules are as follows:

Mouk always plays first.
In a single move, a player chooses the maximum element in the array. He removes it and all elements to its right. For example, if the starting array array = [2,3,5,4,1], then it becomes array' = [2,3] after removing [5,4,1].
The two players alternate turns.
The last player who can make a move wins. Pabbi and Mouk play g games. Given the initial array for each game, find and print the name of the winner on a new line. If Pabbi wins, print PABBI; if Mouk wins, print MOUK.
To continue the example above, in the next move Pabbi will remove 3. Mouk will then remove 2 and win because there are no more integers to remove.

Input Format

The first line contains a single integer g, the number of games.

Each of the next g pairs of lines is as follows:

The first line contains a single integer, n, the number of elements in array.
The second line contains n distinct space-separated integers array[i] where 0<=i
Constraints

Array array contains n distinct integers. For 35% of the maximum score:
1<=g<=100
1<=n<=1000
1<=array[i]<=10^5
The sum of n over all games does not exceed 1000. For 100% of the maximum score:

1<=g<=100
1<=n<=10^5
1<=array[i]<=10^9
The sum of n over all games does not exceed 10^5.

Output Format

Print out a string either "PABBI" or "MOUK"(excluding the double quotes) on each of the g consecutive lines.

Sample Input 0

2
5
5 2 6 3 4
2
3 1
Sample Output 0

PABBI
MOUK
Sample Input 1

2
5
1 3 5 7 9
5
7 4 6 5 9
Sample Output 1

MOUK
PABBI"""

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split(" ")))
    c=0
    while(n>0):
        k=max(l)
        h=l.index(k)
        m=len(l[h:])
        l=l[:h]
        n=n-m
        c=c+1
    if c%2==0:
        print("PABBI")
    else:
        print("MOUK")