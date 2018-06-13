using System;
namespace QuickSort
{
    public static class QuickSort
    {
		public static void Sort(int[] arr)
		{
			Sort(arr, 0, arr.Length - 1);
		}

		private static void Sort(int[] arr,int left,int right)
		{
			if (left < right)
			{
				int pivotIndex = Partition(arr, left, right);
                
				// Recursively sort the elements before and after the pivot;e
				Sort(arr, left, pivotIndex - 1);
				Sort(arr, pivotIndex + 1, right);
			}
		}

		private static int Partition(int[] arr, int left, int right)
		{
			int pivot = arr[right];

			// Initializing the index of where the pivot should end up at;
			int lastNumberSmallerThanPivotIndex = left - 1;

			for (int i = left; i < right; i++)
			{
				if(arr[i] <= pivot)
				{
					lastNumberSmallerThanPivotIndex++;

					// Swap the current element with the element after the last smaller than pivot element;
					// in other words: swap curent element with the first bigger than pivot element;
					int temp = arr[i];
					arr[i] = arr[lastNumberSmallerThanPivotIndex];
					arr[lastNumberSmallerThanPivotIndex] = temp;
				}
			}

			// Situate the pivot at the correct position, by swapping it with the element at that position
			int swap = arr[lastNumberSmallerThanPivotIndex + 1];
			arr[right] = swap;
			arr[lastNumberSmallerThanPivotIndex + 1] = pivot;

			return lastNumberSmallerThanPivotIndex + 1;
		}
	}
}
