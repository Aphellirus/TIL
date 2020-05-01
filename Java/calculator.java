import java.util.*;
import java.util.Scanner;

 public class calculator
 {
 public static int add(int a,int b) {   
   int sum = a+b;  
   System.out.println("The sum is\n"  +sum);   
   return 0;
 }
 public static int subt(int a,int b) {   
   int difference = a-b;   
   System.out.println("The difference is\n"   +difference);   
   return 0;
 }
 public static int mul(int a,int b) {   
  int product = a*b;  
  System.out.println("The product is\n"+product);  
  return 0;  
 }
 public static double div(double a,double b){
  double division = a/b;
  System.out.println("The division is\n"+division);
  return 0;
 }
 public static double mod(double a,double b){
   double moddiv = a%b;
   System.out.println("The modulus division is\n"+moddiv);
   return 0;
 }
  public static void main(String args[]) {           
    Scanner input = new Scanner(System.in);    
    
    System.out.println("Enter your choice::\n'1' for Addition\n'2' for Subtraction\n'3' for Multiplication\n'4' for Division");
    System.out.println("'5' for Modulo Division\n'6' for Square Root\n'7' for Cube Root"); 
    System.out.println("'8' for Square\n'9' for Cube");   
    int choice = input.nextInt();
    if(choice == 4) {
      System.out.println("Enter your operands::\n");
      double a = input.nextDouble();
      double b = input.nextDouble();
      div(a,b);
    } 
    else if(choice == 5){
      System.out.println("Enter the operands::\n");
      double c = input.nextDouble();
      double d = input.nextDouble();
      mod(c,d);
    }
    else if(choice == 6){
      System.out.println("Enter the Number\n");
     double e = input.nextDouble();
     System.out.println("The Square Root is::\n"+Math.sqrt(e));
    }
    else if(choice == 7){
      System.out.println("Enter the Number\n");
      double f = input.nextDouble();
      System.out.println("The Cube Root is::\n"+Math.cbrt(f));
    }
    else if(choice == 8){
      System.out.println("Enter the Number\n");
      double g = input.nextDouble();
      System.out.println("The Square is\n"+(g*g));
    }
    else if(choice == 9){
      System.out.println("Enter the Number\n");
      double h = input.nextDouble();
      System.out.println("The Cube is\n"+(h*h*h));
    }
    else if(choice>9||choice<1){
      System.out.println("You entered a wrong choice");  
    }
    else {
          System.out.println("Enter the operands::");   
          int x = input.nextInt();    
          int y = input.nextInt();    
          switch(choice) {      
             case 1:add(x,y);break;      
             case 2:subt(x,y);break;      
             case 3:mul(x,y);break;
             case 4:break;  
             case 5:break;
             case 6:break;
             case 7:break;
             case 8:break;
             case 9:break;
             default:System.out.println("You entered a wrong choice");      
             break; 
          }   
     }   
  }
}
