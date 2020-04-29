using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Reverse
{
    class Program
    {
        static void Main(string[] args)
        {
            string s = Console.ReadLine();
            char [] arr = s.ToCharArray();
            Array.Reverse(arr);
            Console.Write(new String(arr));
        }
    }
}
