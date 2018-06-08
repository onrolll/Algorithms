using System;

namespace InsertionSort
{
    class Program
    {
        static void Main(string[] args)
        {
			var arr = new int[] { 12, 25, 64, 3, 2, 94, 66, 13, 15, 4, 8 };

			InsertionSort.Sort(arr);
          
            Console.WriteLine(string.Join(' ', arr));
		}
    }
}
