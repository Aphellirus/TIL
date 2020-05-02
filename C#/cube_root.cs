using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Math
{
    class Program
    {
        static void Main(string[] args)
        {
            double nm = double.Parse(Console.ReadLine());
            Console.WriteLine($"root: {FindCubeRoot(nm)}");
        }
        
        static double FindCubeRoot(double num)
        {
            const double precision = 0.0001;
            double root = 2;
            double target = root;
            double absdif = 1;

            Console.WriteLine("Calculating...");

            while (absdif > precision)
            {
                if (target > num) {
                    root -= 0.00009;
                    target = root;
                }
                else if (target < num) {
                    root += 1;
                    target = root;
                }  

                for (var i=1; i<3; i++)
                    target *= root;
                
                absdif = (target - num) > 0 ? (target - num) : -(target - num);              
            }

            return root;
        }
    }
}
