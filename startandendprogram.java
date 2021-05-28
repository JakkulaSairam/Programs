import java.util.Arrays;
import java.util.Scanner;

/*[15:36, 26/05/2021] Ramesh clg: Prashanth Varma is working on integer sets.
He is given an Zero-Set ZS of length N, the set conatins only 0's.
Also he is provided with a set of M triplets[], where triplet[i] = [start, end, val].
The triplet contains the following values: start means starting index, 
end menas last index, and val means value to be added.

Prashanth has to perform M operations as follows:
	- He need to read three values from the triplet[i], where 0<= i < M.
	- He needs to add the value of 'val' to all the elements in ZS,
	  between start and end indices, both are inclusive.
	
Your task is to help Prashanth Varma, to perform M operations on ZS
and return the final ZeroSet ZS.

NOTE:
Can you solve the problem in O(n+M) time complexity?

Input Format:
-------------
Line-1: Two space separated integers N and M, size of ZS and number of triplets.
Next M lines: Three space separated integers, the triplets [start, end, val]

Output Format:
--------------
Print the final ZS, after performing M operations.


Sample Input:
-------------
5 3
1 3 2
2 4 3
0 2 -2

Sample Output:
--------------
[-2,0,3,5,3]


Explanation:
------------
Initial state of the ZeroSet is: [0,0,0,0,0]
	- After applying operation [1,3,2] => [0,2,2,2,0]
	- After applying operation [2,4,3] => [0,2,5,5,3]
	- After applying operation [0,2,-2] => [-2,0,3,5,3]
    */

public class startandendprogram {
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        int start,end,value;
        int n=sc.nextInt();
        int m=sc.nextInt();
        int a[]=new int[n];
        for(int i=0;i<m;i++){
            start=sc.nextInt();
            end=sc.nextInt();
            value=sc.nextInt();
            a[start]+=value;
            if(end+1<n)
            a[end+1]+=value*-1;

        }
        int s=0;
        for (int i = 0; i < a.length; i++) {
            s+=a[i];
            a[i]=s;
        }
    System.out.println(Arrays.toString(a));
    sc.close();
    }
    
}
