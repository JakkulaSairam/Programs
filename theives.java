/*Brahmi and his gang was chased by group of police officers, unfortunately they 
all got locked up in a building consist of M*N rooms in the form of a grid. 
All the rooms are connected with  the adjacent rooms both horizontally and vertically.
There are few rooms for them to escape called as safe zones. 

Now help Brahmi and his gang to reach the safe zones in the building.

In the Building, the rooms classified as follows:
    -1 -> Danger zone (they should not enter into it).
     0 -> Safe Zone (room to escape)
    -2 -> a thief

Now create a method to print the grid after performing following step: 
Fill each room of the Brahmi and his gang with the distance to its nearest safe zone.
If it is impossible to reach a safezone, fill with '-2' only.

Input Format:
-------------
Line-1 -> two integers M and N, size of the grid of rooms.
Next M Lines -> N space separated integers, from this set [-2,-1,0] only.

Output Format:
--------------
Print an integer as result.


Sample Input-1:
---------------
4 4
-2 -1 0 -2
-2 -2 -2 -1
-2 -1 -2 -1
0 -1 -2 -2

Sample Output-1:
----------------
3 -1 0 1
2 2 1 -1
1 -1 2 -1
0 -1 3 4

*/
import java.util.Scanner;
public class theives{
    static int a[][];
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        int r=sc.nextInt();
        int c=sc.nextInt();
        a=new int[r][c];

        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                a[i][j]=sc.nextInt();
            }
        }
        int count;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                count=0;
                if(a[i][j]==0)
                paths(i,j,count);
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                System.out.print(a[i][j]+" ");
            }
            System.out.println();
        }
        
        sc.close();
    }

    static void paths(int i, int j, int count) {
        if(i<0 || j<0|| i>=a.length||j>=a[0].length){
            return;
        }
        if(a[i][j]==-1)
        return;
        else if(a[i][j]==-2)
        a[i][j]=count;
        else if(a[i][j]>0){
            a[i][j]=Math.min(a[i][j],count);
        }
        if(a[i][j]==count){
            paths(i+1, j, count+1);
            paths(i, j+1, count+1);
            paths(i-1, j, count+1);
            paths(i, j-1, count+1);
        }
        return;
    }
}