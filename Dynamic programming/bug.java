import java.util.*;
 class samosa {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        String s[]= sc.nextLine().split(" ");
        int a[]=new int[s.length];
        int t =sc.nextInt();
        int n=s.length;
     for (int i = 0; i < a.length; i++) {
            a[i]=Integer.parseInt(s[i]);
        }
        Arrays.sort(a);
        if(t==a.length - 1)System.out.println(a[n-1]);
        else System.out.println(getMinSpeed(a,t,1,a[n-1]));
        sc.close();
    }

    private static int getMinSpeed(int[] a, int t, int l, int r) {
       System.out.println(l+" "+r);
        if(r<l)return l;
        if(l==r)
        return l;
        int mid;
        while(l<r){
            mid=l+(r-l)/2;
            if(checkPossible(mid,a,t)){
                return getMinSpeed(a, t, l,mid);
             }else{
                return getMinSpeed(a, t, mid+1, r);
             }
        }
        return l;
    }

    private static boolean checkPossible(int mid,int a[],int t) {
       
        if(mid<=0)return false;
        int c=0;
        for (int i = 0; i < a.length; i++) {
            if(a[i]<=mid)c+=1;
            else{
                c+=a[i]/mid;
                if(a[i]%mid!=0)c+=1;
            }

        }
        return ( c<=t);
    }
}