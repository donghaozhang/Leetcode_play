from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Fixed version of the 3Sum solution with proper two-pointer approach
        """
        # Sort the array to handle duplicates and use two pointers approach
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Use two pointers for the remaining elements
            left = i + 1  # left should start after i
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
        
        return result


# Test the fixed solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Expected: [[-1, -1, 2], [-1, 0, 1]]
    print(solution.threeSum([0, 1, 1]))               # Expected: []
    print(solution.threeSum([0, 0, 0]))               # Expected: [[0, 0, 0]] 