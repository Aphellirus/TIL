using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
 // Compiler version 4.0, .NET Framework 4.5


 namespace Manipulator
 {
   public class Program
   {
     public static void Main(string[] args)
     {
       Console.WriteLine("TEXT PROGRAM\n\n");
       Console.WriteLine("What would you like to do?\n");
       Console.WriteLine("1. Reverse text");
       Console.WriteLine("2. Sort text");
       Console.WriteLine("3. Multiply text");
       Console.WriteLine("4. Generate random text");
       int choice = Int32.Parse(Console.ReadLine());
       
       if(choice == 1)
       {
         Console.WriteLine("\nInput the text to be reversed:");
         string text = Console.ReadLine();
         char[] textArray = text.ToCharArray();
         Array.Reverse(textArray);
         Console.WriteLine();
         foreach(char c in textArray)
         {
           Console.Write(c);
         }
       }
       else if(choice == 2)
       {
         Console.WriteLine("\nWould you like to sort your text forwards(f) or backwards(b)?");
         string direction = Console.ReadLine();
         if(direction == "f" || direction == "forwards")
         {
           Console.WriteLine("\nInput the text to be sorted:");
           string text = Console.ReadLine();
           char[] textArray = text.ToCharArray();
           Array.Sort(textArray);
           Console.WriteLine();
           foreach(char c in textArray)
           {
             Console.Write(c);
           }
         }
         else if(direction == "b" || direction == "backwards")
         {
           Console.WriteLine("\nInput the text to be sorted:");
           string text = Console.ReadLine();
           char[] textArray = text.ToCharArray();
           Array.Sort(textArray);
           Array.Reverse(textArray);
           Console.WriteLine();
           foreach(char c in textArray)
           {
             Console.Write(c);
           }
         }
       }
       else if(choice == 3)
       {
         Console.WriteLine("\nInput the text to be multiplied:");
         string text = Console.ReadLine();
         char[] textArray = text.ToCharArray();
         Console.WriteLine("\nHow many times would you like the letters multiplied?");
         int times = Int32.Parse(Console.ReadLine());
         Console.WriteLine();
         for(int i = 0; i < textArray.Length; i++)
         {
           for(int j = 1; j < times + 1; j++)
           {
             Console.Write(textArray[i]);
           }
         }
       }
       else if(choice == 4)
       {
         Console.WriteLine("\nHow many strings should be generated?");
         int words = Int32.Parse(Console.ReadLine());
         Console.WriteLine("\nWhat is the max length of a string?");
         int max = Int32.Parse(Console.ReadLine());
         for(int i = 0; i < words; i++)
         {
           var random = new Random();
           int rand = random.Next(1, max);
           for(int j = 0; j < rand; j++)
           {
             var character = new Random();
             int charac = character.Next(65, 90);
             Console.Write((char)charac);
           }
           Console.Write(" ");
         }
       }
     }
   }
 }
