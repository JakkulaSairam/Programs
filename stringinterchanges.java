/*
Krishna is working on strings, He is trying to modify the string 
which has to be first in lexicographic order.
You can modify the string using following operations:
	- Interchnage the characters at the given pair of indices.
	- You can perform the interchange of the pair any number of times.
	- You will be given I number of pairs

Example: 
--------
If pair is ->[i,j], you can interchange the characters at i-th and j-th indices
with each other.

Krishna is given a String S, an integer I and I pairs of indices.
Can you help Krishna to find the string that can be formed 
after performing interchange operations, which has to be first in the
lexicographical order.

Note: String contains only lowercase letters.


Input Format:
-------------
Line-1: A string S
Line-2: An integer I, number of interchanges.
Next I lines: Two space separated integers, interchange pair.

Output Format:
--------------
A string, lexicographic smallest string after the interchanges


Sample Input-1:
---------------
cba
2
0 1
1 2

Sample Output-1:
----------------
abc

Explaination: 
-------------
Interchange s[0] and s[1], s = "bca"
Interchange s[1] and s[2], s = "bac"
Interchange s[0] and s[1], s = "abc"


Sample Input-2:
---------------
dcab
2
0 3
1 2

Sample Output-2:
----------------
bacd

Explaination: 
-------------
Interchange s[0] and s[3], s = "bcad"
Interchange s[1] and s[2], s = "bacd"


Sample Input-3:
---------------
dcab
3
0 3
1 2
0 2

Sample Output-3:
----------------
abcd

Explaination: 
-------------
Interchange s[0] and s[3], s = "bcad"
Interchange s[0] and s[2], s = "acbd"
Interchange s[1] and s[2], s = "abcd



*/

import java.util.*;
public class stringinterchanges {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        int arr[][] = new int[n][2];
        for (int i = 0; i < n; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }
        List<String> set = new ArrayList<String>();
        set.add(str);
        StringBuilder op = new StringBuilder(str);
        System.out.println(find(arr, n, op, set));
        sc.close();
    }
    public static String find(int[][] arr, int n, StringBuilder op, List<String> set) {
        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder(op);
            char c = sb.charAt(arr[i][0]);
            sb.replace(arr[i][0], arr[i][0] + 1, String.valueOf(sb.charAt(arr[i][1])));
            sb.replace(arr[i][1], arr[i][1] + 1, String.valueOf(c));
            if (!set.contains(sb.toString())) {
                set.add(sb.toString());

                find(arr, n, sb, set);
            
            }
        }
        Collections.sort(set);
        return set.get(0);
    }

}
