using System;

namespace RadixSortBase10
{
    class Program
    {
        static void Main(string[] args)
        {
			int[] arr = new int[] { 43, 22, 12, 100, 31, 66, 87, 2, 7 };

			RadixSort.Sort(arr);

			Console.WriteLine(string.Join(' ', arr));
        }
    }
}
