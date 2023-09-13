using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*Console.WriteLine("Helló világ");
            Console.Write("Ez ");
            Console.Write("mi?");*/
            /*int a = 7;
            int b = 3;
            int ab = a + b;*/
            /*b = b + 3;
            b += 3;
            b -= 2;
            Console.WriteLine(b);
            Console.WriteLine(ab);*/
            /*string str1 = "alma";
            string str2 = "fa";
            string ossz = str1 + str2;
            int a = 12, b = 23, c = 34;
            int eredmeny = a + b + c;
            Console.WriteLine("Az eredmény " + eredmeny + " lett.");
            int a = 1;
            int b = 2;
            //a változóba a "b nagyobb, mint a" szöveg kerül, mivel a feltétel nem igaz
            string nagyobb = a > b ? "a nagyobb, mint b" : "b nagyobb, mint a";

            int j, i = 2;
            j = i++; // postfix
            Console.Write("j = " + j + "; i = " + i);
            int k, l = 2;
            k = ++l; // prefix
            byte tulcsordulas = byte.MaxValue
            tulcsordulas++
            Console.Write("k = " + k + "; l = " + l);*/
            string beker = Console.ReadLine();
            int szam1 = int.Parse(beker);
            string beker2 = Console.ReadLine();
            int szam2 = Convert.ToInt32(beker2);
            int összeg = szam1 + szam2;
            Console.WriteLine(összeg);

            Console.ReadKey();
        }
    }
}
