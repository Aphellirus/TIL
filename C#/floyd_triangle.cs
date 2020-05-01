using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
 // Compiler version 4.0, .NET Framework 4.5


 namespace Triangle
 {
   public class Program
   {
     public static void Main(string[] args)
     {
        Console.WriteLine("This code displays floyd's triangle.");
           int i,j,n;
           int a = 1;
           Console.WriteLine("Enter number of layers:- ");
           n = Convert.ToInt32(Console.ReadLine());
           for (i=1; i<=n; i++)
           {
             for(j=1; j<=i; j++)
             {
               Console.Write(a++ +" ");
             }
             Console.WriteLine();
           
           }
     }
   }
 }
