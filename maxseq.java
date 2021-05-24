/*Ashok is given an array of integers nums.
His task is to find the longest contiguous subsequence S, 
the product of all the numbers in the subsequence should be positive.

Return the length of longest contiguous subarray.

Input Format:
-------------
Space separated integers nums[], list of numbers.

Output Format:
--------------
Print the length of the longest contiguous subsequence


Sample Input-1:
---------------
1 -1 2 -2

Sample Output-1:
----------------
4


Sample Input-2:
---------------
-1 -2 -3 0 1

Sample Output-2:
----------------
2

Explanation:
------------
0 is considered as positive number.


Sample Input-3:
---------------
1 2 3 4 -5 6  7 8

Sample Output-3:
----------------
4*/

import java.util.*;
public class maxseq{
    static ArrayList<Integer>res;
    public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        res=new ArrayList<>();
        String s=sc.nextLine();
        if(s.indexOf("0")>0 && CheckZeroExiztense(s)){
            String words[]=s.split(" 0");
            int c=0;
            for(String ss:words){
                
                 String tt[]=ss.split(" ");
                 if(c>0){
                        String t[]=new String[tt.length-1];
                        int k=0;
                        for (int i = 1; i < tt.length; i++) {
                            t[k++]=tt[i];
                            
                        }
                        getLongestSubLen(t);
                 }else{
                    getLongestSubLen(tt);
                 }

                
                c++;
            }
            
            
            
        }else{
            System.out.println(s);
             String ss[]=s.split(" ");
             getLongestSubLen(ss);
        }
        System.out.println(Collections.max(res));
        sc.close();
    }
    
    private static boolean CheckZeroExiztense(String s) {
        for (String t : s.split(" ")) {
            if(t.equals("0"))return true;
        }
        return false;
    }

    public static void getLongestSubLen(String ss[]){
       
        int a[]=new int[ss.length];
        int fni=-1;
        int negcount=0;
        int i=0;
        System.out.println(Arrays.toString(ss));
        for(String t:ss){
           
            a[i]=Integer.parseInt(t);
            if(a[i]<0){
                negcount++;
                if(fni==-1)fni=i;
            }
            i++;
        }
        if(negcount%2==0){
            res.add(ss.length);
        }else{
          /*  String left[]=new String[0+fni];
            String ryt[]=new String[ss.length-left.length];
            for(int k=0;k<fni;k++){
                left[k]=ss[k];
            }
            for(int k=fni;k<ss.length;k++){
                ryt[k]=ss[k];
            }
            
            getLongestSubLen(left);
            getLongestSubLen(ryt);*/
            
     //   System.out.println("odd negcount: "+fni+ " "+Arrays.toString(ss)+" "+(0+fni)+" "+(ss.length-fni-1));
            res.add(Math.max(0+fni,ss.length-fni-1));
        }
    }
    
}