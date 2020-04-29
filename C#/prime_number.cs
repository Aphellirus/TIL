using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Enter any number to check for it's prime
namespace PrimeNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("#UPVOTE");
            int val = Convert.ToInt32(Console.ReadLine());
            
            bool isPrime=true;
            
            for(int i=2; i<val/2; i++)
            {
                if(val % i == 0)
                {
                    Console.WriteLine(val + " Is Not Prime Number!");
                    isPrime = false;
                    break;
                }
            }
            
            if(isPrime)
                Console.WriteLine(val + " Is Prime Number!");
        }
    }
}
