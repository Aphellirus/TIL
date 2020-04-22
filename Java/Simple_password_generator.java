import java.util.*;
public class Main
{
    char[] password(int n){
        
    char [] a=new char[n];
        String s="0123456789";
        String p="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String t="abcdefghijklmnopqrstuvwxyz";
        String q="!@#$%^&*~";
        String j=s+p+t+q;
        Random r=new Random();
        for(int i=0;i<n;i++)
        {
            a[i]=j.charAt(r.nextInt(j.length()));
        }
        return a;
    }
    public static void main(String[] args) {

    Main o =new Main();
    System.out.println(o.password (8));
    }
}
