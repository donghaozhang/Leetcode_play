import math
from typing import List

class Solution:
    """
    Finds the k closest elements to x in a sorted array arr.

    Uses binary search to find the optimal starting index of the k-element window.
    """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Finds k closest elements to x in the sorted array arr.

        Args:
            arr: The sorted input array.
            k: The number of closest elements to find.
            x: The target value.

        Returns:
            A list containing the k closest elements, sorted in ascending order.
        """
        n = len(arr)

        # Handle edge case where k is the entire array
        if k == n:
            return arr

        # Binary search for the optimal start index 'left' of the window [left, left + k - 1]
        # The search space for 'left' is [0, n - k]
        low = 0
        high = n - k

        while low < high:
            mid = low + (high - low) // 2
            
            # Compare the element just outside the left end (arr[mid])
            # with the element just outside the right end (arr[mid + k])
            # We want to determine if the window starting at 'mid' is better
            # than the window starting at 'mid + 1'.

            # If x is closer to arr[mid+k] than arr[mid],
            # it means we should discard arr[mid] and shift the window right.
            # The optimal window must start at mid + 1 or later.
            # Condition: x - arr[mid] > arr[mid + k] - x
            # This checks if the distance from x to arr[mid] is greater than
            # the distance from x to arr[mid+k].
            # If distances are equal, x - arr[mid] <= arr[mid+k] - x favors
            # keeping the smaller element arr[mid], hence we keep the window starting at mid.
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                # If x is closer to arr[mid] or equidistant,
                # the optimal window could start at 'mid' or earlier.
                high = mid

        # When the loop ends, 'low' is the starting index of the k closest elements
        return arr[low : low + k]

# --- Test Cases ---

def run_tests():
    sol = Solution()
    test_cases = [
        # Example 1
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        # Example 2
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
        # Edge case: k = 1
        ([1, 1, 1, 10, 10, 10], 1, 9, [10]),
        # Edge case: k = length of array
        ([1, 2, 3], 3, 2, [1, 2, 3]),
        # Edge case: x smaller than all elements
        ([10, 20, 30], 2, 5, [10, 20]),
        # Edge case: x larger than all elements
        ([10, 20, 30], 2, 35, [20, 30]),
        # Tie-breaking case
        ([1, 2, 3, 4, 5], 2, 3, [2, 3]), # |2-3|=1, |3-3|=0, |4-3|=1. Closest are 3, 2. Result [2, 3]
        ([1, 2, 4, 5], 2, 3, [2, 4]), # |2-3|=1, |4-3|=1. Tie, choose smaller elements. Need k=2. Result [2, 4].
        ([1, 3, 5, 7], 2, 4, [3, 5]), # |3-4|=1, |5-4|=1. Tie, choose smaller elements. Need k=2. Result [3, 5].
        # More complex case
        ([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5, [3, 3, 4]),
        # Negative numbers
        ([-5, -3, -1, 0, 2, 4], 3, -2, [-3, -1, 0]),
        ([-2, -1, 0, 1, 2], 3, 0, [-1, 0, 1]),
        # Duplicates around x
        ([1, 1, 2, 2, 2, 3, 3], 3, 2, [2, 2, 2]), # Should pick the 2s
        ([1, 1, 2, 2, 2, 3, 3], 4, 2, [1, 2, 2, 2]), # Should pick one 1 and three 2s
        ([1, 1, 2, 2, 2, 3, 3], 5, 2, [1, 1, 2, 2, 2]), # Should pick two 1s and three 2s
    ]

    for i, (arr, k, x, expected) in enumerate(test_cases):
        result = sol.findClosestElements(arr, k, x)
        print(f"Test Case {i + 1}:")
        print(f"  Input: arr={arr}, k={k}, x={x}")
        print(f"  Expected Output: {expected}")
        print(f"  Actual Output:   {result}")
        assert result == expected, f"Test Case {i + 1} Failed!"
        print("-" * 20)

    print("All test cases passed!")

# Run the tests
run_tests()

