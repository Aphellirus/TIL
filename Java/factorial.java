import java.util.Scanner;
class factorial
{
  public static void main(String [] args)
  {
    Scanner sc=new Scanner(System.in);
    long a=1,b=1,c;
    System.out.print("enter a number of which you want the factorial:");
    c=sc.nextLong();
    while(a<=c)
    {
      b=b*a;
      a++;
    }
    System.out.println("the factorial of the number:"+b);
  }
}
