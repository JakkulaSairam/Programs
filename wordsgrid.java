/*"""You are given a phrase and a paper of size m*n.
So you can type exactly m * n characters on that paper.
i.e,. there are 'm' rows and in each row you can type 'n' characters
You need to type the phrase on the paper with some rules.

The rules are as follows:
    - A word in the phrase cannot be split into two lines.
    - The order of words in the phrase shuld not change.
    - Two consecutive words in a line must be separated by a single space.

Your task is to find out how many times the phrase can be typed on the paper.

constraint:
	Length of each word is <=10.

Input Format:
-------------
Line-1: Three space separated integers m, n, and s, grid size m*n, number of words.
Line-2: 's' space separated strings, set of words

Output Format:
--------------
Print an integer, no.of times set of words fit into the grid.


Sample Input-1:
---------------
2 8 2
socail distance

Sample Output-1:
----------------
1

Explanation:
------------
social__
distance


Sample Input-2:
---------------
3 6 3
a bc def

Sample Output-2:
----------------
2

Explanation:
------------
a_bc__
def_a_
bc_def
"""
*/
import java.util.*;
class wordPrint{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int m=sc.nextInt(),n=sc.nextInt(),nw=sc.nextInt();
        sc.nextLine();
        String ss[]=sc.nextLine().split(" ");
        int j=0,count=0;
        for (int i = 0; i < m; i++) {
            int k=0;
          //  System.out.println("Line: "+i);
            while(k<n){
                if(k+ss[j].length()<=n){
                   
                    k+=ss[j].length()+1;
                  //  System.out.print(ss[j]+"_"+k);
                    j=(j+1)%nw;
                    if(j==0)count++;
                }else{
                    break;
                }
                
            }
           // System.out.println();
        }
        System.out.println(count);
        sc.close();
    }
}
