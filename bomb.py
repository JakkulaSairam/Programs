"""Major Ajay Krishna and Prasad garu are working on a military operation at 
Himachal Pradesh. They are given an operation to defuse the bomb, and they have 
time falling short.

Their informer will provide them with a round-shape lock of length ‘L’, 
where L number of integers on the lock and a clue ‘C’.

To defuse the bomb they have to restore the original state of the lock, 
by restoring every integer on lock. All the integers must be restored in the 
same way based on the clue.

Its your task to help Major Ajay Krishna, to restore the original code on the lock, 
to defuse the bomb.

To restore the lock to its original state, you have to follow these instructions:
	- If C > 0, restore every i-th number with the sum of the next C integers.
	- If C < 0, restore every i-th number with the sum of the previous C integers.
	- If C == 0, restore every i-th number with 0.
	
As the lock is in round shpae, the next element of lock[n-1] is lock[0], 
and the previous element of lock[0] is lock[n-1].


Input Format:
-------------
Line-1: Two space separated integers L, C.
Line-2: L space separated integers, integers on the Lock.

Output Format:
--------------
Print the original state of the lock.


Sample Input-1:
---------------
5 2
2 5 9 4 7

Sample Output-1:
----------------
[14, 13, 11, 9, 7]


Sample Input-2:
---------------
5 0
1 5 6 3 2

Sample Output-2:
----------------
[0, 0, 0, 0, 0]
"""
l,c=list(map(int,input().split()))
a=list(map(int,input().split()))
b=[]
h=a
h.extend(a)
for i in range(0,l):
    if c==0:
        b.append(0)
    if c>0:
        k=h[i+1:i+1+c]
        b.append(sum(k))
    if c<0:
        m=i+len(a)
        k=h[m-c:m]
        b.append(sum(k))
print(b)


"""
import java.util.*;
class Time
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int l = sc.nextInt();
        int c = sc.nextInt();
        int arr[] = new int[l];
        for(int i = 0; i < l; ++i){
            arr[i] = sc.nextInt();
        }
        int op[] = new int[l];
        int flag = 0;
        if(c > 0)
        {
            
            for(int i = 0;i < l;i++)
            {
                int t = 0;
                for(int j = i+1;j <= i+c;j++)
                {
                    t += arr[j%l];
                }
                op[i] = t;
            }
        }
        else if(c < 0)
        {
            for(int i = 0;i < l;i++)
            {
                int t  = 0;
                int p = 2 * l + i + c ;
                //System.out.println(p) ;
                for(int j = p;j < p+Math.abs(c);j++)
                {
                //System.out.print(j + " ") ;
                t += arr[j % l];
                }
                //System.out.println() ;
                op[i] = t;
            }
        }
        else{
            flag = 1;
        }
        for(int i = 0;i < l;i++)
        {
            System.out.print(op[i]+" ") ;
        }
    }
}"""