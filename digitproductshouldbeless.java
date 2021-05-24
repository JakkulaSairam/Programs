/** 
 * Cardano is a famous mathematician. working on numbers.
Given a number N, which is the product of all the digits of a number.
You need to find such smallest number S.

Your task is to help Mr Cardano to find smallest number S, 
where the product of all the digits of S should be equal to N.
If it is not possible to create S with in range of integer, print 0.


Input Format:
-------------
An integer N

Output Format:
--------------
Print an integer, smallest number S.


Sample Input-1:
---------------
36

Sample Output-1:
----------------
49


Sample Input-2:
---------------
147

Sample Output-2:
----------------
377


Sample Input-3:
---------------
22

Sample Output-3:
----------------
0


 * 
 */
import java.util.*;
public class digitproductshouldbeless {
    public static void main(String[] args) {
       Scanner sc= new Scanner(System.in);
       int n=sc.nextInt();
       System.out.println(getSmallest(n));
       sc.close(); 
    }
    public static int getSmallest(int n) {
        int num = n;
        int prod=1;
        do {
            prod = prodDigits(num);

           if(prod>=100000)return 0;
            num++;
        } while(prod != n);
        return num-1;
    }

    public static int prodDigits(int num) {
        int prod = 1;
        while(num != 0) {
            prod *= num%10;
            num/=10;
        }
        return prod;
    }
}
