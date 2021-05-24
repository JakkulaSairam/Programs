"""
Kiran is given a string S, and an integer N.
Kiran wants to find the longest substring which has following properties:
	- the substring of S should be maximum in length, and 
	- should contains atmost N distint characters in it.
	
Can you help Kiran to find the longest substring 'ls' with above properties,
and return the length of the substring 'ls'.

Input Format:
-------------
Line-1: A string S
Line-2: An integer N, number of distinct characters.

Output Format:
--------------
Print an integer, lenth of longest substring with atmost N distinct characters.


Sample Input-1:
---------------
philippines
3

Sample Output-1:
----------------
6

Sample Input-2:
---------------
abaccdbcca
2

Sample Output-2:
----------------
3
"""
s=input()
n=int(input())
p=[]
ans=[]
for i in range(len(s)):
    l=[]
    j=i
    s1=""
    while(len(set(l))<=n and j<len(s)):
        s1=s1+s[j]
        l.append(s[j])
        j=j+1
    p.append(l)
    ans.append(len(s1))
#print(p)
print(max(ans)-1)

"""
import java.util.*;
class slidingwindow{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        String s=sc.next();
        int dist=sc.nextInt(); 
        int max=-1;
        ArrayList<Character>list;
        for (int i = 0; i < s.length(); i++) {
            int c=dist-1;
            list=new ArrayList<>();
            list.add(s.charAt(i));
            for (int j = i+1; j < s.length(); j++) {
                if(!list.contains(s.charAt(j))&&c!=0){
                    c--;
                    list.add(s.charAt(j));
                }
                else if(list.contains(s.charAt(j))){
                    list.add(s.charAt(j));
                }
                if(!list.contains(s.charAt(j))){
                    if(c==0){
                        break;
                    }
                }
                
                //System.out.println(s.substring(i,j+1)+" "+list);
            }
            if(list.size()>max)
            max=list.size();
        }

        System.out.println(max);
        sc.close();
    }
}
"""



