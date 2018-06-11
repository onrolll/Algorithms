using System;
namespace MergeSort
{
    public static class MergeSort
    {
        public static void Sort(int[] arr, int start, int end)
		{
			if(start<end)
			{
				// Find the middle point
				int middlePoint = (start + end) / 2;

				// Sort both havles
				Sort(arr, start, middlePoint);
				Sort(arr, middlePoint + 1, end);

				// Merge sorted halves
				Merge(arr, start, middlePoint, end);
			}
		}

		private static void Merge(int[] arr, int start, int middlePoint, int end)
		{
			// Find the sizes of the subarrays to be merged;
			int sizeOfLeftSubarray = middlePoint - start + 1;
			int sizeOfRightSubarray = end - middlePoint;
            
			// Initialize empty subarrays of appropriate sizes
			int[] leftSubarray = new int[sizeOfLeftSubarray];
			int[] rightSubarray = new int[sizeOfRightSubarray];

			// Copy corresponding data to subarrays
			for (int i = 0; i < sizeOfLeftSubarray; i++)
				leftSubarray[i] = arr[start + i];
			for (int i = 0; i < sizeOfRightSubarray; i++)
				rightSubarray[i] = arr[middlePoint + 1 + i];
            
			// Initial indexes of leftSubarray & rightSubarray
			int indexOfLeftSubarray = 0;
            int indexOfRightSubarray = 0;

			// Initial index of arr
			int indexOfInitialArray = start;
            
			while (indexOfLeftSubarray < sizeOfLeftSubarray & indexOfRightSubarray < sizeOfRightSubarray)
			{
				if (leftSubarray[indexOfLeftSubarray] < rightSubarray[indexOfRightSubarray])
				{
					arr[indexOfInitialArray] = leftSubarray[indexOfLeftSubarray];
					indexOfLeftSubarray++;
				}
				else
				{
					arr[indexOfInitialArray] = rightSubarray[indexOfRightSubarray];
					indexOfRightSubarray++;
				}
				indexOfInitialArray++;
			}
			// Copy remaining elements from one of the subarrays
			while(indexOfLeftSubarray<sizeOfLeftSubarray)
			{
				arr[indexOfInitialArray] = leftSubarray[indexOfLeftSubarray];
				indexOfLeftSubarray++;
				indexOfInitialArray++;
			}
			while(indexOfRightSubarray < sizeOfRightSubarray)
			{
				arr[indexOfInitialArray] = rightSubarray[indexOfRightSubarray];
				indexOfRightSubarray++;
				indexOfInitialArray++;
			}
		}
	}
}
