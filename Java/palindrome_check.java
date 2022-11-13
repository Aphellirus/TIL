import java.util.*;
public class k
{
    public static void main(String args[]){
        int n,r,i,rev=0;
        Scanner sc=new Scanner (System.in);
        n=sc.nextInt();
        for(i=n;i!=0;i=i/10)
        {
            r=i%10;
            rev =rev*10+r;
        }
        if (n==rev)
        {
            System.out.println("The number is not a palindrome.");
            
        }
        else
        {
            System.out.println("The number is a palindrome.");
        }
    }
}
