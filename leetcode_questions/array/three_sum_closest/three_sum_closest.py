from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Find three integers in nums such that the sum is closest to target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            The sum of the three integers closest to the target
        """
        # Sort the array to use two pointers approach
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            # Skip duplicate values for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Two pointers approach for the remaining two elements
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if current sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # If we found exact match, return immediately
                if current_sum == target:
                    return target
                
                # Adjust pointers based on comparison with target
                if current_sum < target:
                    left += 1
                else:  # current_sum > target
                    right -= 1
                    
        return closest_sum


def test_three_sum_closest():
    """Test the threeSumClosest function with various examples"""
    solution = Solution()
    
    # Test case 1: Regular case from example
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    expected1 = 2  # -1 + 2 + 1 = 2
    result1 = solution.threeSumClosest(nums1, target1)
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2: All zeros
    nums2 = [0, 0, 0]
    target2 = 1
    expected2 = 0  # 0 + 0 + 0 = 0
    result2 = solution.threeSumClosest(nums2, target2)
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: Exact match
    nums3 = [1, 1, 1]
    target3 = 3
    expected3 = 3  # 1 + 1 + 1 = 3
    result3 = solution.threeSumClosest(nums3, target3)
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    # Test case 4: Larger dataset
    nums4 = [-5, -3, -1, 0, 2, 4, 6]
    target4 = 7
    expected4 = 8  # 2 + 0 + 6 = 8, closest to 7
    result4 = solution.threeSumClosest(nums4, target4)
    assert result4 == expected4, f"Expected {expected4}, got {result4}"
    
    # Test case 5: Negative target
    nums5 = [1, 2, 5, 10, 11]
    target5 = -5
    expected5 = 8  # 1 + 2 + 5 = 8, closest to -5
    result5 = solution.threeSumClosest(nums5, target5)
    assert result5 == expected5, f"Expected {expected5}, got {result5}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_three_sum_closest() 