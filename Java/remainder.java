
import java.io.*;
public class Remainder
{
    public static void main(String args[])throws Exception
    {
        DataInputStream a=new DataInputStream(System.in);
         int x,y,z,b,c;
         System.out.println("Enter two numbers");
         x=Integer.parseInt(a.readLine());
         y=Integer.parseInt(a.readLine());
         z=x/y;
         b=y*z;
         c=x-b;
         System.out.println("Remainder-"+c);
     
    }
}
