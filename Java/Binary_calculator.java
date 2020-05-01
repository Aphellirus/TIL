import java.util.*;
class cal
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
    int n;
    int p;
    double m=0.0;
    double k;
    int s=0;
    System.out.println("Enter A Number");
    n=sc.nextInt();
    int n1=n;
    while(n1!=0)
    {
      k= Math.pow(10,s);
      p=n1%2;
      m=m+(p*k);
      s=s+1;
      n1=n1/2;
    }
    int l= (int) m;
    System.out.println("The Binary of "+n+" is "+l);
  }
}
