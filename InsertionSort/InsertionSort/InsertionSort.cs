using System;
namespace InsertionSort
{
    public static class InsertionSort
    {
        public static void Sort(int[] arr)
		{
			for (int i = 1; i < arr.Length; i++)
			{
				int key = arr[i];
				int j = i - 1;

				//  Move elements in the range [0; i - 1] to the right, if they are larger than the key
				while (j >= 0 && arr[j] > key)
				{
					arr[j + 1] = arr[j];
					j--;
				}
				// Assign the value of the key to the appropriate position
				arr[j + 1] = key;
			}
		}
    }
}
