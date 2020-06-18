using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reverse {
    class Program {
        static void Main(string[] args) {
            // sample text
            string text = "I am your Father";
            text = String.Join(" ", text.Split(' ').Reverse());
            Console.Write(text);
        }
    }
}
