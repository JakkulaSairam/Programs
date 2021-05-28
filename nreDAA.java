import java.util.*;
public class listgeneration{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        char in[]=sc.next().toCharArray();
        ArrayList<Integer>res=new ArrayList<Integer>();
        getListUtil(in,res,0);
        System.out.println(res);        
        sc.close();
    }


    

    private static boolean getListUtil(char[] in, ArrayList<Integer> res, int i) {
        if(i==in.length+1 && check(in,res,i))return true;
        if(i>0 && !check(in,res,i))return false;
        for (int j = 1; j <= in.length+1; j++) {
             if(!res.contains(j)){
                    res.add(j);
                   if(getListUtil(in, res, i+1)){
                       return true;
                   }
                   else
                   res.remove(i);
             }
             
        }
        return false;
    
    }

    private static boolean check(char[] in, ArrayList<Integer> res, int i) {
        for (int j = 0; j < i-1; j++) {
            if(in[j]=='D' && res.get(j)<res.get(j+1))return false;
            if(in[j]=='A' && res.get(j)>res.get(j+1))return false;
        }
        return true;
    }
}
