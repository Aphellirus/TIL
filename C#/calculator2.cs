using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
 // Compiler version 4.0, .NET Framework 4.5


 namespace Math
 {
   public class Calculator
   { 
     
     public static void Main(string[] args)
     {
       Start:
       
       Console.WriteLine("Choose a method:");
       Console.WriteLine("1.Basics:");
       Console.WriteLine("2.Power & Square root:");
       Console.WriteLine("3.Trignometry:");
       int c;
       c = Convert.ToInt32(Console.ReadLine());
       if(c == 1){
         Console.WriteLine("1.Add");
     Console.WriteLine("2.Subtract");
     Console.WriteLine("3.Multiply");
     Console.WriteLine("4.Divide");
     Console.ReadKey();
     int z;
     z = Convert.ToInt32(Console.ReadLine());
       Console.WriteLine("Enter First Number:");
     Double x;
     x = Convert.ToDouble(Console.ReadLine());
     Console.ReadKey();
     Console.WriteLine("Enter Second Number:");
     Double y;
     y = Convert.ToDouble(Console.ReadLine());
     Console.ReadKey();
     Console.WriteLine("Result:");
    
    
     if(z == 1){
       Console.WriteLine(x+y);
     }
     else if(z == 2){
       Console.WriteLine(x-y);
     }
     else if(z == 3){
       Console.WriteLine(x*y);
     }
     else if(z == 4){
       Console.WriteLine(x/y);
     }
       
     else{
       Console.WriteLine("Error.");
     }
     Console.ReadKey();
     
     }
     else if(c == 2){
       Console.WriteLine("1.Power.");
       Console.WriteLine("2.Square root");
       int g;
       g = Convert.ToInt32(Console.ReadLine());
     
       if(g == 1){
          double m, n; Console.WriteLine("Enter the Number: "); 
          m = double.Parse(Console.ReadLine()); 
          Console.WriteLine("Enter the Exponent: ");
           n = double.Parse(Console.ReadLine()); 
           double value1 = Math.Pow(m, n); 
           Console.WriteLine(m+" "+ "to power"+" "+n+ " "+"is"+" "+value1);
            Console.ReadKey();  
         
         
       }else if(g==2){
         double m, n; 
         Console.WriteLine("Enter the Number: "); 
         m = double.Parse(Console.ReadLine()); 
         n = 0.5;
      
          double value1 = Math.Pow(m, n);
           Console.WriteLine("Sqaure root of"+" "+m+" "+"is"+" "+ value1);
            Console.ReadKey();
       }
       
   
     }else if (c == 3){
       double h, a, o;
       string k;
       Console.WriteLine("Enter the name of angle:");
       k = Convert.ToString(Console.ReadLine());
       Console.WriteLine("Specify the hypotenuse:");
       h = Convert.ToInt32(Console.ReadLine());
       Console.WriteLine("Specify the adjacent:");
       a = Convert.ToInt32(Console.ReadLine());
       Console.WriteLine("Specify the opposite:");
       o = Convert.ToInt32(Console.ReadLine());
       int i;
       Console.WriteLine("1.Sin" +" "+ (k));
       Console.WriteLine("2.Cos" +" "+ (k));
       Console.WriteLine("3.Tan" +" "+ (k));
       Console.WriteLine("4.Cot" +" "+  (k));
       Console.WriteLine("5.Sec" +" "+ (k));
       Console.WriteLine("6.Csc" +" "+ (k));
       i = Convert.ToInt32(Console.ReadLine());
       Console.WriteLine("Answer:");
       if(i == 1){
         Console.WriteLine(o/h);
         }
         else if(i == 2){
           
         
         Console.WriteLine(a/h);
         }
         else if(i == 3){
           
         
         Console.WriteLine(o/a);
         }
         else if(i == 4){
           
         
         Console.WriteLine(a/o);
         }
         else if(i == 5){
           
         
         Console.WriteLine(h/a);
         }
         else if(i == 6){
          
         
         Console.WriteLine(h/o);
         }
       
     }
     Console.WriteLine("---------------------\n" +
                       "---------------------") ;
     Console.WriteLine("Press 1 to restart or 2 to finish process.");
     int sklolo;
     sklolo = int.Parse(Console.ReadLine());
     if(sklolo==1){
       goto Start ;
       }
       else{
       Console.WriteLine("Thank you!");
     }
    
     
      
       
       
     }
   }
 }
    
