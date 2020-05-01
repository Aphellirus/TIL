using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
 // Compiler version 4.0, .NET Framework 4.5


 namespace Game
 {
   public class Program
   {
     public static void Main()
     {
       Console.WriteLine("ROCK PAPER SCISSORS\n\n");
       Console.WriteLine("Choose rock(r), paper(p), scissors(s)");
       char choice = char.Parse(Console.ReadLine());
       Console.WriteLine("\n");
       choice = char.ToLower(choice);
       
       var random = new Random();
       int pcChoice = random.Next(1, 4);
       
       if(choice == 'r')
       {
         if(pcChoice == 1)
         {
           Console.WriteLine("You chose: rock");
           Console.WriteLine("NPC chose: rock");
           Console.WriteLine("\nYou tied");
         }
         else if(pcChoice == 2)
         {
           Console.WriteLine("You chose: rock");
           Console.WriteLine("NPC chose: paper");
           Console.WriteLine("\nYou lose");
         }
         else if(pcChoice == 3)
         {
           Console.WriteLine("You chose: rock");
           Console.WriteLine("NPC chose: scissors");
           Console.WriteLine("\nYou win");
         }
       }
       else if(choice == 'p')
       {
         if(pcChoice == 1)
         {
           Console.WriteLine("You chose: paper");
           Console.WriteLine("NPC chose: rock");
           Console.WriteLine("\nYou win");
         }
         else if(pcChoice == 2)
         {
           Console.WriteLine("You chose: paper");
           Console.WriteLine("NPC chose: paper");
           Console.WriteLine("\nYou tied");
         }
         else if(pcChoice == 3)
         {
           Console.WriteLine("You chose: paper");
           Console.WriteLine("NPC chose: scissors");
           Console.WriteLine("\nYou lose");
         }
       }
       else if(choice == 's')
       {
         if(pcChoice == 1)
         {
           Console.WriteLine("You chose: scissors");
           Console.WriteLine("NPC chose: rock");
           Console.WriteLine("\nYou lose");
         }
         else if(pcChoice == 2)
         {
           Console.WriteLine("You chose: scissors");
           Console.WriteLine("NPC chose: paper");
           Console.WriteLine("\nYou win");
         }
         else if(pcChoice == 3)
         {
           Console.WriteLine("You chose: scissors");
           Console.WriteLine("NPC chose: scissors");
           Console.WriteLine("\nYou tied");
         }
       }
       Program.Main();
     }
   }
 }
