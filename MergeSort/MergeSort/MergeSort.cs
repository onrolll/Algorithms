using System;
namespace MergeSort
{
    public static class MergeSort
    {
        public static void Sort(int[] arr, int l, int r)
		{
			if(l<r)
			{
				// Find the middle point
				int m = (l + r) / 2;

				// Sort both havles
				Sort(arr, l, m);
				Sort(arr, m + 1, r);

				// Merge sorted halves
				Merge(arr, l, m, r);
			}
		}

		private static void Merge(int[] arr, int l, int m, int r)
		{
			// Find the sizes of the subarrays to be merged;
			int sL = m - l + 1;
			int sR = r - m;
            
            // Initialize empty subarrays of appropriate sizes
			int[] L = new int[sL];
			int[] R = new int[sR];

            // Copy corresponding data to subarrays
            for (int i = 0; i < sL; i++)
				L[i] = arr[l + i];
			for (int i = 0; i < sR; i++)
				R[i] = arr[m + 1 + i];

			// Initial indexes of L & R
			int j = 0;
			int n = 0;

			// Initial index of arr
			int k = l;
            
            while (j < sL & n < sR)
			{
                if (L[j] < R[n])
				{
					arr[k] = L[j];
					j++;
				}
				else
				{
					arr[k] = R[n];
					n++;
				}
				k++;
			}

            // Copy remaining elements from one of the subarrays
			while(j<sL)
			{
				arr[k] = L[j];
				j++;
				k++;
			}
			while(n < sR)
			{
				arr[k] = R[n];
				n++;
				k++;
			}
		}
	}
}
