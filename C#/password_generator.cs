using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Password
{
  public class Program
  {
    public static void Main(string[] args)
    {
      string Let = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz";
      string Num = "1234567890";
      Console.Write("Length of password:");
      int Len = Convert.ToInt32(Console.ReadLine());
      Console.Write("Your password is: ");
      Random rand = new Random();
      int LN;
      int Pos;
      for(int i = 0; i < Len; i++)
      {
        LN = rand.Next(0, 2);
        if(LN == 0)
        {
          Pos = rand.Next(0, 52);
          Console.Write(Let[Pos]);
        }
        else
        {
          Pos = rand.Next(0, 10);
          Console.Write(Num[Pos]);
        }
      }
      Console.Clear();
    }
  }
}
