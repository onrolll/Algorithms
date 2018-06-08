using System;

namespace MergeSort
{
    class Program
    {
        static void Main(string[] args)
        {
			var arr = new int[] { 44, 2, 5, 16, 17, 33, 4, 81, 797 };

			MergeSort.Sort(arr, 0, arr.Length - 1);

            Console.WriteLine(string.Join(' ', arr));
		}
    }
}
