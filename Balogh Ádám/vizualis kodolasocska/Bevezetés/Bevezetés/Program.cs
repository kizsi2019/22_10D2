using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bevezetés
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*Console.WriteLine("Helló világ");
            Console.Write("Ez");
            Console.Write("mi?");*/
            int a = 7;
            int b = 3;
            int ab = a + b;
            //b = b + 3;
            b += 3;
            b -= 2;
            Console.WriteLine(b);
            Console.WriteLine(ab);
            string str1 = "alma";
            string str2 = "fa";
            string ossz = str1 + str2;
            Console.WriteLine(ossz);
            Console.ReadKey();
        }
    }
}
