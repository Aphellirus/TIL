using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LoopBreak
{
    class Program
    {
        static void Main(string[] args)
        {
            int x=0;
            while(x<20){
                if(x==5)
                break;
                Console.WriteLine(x);
                x++;
            }
        }
    }
}
