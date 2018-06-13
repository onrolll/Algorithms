using System;

namespace QuickSort
{
    class Program
    {
        static void Main(string[] args)
        {
			int[] arr = new int[] { 99, 16, 3, 54, 67, 89, 653, 345, 123, 0, 4, 118 };

			QuickSort.Sort(arr);

			Console.WriteLine(string.Join(' ', arr));
		}
    }
}
