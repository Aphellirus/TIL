using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LoopContinue
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int x = 0; x < 20; x++) {
                if (x == 5)
                    continue;

                Console.WriteLine(x);
            }
        }
    }
}
