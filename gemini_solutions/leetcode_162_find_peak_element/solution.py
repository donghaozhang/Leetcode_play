import math
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Finds a peak element in the array using binary search.

        A peak element is an element that is strictly greater than its neighbors.
        Assumes nums[-1] = nums[n] = -infinity.

        Args:
            nums: A list of integers.

        Returns:
            The index of any peak element.
        """
        n = len(nums)

        # Handle edge case: single element array
        if n == 1:
            return 0

        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2

            # Compare mid element with its right neighbor
            if nums[mid] < nums[mid + 1]:
                # We are on an ascending slope, peak must be to the right (mid+1 or further)
                left = mid + 1
            else:
                # We are on a descending slope (or at a peak),
                # peak must be at mid or to the left.
                # Keep mid in the search space as it could be the peak.
                right = mid

        # When the loop terminates, left == right, pointing to a peak element.
        # Why is nums[left] a peak?
        # The loop invariant ensures a peak exists in [left, right].
        # When left == right, the range has one element.
        # Consider the final state: left = right = p.
        # If we arrived here via right = mid, it means nums[mid] > nums[mid+1] (i.e., nums[p] > nums[p+1]).
        # If we arrived here via left = mid + 1, it means the previous mid was p-1, and nums[p-1] < nums[p].
        # Combining these (or handling boundary conditions using implicit -infinity), nums[p] must be a peak.
        return left

# Helper function to run test cases
def run_tests():
    sol = Solution()
    test_cases = [
        ([1, 2, 3, 1], [2]), # Peak is 3 at index 2
        ([1, 2, 1, 3, 5, 6, 4], [1, 5]), # Peaks are 2 (idx 1) and 6 (idx 5) - either is fine
        ([1], [0]), # Single element is a peak
        ([3, 2, 1], [0]), # Peak at the beginning
        ([1, 2, 3], [2]), # Peak at the end
        ([2, 1], [0]), # Two elements, descending
        ([1, 2], [1]), # Two elements, ascending
        ([1, 1, 1, 1], [0, 1, 2, 3]), # Any index could be argued if strictness wasn't required, but here it finds one based on slope logic
        ([6, 5, 4, 3, 2, 3, 2], [0, 5]), # Multiple peaks
    ]

    for i, (nums, expected_indices) in enumerate(test_cases):
        result = sol.findPeakElement(nums.copy()) # Use copy to avoid modifying original test case list if needed
        print(f"Test Case {i+1}:")
        print(f"  Input: nums = {nums}")
        print(f"  Expected Peak Index (one of): {expected_indices}")
        print(f"  Actual Peak Index: {result}")
        if result in expected_indices:
            # Verify if the returned index is indeed a peak
            is_peak = True
            n = len(nums)
            left_val = nums[result - 1] if result > 0 else -math.inf
            right_val = nums[result + 1] if result < n - 1 else -math.inf
            if not (nums[result] > left_val and nums[result] > right_val):
                 is_peak = False

            if is_peak:
                print(f"  Result: PASSED (Found valid peak at index {result})")
            else:
                 print(f"  Result: FAILED (Index {result} value {nums[result]} is not a peak)")

        else:
            # Check if the returned index is actually a peak, even if not listed in expected_indices
            # (only happens if multiple peaks exist and the algorithm finds a different one)
            is_peak = True
            n = len(nums)
            left_val = nums[result - 1] if result > 0 else -math.inf
            right_val = nums[result + 1] if result < n - 1 else -math.inf
            if not (nums[result] > left_val and nums[result] > right_val):
                 is_peak = False

            if is_peak:
                 print(f"  Result: PASSED (Found valid peak at index {result}, which is one of the possible peaks)")
            else:
                 print(f"  Result: FAILED (Returned index {result} is not one of the expected indices {expected_indices} AND is not a peak)")
        print("-" * 20)

# Run the tests
run_tests()
