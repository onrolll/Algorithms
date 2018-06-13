using System;
namespace HeapSort
{
    public static class HeapSort
    {
		public static void Sort(int[] arr)
		{
			// Build a MaxHeap out of an array;
			for (int i = arr.Length / 2 - 1; i >= 0; i--)
				Heapify(arr, arr.Length, i);
			
			for (int i = arr.Length - 1; i >= 0; i--)
			{
				// Moving largest element to end of array;
				Swap(arr, 0, i);
				// Heapifying reduced heap;
				Heapify(arr, i, 0);
			}
		}

		private static void Heapify(int[] arr, int sizeOfMaxHeap, int i)
		{
			int largest = arr[i];
			int childIndex = 2 * i + 1;

			if (childIndex < sizeOfMaxHeap)
			{
				if (childIndex + 1 < sizeOfMaxHeap && arr[childIndex + 1] > arr[childIndex])
					childIndex++;
				if (arr[childIndex] > largest)
					largest = arr[childIndex];
			}
			// if largest is still arr[i], this iteration is done;
			if (largest == arr[i]) return;

			Swap(arr, i, childIndex);
			Heapify(arr, sizeOfMaxHeap, childIndex);
		}

		private static void Swap(int[] arr, int i, int j)
		{
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}
}
