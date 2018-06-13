using System;

namespace HeapSort
{
    class Program
    {
        static void Main(string[] args)
        {
			int[] arr = new int[] { 11, 2, 44, 56, 789, 34, 3, 15, 28, 40, 42, 605 };

			HeapSort.Sort(arr);

			Console.WriteLine(string.Join(' ', arr));
		}
    }
}
