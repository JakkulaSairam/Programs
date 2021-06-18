import java.util.Scanner;

/*There are N celebrities participated in Go-Green Campaign,
All of them joined together and each one planted a tree on a flat land
at different positions.
 
Now, your task is to find the maximum number of trees in single straight line.

Input Format:
-------------
Line-1 -> An integers N, number of trees planted.
Next N lines -> Two space separated integers, position of the tree.

Output Format:
--------------
Print an integer as result.


Sample Input:
-------------
6
1 1
3 2
5 3
4 1
2 3
1 4

Sample Output:
--------------
4

Explanation:
------------

    Y
    |
    |	"
    | 		"			"
    |			"
    |	"			"	
    ------------------------- X
    0   1   2   3   4   5*/


class longestconsecutiveones {
        static int longestLine(int[][] M) {
            int l = M.length;
            if (l == 0)
                return 0;
            int w = M[0].length;
            int horizen[] = new int[w];
            int ver = 0;
            int dia[] = new int[l + w - 1];
            int anti[] = new int[l + w - 1];
            int result = 0;
            for (int i = 0; i < l; i++) {
                ver = 0;
                for (int j = 0; j < w; j++) {
                    if (M[i][j] == 1) {
                        horizen[j]++;
                        ver++;
                        dia[i + j]++;
                        anti[l - 1 - (i - j)]++;
                    } else {
                        result = Math.max(ver, result);
                        ver = 0;
                        result = Math.max(horizen[j], result);
                        horizen[j] = 0;
                        result = Math.max(dia[i + j], result);
                        dia[i + j] = 0;
                        result = Math.max(anti[l - 1 - (i - j)], result);
                        anti[l - 1 - (i - j)] = 0;
                    }

                }
                if (ver > 0) {
                    result = Math.max(ver, result);
                }
            }

            for (int i = 0; i < w; i++) {
                result = Math.max(horizen[i], result);
            }
            for (int i = 0; i < w + l - 1; i++) {
                result = Math.max(anti[i], result);
                result = Math.max(dia[i], result);
            }

            return result;

        }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int k=sc.nextInt();
        int a[][]=new int[k][k];
        String s[];
        for (int i = 0; i < k; i++) {
         s=sc.nextLine().split(" ");
             int p=Integer.parseInt(s[0]);
             int q=Integer.parseInt(s[1]);
             a[p][q]=1;
         
        }
                

        System.out.println(longestLine(a));
        
    }
}
