using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
 // Compiler version 4.0, .NET Framework 4.5


 namespace Converter
 {
   public class Program
   {
     public static void Main(string[] args)
     {
       
       Console.WriteLine("A simple conversion calculator for converting Celsius degree to Kelvin and Fehrenheit");
            Console.WriteLine("What degree whould you like to convert to\nPlease select an option below:");
            Console.WriteLine("1. Kelvin\n2. Fahrenheit");
            int option = Convert.ToInt16(Console.ReadLine());

            if (option == 1)
            {
                Console.WriteLine("You have choosen " + option);
                Console.Write("Please input the  degree value:");
                Double value = Convert.ToDouble(Console.ReadLine());
                Double k = (value + 272.15);
                Console.WriteLine("Your answer is " + k + " degree K");
                Console.ReadLine();
            }
            else
            if (option == 2)
            {
                Console.WriteLine("You have choosen " + option);
                Console.Write("Please input the  degree value: ");
                Double value = Convert.ToDouble(Console.ReadLine());
                Double f = (value * (9 / 5) + 32);
                Console.WriteLine("Your answer is " + f + " degree F");
                Console.ReadLine();
            }
            else
            {
                Console.WriteLine("Invalid selection");
                Console.ReadLine();
            }
     }
   }
 }
