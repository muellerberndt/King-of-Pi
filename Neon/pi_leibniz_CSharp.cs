using System;
using System.Diagnostics;

namespace pi_leibniz_CSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            double r = 0;
            double e = 0;
            ulong a = 1000000;

            Stopwatch stopWatch = new Stopwatch();
            stopWatch.Start();

            while (true)
            {
                for (double i = 0; i < a; i++)
                {
                    double x = 2 * i + 1;
                    r = Math.Pow(-1, i) / (x);
                    e = e + r;
                }
                Console.WriteLine(e * 4);
                Console.WriteLine(Math.PI);
                break;
            }

            stopWatch.Stop();
            TimeSpan ts = stopWatch.Elapsed;
            string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
                ts.Hours, ts.Minutes, ts.Seconds,
                ts.Milliseconds);
            Console.WriteLine("RunTime " + elapsedTime);
        }
    }
}
