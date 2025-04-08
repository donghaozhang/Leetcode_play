from typing import List

class Solution:
    """
    Finds the minimum element in a rotated sorted array with unique elements.
    """
    def findMin(self, nums: List[int]) -> int:
        """
        Uses binary search to find the minimum element in O(log n) time.

        Args:
            nums: A list of integers representing the rotated sorted array.

        Returns:
            The minimum element in the array.
        """
        if not nums:
            # Although constraints state n >= 1, handle empty list defensively.
            return -1 # Or raise an error, depending on requirements

        n = len(nums)
        left, right = 0, n - 1

        # If the array is not rotated (or rotated n times),
        # the first element is the minimum.
        # This check is not strictly necessary for the algorithm's correctness
        # but can be a small optimization.
        # if nums[left] <= nums[right]:
        #     return nums[left]

        # Binary search loop
        while left < right:
            mid = left + (right - left) // 2

            # Compare nums[mid] with nums[right] to decide which half to search
            if nums[mid] > nums[right]:
                # Minimum element is in the right half (mid+1 to right)
                # because nums[mid] is part of the 'larger' segment
                left = mid + 1
            else: # nums[mid] < nums[right] (equality impossible due to unique elements)
                # Minimum element is potentially nums[mid] or in the left half (left to mid)
                # because nums[mid] is part of the 'smaller' segment or is the pivot
                right = mid

        # When the loop ends, left == right, and points to the minimum element
        return nums[left]

# --- Test Cases ---
solver = Solution()

# Example 1
nums1 = [3, 4, 5, 1, 2]
print(f"Input: {nums1}, Output: {solver.findMin(nums1)}") # Expected: 1

# Example 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
print(f"Input: {nums2}, Output: {solver.findMin(nums2)}") # Expected: 0

# Example 3: Not rotated (or rotated n times)
nums3 = [11, 13, 15, 17]
print(f"Input: {nums3}, Output: {solver.findMin(nums3)}") # Expected: 11

# Edge Case: Single element
nums4 = [1]
print(f"Input: {nums4}, Output: {solver.findMin(nums4)}") # Expected: 1

# Edge Case: Two elements, rotated
nums5 = [2, 1]
print(f"Input: {nums5}, Output: {solver.findMin(nums5)}") # Expected: 1

# Edge Case: Two elements, not rotated
nums6 = [1, 2]
print(f"Input: {nums6}, Output: {solver.findMin(nums6)}") # Expected: 1

# Larger case
nums7 = [7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6]
print(f"Input: {nums7}, Output: {solver.findMin(nums7)}") # Expected: 1
