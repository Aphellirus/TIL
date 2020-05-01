using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
 //Compiler version 4.0, .NET Framework 4.5


 namespace Prime
 {
   public class Program
   {
     public static void Main(string[] args)
     {
       int I; 
       int j=2;
       int ch=0;
       Console.Write("Enter any number ");
       I=Convert.ToInt32(Console.ReadLine());
      while (j<=I/2){
        if (I%j==0){
          Console.Write(I+"Not Prime ");
          ch=1;
          break; 
        }
        else {
          j++;
        }
        
      }
      if(ch==0){
        Console.Write(I+"Prime Number ");
      }
     
      Console.ReadLine();
     }
     
   }

 
}
