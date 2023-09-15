using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Adj meg egy számot! ");
            int szam1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Adj meg egy másik számot! ");
            int szam2 = Convert.ToInt32(Console.ReadLine());

            if (szam1 > szam2)
            {
                Console.WriteLine(szam1 + " nagyobb mint " + szam2);
            }

            else if (szam1 < szam2)
            {
                Console.WriteLine(szam2 + " nagyobb mint " + szam1);
            }

            else
            {
                Console.WriteLine("A két szám egyenlő");
            }

            Console.ReadLine();
        }
    }
}
