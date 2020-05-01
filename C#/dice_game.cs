using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
 // Compiler version 4.0, .NET Framework 4.5


 namespace Dice
 {
   public class Program
   {
     
      public static void Main(string[] args)
     {
       
      playagain :
      Console.WriteLine ("\t welcome to 💀the dice game💀\n \t#######\n \t####### \n \t#######\n \t####### \n \t####### \n \t#######\n \n  2 players game only");
       Console.WriteLine("  \n\tenter your name player 1");
       string player1 = Console.ReadLine();
       Console.WriteLine("\n  player1 has chossed: " + player1 + " as his name");
       Console.WriteLine("   \n\tnow its player2 turn");
       string player2 = Console.ReadLine();
       Console.WriteLine("\nplayer2 has chossed: " + player2 + " as his name");
       Console.WriteLine("\nchose the first one to play " + player1 + " :1  or " + player2 + " :2");
       string firstplayer = Console.ReadLine();
       
       Random rnd = new Random();
        int dice = rnd.Next(1, 7);
        int dice2 = rnd.Next(1, 7);
       
        if (firstplayer == "1"){
          
         Console.WriteLine (player1 + "  dice is " + dice);
         Console.WriteLine (player2 + " dice is " + dice2);
          }
          
          else if (firstplayer == "2"){
                                    
            Console.WriteLine (player2 + " dice is " + dice2);
            Console.WriteLine (player1 + " dice is " + dice);
            }
            
           if (dice <= dice2) {
             Console.WriteLine(player2 + " has won");
             }
              
              else if (dice > dice2){
                Console.WriteLine(player1 + " has won");
              }
              if (dice == dice2){
                Console.WriteLine("tied");
              }
             goto playagain;
       
       
           
 
    }
  }    
 }
    
