/*"""
Ramu is a milk supplier to Somu. He has only two aluminium cups of 
capacity m and n litres. Using these two cups only, he can measure the milk. 
He has to supply exactly P litres of milk to Somu.

To measure the milk, operations allowed are:
	- Fill one of the cups completely with milk.
	- Empty the other cup.
	- Pour milk from one cup into another cup till it fills completely,
	 or the first cup itself is empty.
	 
Such that, at the end one or both cups contains P litres of the milk.
	
Please help Ramu, to check whether P litres of milk can be measured
using the two cups or not.

Input Format:
-------------
3 space separated integers, m, n and P.

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
3 5 4

Sample Output-1:
----------------
true


Sample Input-2:
---------------
2 4 5

Sample Output-2:
----------------
false
""" */
import java.util.Scanner;
public class milk {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int m=sc.nextInt();
        int n=sc.nextInt();
        int p=sc.nextInt();
        int f=0;
        if(m>p||n>p){
            f=1;
        }
        if(n<p && m<p){
            if(m>n){
                while(m!=p){
                    n--;
                    m++;
                }
                if(n==0||(n==p &&m==p))f=1;
            }
            if(n>m){
                while(n!=p){
                    m--;
                    n++;
                }
                if(m==0||(n==p &&m==p))f=1;
            }
        }
        if(f==1)System.out.println(true);
        else System.out.println(false);
        sc.close();
    }  
}