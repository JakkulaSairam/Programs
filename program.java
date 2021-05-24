import java.util.*;

public class program {
    static boolean checkmimeo(String sub){
    //    System.out.println("check: "+sub);
        String s= "";
        s+=sub.charAt(0);
        for (int i = 0; i < sub.length(); i++) {
            if(!s.equals(String.valueOf(sub.charAt(i)))){
                    return false;
            }
        }
        return true;
    }
    static String blast(String s,int n,int i){
      //  System.out.println(s+" "+i);
        if(s.length()==i)return s;
        if(i+n-1<s.length() && checkmimeo( s.substring(i,i+n))){
            String t=s.substring(0,i)+s.substring(i+n,s.length());
            return blast(t,n,0);
        }else{
            return blast(s,n,i+1);
        }
        
        
    } 
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        String s=sc.next();
        int n=sc.nextInt();
        System.out.println(blast(s,n,0));
        sc.close();
    }
}