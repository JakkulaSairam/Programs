
/*Shaggy Rogers is working with numbers.
He is given a number N, 
He wants to replace all occurrences of a digit in the number N,
with another digit between [0-9]. May be with same number too.

But there should not be any leading zeros in the number after the replacement,
Or the number should not become zero.

Rogers can perform the replacement of the occurrences of the digit in N for two 
times, He will generate two new numbers P and Q, such that the value of |P-Q| 
should be Maximum.

Your task is to help Shaggy Roers to find the maximum difference of P and Q possible.


Input Format:
-------------
An integer N, the number

Output Format:
--------------
Print an integer, the maximum difference of P and Q


Sample Input-1:
---------------
123

Sample Output-1:
----------------
820

Explanation:
------------
Replacement-1: replace 1 with 9 you will get P as 923
Replacement-2: replace 2 with 0 you will get Q as 103
So Max difference is 820.


Sample Input-2:
---------------
4254

Sample Output-2:
----------------
8008

Explanation:
------------
Replacement-1: replace 4 with 9 you will get P as 9259
Replacement-2: replace 4 with 1 you will get Q as 1251
So Max difference is 8008.*/

/*ans=[]
def call(a, i):
    s = "".join(a)
    s = s.replace(s[i], '0')
    ans.append(int(s))
n=input()
l=[i for i in str(n)]
k=l.copy()
if l[0]=='9':
    for i in range(len(l)):
        if l[i]=='9':
            continue
        else:
            s1="".join(l)
            s1=s1.replace(s[i],'9')
            break
else:
    s1 = "".join(l)
    s1 = s1.replace(s1[0], '9')

m=int(s1)
ansma=[]

if k[0]=='1':
    for i in range(1,len(l)):
        call(k,i)
else:
    s2="".join(k)
    s2=s2.replace(s2[0],'1')
    ans.append(int(s2))
mi=max(ans)
print(ans)
for i in range(len(ans)):
    if len(str(ans[i]))==len(k) and mi>ans[i]:
        print(ans[i])
        mi=ans[i]
print(m-mi)
*/
import java.util.*;

public class numberdiiferencebyreplacing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int fmax = 0;
        int fmin = 0;
        int min = 0;
        int max = 0;
        if (s.charAt(0) != '1') {
            min = Integer.parseInt(s.replace(s.charAt(0), '1'));
            fmin = 1;
        }
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != '9' && fmax == 0) {
                max = Integer.parseInt(s.replace(s.charAt(i), '9'));
                fmax = 1;
            }
            if (fmin == 0 && s.charAt(i) != '0') {
                if (!s.replace(s.charAt(i), '0').startsWith("0")) {
                    min = Integer.parseInt(s.replace(s.charAt(i), '0'));
                    fmin = 1;
                }
                if (fmax == 1 && fmin == 1)
                    break;
            }
        }
        System.out.println(max - min);
        sc.close();
    }
}
