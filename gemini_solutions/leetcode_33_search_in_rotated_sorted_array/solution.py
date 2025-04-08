from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        Args:
            nums: A list of distinct integers, sorted and possibly rotated.
            target: The integer value to search for.

        Returns:
            The index of the target if found, otherwise -1.
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Case 1: Found the target
            if nums[mid] == target:
                return mid

            # Case 2: Left half is sorted (nums[low] to nums[mid])
            if nums[low] <= nums[mid]:
                # Check if target is within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Search left
                else:
                    low = mid + 1   # Search right
            # Case 3: Right half is sorted (nums[mid] to nums[high])
            else: # nums[low] > nums[mid]
                # Check if target is within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Search right
                else:
                    high = mid - 1  # Search left

        # Target not found
        return -1

# --- Test Cases ---
solver = Solution()

# Example 1
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {solver.search(nums1, target1)}") # Expected: 4
print("-" * 20)

# Example 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(f"Input: nums = {nums2}, target = {target2}")
print(f"Output: {solver.search(nums2, target2)}") # Expected: -1
print("-" * 20)

# Example 3
nums3 = [1]
target3 = 0
print(f"Input: nums = {nums3}, target = {target3}")
print(f"Output: {solver.search(nums3, target3)}") # Expected: -1
print("-" * 20)

# Additional Test Cases
nums4 = [1]
target4 = 1
print(f"Input: nums = {nums4}, target = {target4}")
print(f"Output: {solver.search(nums4, target4)}") # Expected: 0
print("-" * 20)

nums5 = [5, 1, 3]
target5 = 5
print(f"Input: nums = {nums5}, target = {target5}")
print(f"Output: {solver.search(nums5, target5)}") # Expected: 0
print("-" * 20)

nums6 = [5, 1, 3]
target6 = 3
print(f"Input: nums = {nums6}, target = {target6}")
print(f"Output: {solver.search(nums6, target6)}") # Expected: 2
print("-" * 20)

nums7 = [3, 1]
target7 = 1
print(f"Input: nums = {nums7}, target = {target7}")
print(f"Output: {solver.search(nums7, target7)}") # Expected: 1
print("-" * 20)

nums8 = [3, 5, 1]
target8 = 3
print(f"Input: nums = {nums8}, target = {target8}")
print(f"Output: {solver.search(nums8, target8)}") # Expected: 0
print("-" * 20)

