using System;

namespace ShellSort
{
    class Program
    {
        static void Main(string[] args)
        {
			int[] arr = new int[] { 13, 45, 5, 7, 2, 1234, 23, -2, 34, 0 };

			ShellSort.Sort(arr);

			Console.WriteLine(string.Join(' ', arr));
		}
    }
}
