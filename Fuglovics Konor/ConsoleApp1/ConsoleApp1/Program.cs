using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            /*Console.WriteLine("Hello World!");
            int a = 5;
            int b = 6;
            int c = 13;
            int ab = a + b;
            Console.WriteLine(ab);*/

           /* byte overflowing = byte.MaxValue;
            overflowing++;
            Console.WriteLine(overflowing);*/

            string beker = Console.ReadLine();
            int num1 = int.Parse(beker);
            string beker2 = Console.ReadLine();
            int num2 = Convert.ToInt32(beker2);
            int osszeg = num1 + num2;
            Console.WriteLine(osszeg);

            Console.ReadKey();
        }

    }
}
