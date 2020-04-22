using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Test

{
    class Program
    {
        static void Main(string[] args)
        {
        string name;
        Console.WriteLine("what's your name");
        name = Console.ReadLine();
        Console.WriteLine("hello {0}",  name);
        Console.WriteLine("how old are you?");
        int age =
        Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("You are {0} years old",age);
        Console.WriteLine("So Your name is {0} and you are {1} years old", name, age);
        }
    }
}
