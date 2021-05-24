import java.util.*;
public class nQueen {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int board[][]=new int[n][n];
        if( placeQueens(board,n,0))
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                System.out.print(board[i][j]+" ");   
            }
            System.out.println();
        }
        else {
            System.out.println("No Solution Exist");
        }
        sc.close();
    }

    private static boolean placeQueens(int[][] board, int n,int row) {
      
        if(row==n)return true;
        
            for (int j = 0; j < board.length; j++) {
                
                if(!checkWhetherDanger(board,row,j)){
                    board[row][j]=1;
                   if(placeQueens(board, n, row+1)==true){
                        return true;                 
                   }
                        board[row][j]=0;
                
                }            
                
            
        }
        return false;
        
    }

    private static boolean checkWhetherDanger(int[][] board,int i,int j) {
     
        for (int j2 = i-1; j2 >=0; j2--) {
            if(board[j2][j]==1)return true;   
        }
     
        for (int j2 = i-1,j1=j-1; j2>=0&&j1>=0; j2--,j1--) {
            if(board[j2][j1]==1)return true;
        }
        for (int j2 = i-1,j1=j+1; j2>=0&&j1<board.length;j1++,j2--) {
            if(board[j2][j1]==1)return true;
        }
        return false;
    }
}