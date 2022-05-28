
Stopwatch stopWatch = new Stopwatch();
stopWatch.Start();

while (true)
{
    for (double i = 0; i < a; i++)
    {
        double x = 2*i+1;
        r=Math.Pow(-1,i)/(x);
        e=e+r;
    }
    double af = (Math.PI - (e * 4));
    double rf = (af / (e * 4));
    Console.WriteLine(e*4);
    Console.WriteLine(Math.PI);
    break;
}

stopWatch.Stop();
TimeSpan ts = stopWatch.Elapsed;
string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
    ts.Hours, ts.Minutes, ts.Seconds,
    ts.Milliseconds);
Console.WriteLine("RunTime "+elapsedTime);
