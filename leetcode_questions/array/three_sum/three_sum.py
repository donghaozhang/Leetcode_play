from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array that give the sum of zero.
        
        Args:
            nums: List of integers
            
        Returns:
            List of triplets (lists of 3 integers) that sum to zero
        """
        # Sort the array to handle duplicates and use two pointers approach
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Two pointers approach for the remaining two elements
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # Sum is too small, move left pointer to increase the sum
                    left += 1
                elif total > 0:
                    # Sum is too large, move right pointer to decrease the sum
                    right -= 1
                else:
                    # Found a triplet with sum = 0
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers to find more triplets
                    left += 1
                    right -= 1
                    
        return result


def test_three_sum():
    """Test the threeSum function with various examples"""
    solution = Solution()
    
    # Test case 1: Regular case with multiple solutions
    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    result1 = solution.threeSum(nums1)
    # Sort the triplets for consistent comparison
    result1.sort()
    expected1.sort()
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2: No solution
    nums2 = [0, 1, 1]
    expected2 = []
    result2 = solution.threeSum(nums2)
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: Single solution with all zeros
    nums3 = [0, 0, 0]
    expected3 = [[0, 0, 0]]
    result3 = solution.threeSum(nums3)
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    # Test case 4: Larger dataset with more solutions
    nums4 = [-2, -1, 0, 1, 2, 3, -3]
    expected4 = [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    result4 = solution.threeSum(nums4)
    # Sort the triplets for consistent comparison
    result4.sort()
    expected4.sort()
    assert result4 == expected4, f"Expected {expected4}, got {result4}"
    
    # Test case 5: Duplicate triplets should be removed
    nums5 = [-1, -1, 0, 1, 1, 0]
    expected5 = [[-1, 0, 1], [0, 0, 0]]
    result5 = solution.threeSum(nums5)
    # Sort the triplets for consistent comparison
    result5.sort()
    expected5.sort()
    assert result5 == expected5, f"Expected {expected5}, got {result5}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_three_sum() 