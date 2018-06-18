using System;
namespace ShellSort
{
    public static class ShellSort
    {
		public static void Sort(int[] arr)
		{
			// Using left/rightIndex for convenience & readability uses more lines of code 
			int rightIndex, leftIndex, initialRight, gap;

			for ( gap = arr.Length / 2; gap > 0; gap /= 2)
			{
				for (rightIndex = gap; rightIndex < arr.Length; rightIndex++)
				{
					leftIndex = rightIndex - gap;

					// initialRight will be placed at the last left position bigger than it;
					initialRight = arr[rightIndex];

					while (leftIndex >= 0 && arr[leftIndex] > initialRight)
					{
						// Shift bigger than initialRight elements to the right by gap positions
						arr[rightIndex] = arr[leftIndex];

						// Set new right/leftIndex;
						rightIndex -= gap;
						leftIndex = rightIndex - gap;
					}
					// Place initialRight at the correct position;
					arr[rightIndex] = initialRight;
				}
			}
		}
	}
}
