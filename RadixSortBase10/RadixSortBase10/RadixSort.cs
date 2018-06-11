using System;
namespace RadixSortBase10
{
	// This implementation makes sense for very large # of input values;
    public static class RadixSort
    {
        public static void Sort(int[] arr)
		{
			// Get the max number in the array, in order to know how many digits it contains
			int max = GetMax(arr);
            
			// Do a counting sort of the array, going from least to most significant digit, using the exponent;
			for (int exp = 1; max/exp > 0; exp *= 10)
				CountingSort(arr, exp); 
		}

		private static void CountingSort(int[] arr, int exp)
		{
			int[] output = new int[arr.Length];

			// Initialize count; each position represents # of occurances of digits [0-9], in the position given by exponent;
			// i.e.   exp = 10; arr[i] = 156; -> result = arr[i]/exp = 156 / exp = 15; -> take mod of result in given base (in this case 10)
			// -> result = 5; -> increment count[5];
			int[] count = new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,};

			for (int i = 0; i < arr.Length; i++)
				count[(arr[i] / exp) % 10] += 1;

			// Make count contain the position (index) of a given value in the array, according to the exp;
			// i.e. arr = { 8, 4, 1, 3 }; count = { 0, 1, 0, 1, 1, 0, 0, 0, 1, 0 }; --> count = { 0, 1, 1, 2, 3, 3, 3, 3, 4, 4 };
			// Note that only some positions matter, in this example count[i] where i in { 1, 3, 4, 8 };
			for (int i = 1; i < 10; i++)
				count[i] += count[i - 1];

			// Build the output array;
			// Note that for cycle is in reverse order, because when count[x], where x = (arr[i] / exp) % 10, is decremented
			// it will represent the previous position in the output array;
			for (int i = arr.Length - 1; i >= 0; i--)
			{
				output[count[(arr[i] / exp) % 10] - 1] = arr[i];
				count[(arr[i] / exp) % 10]--;
			}

			for (int i = 0; i < arr.Length; i++)
				arr[i] = output[i];
		}

		private static int GetMax(int[] arr)
		{
			if (arr == null)
				throw new ArgumentNullException();

			int max = arr[0];

			for (int i = 1; i < arr.Length; i++)
				if (arr[i] > max)
					max = arr[i];

			return max;
		}
	}
}
