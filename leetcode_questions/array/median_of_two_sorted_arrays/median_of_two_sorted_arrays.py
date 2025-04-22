from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays in O(log(m+n)) time.
        
        Args:
            nums1: First sorted array
            nums2: Second sorted array
            
        Returns:
            Median of the combined arrays
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2
        
        # Binary search on the smaller array
        left, right = 0, m
        
        while left <= right:
            # Partition the smaller array
            i = (left + right) // 2
            # Calculate corresponding partition in larger array
            j = half - i
            
            # Get the four elements around the partition
            nums1_left = float('-inf') if i == 0 else nums1[i-1]
            nums1_right = float('inf') if i == m else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j-1]
            nums2_right = float('inf') if j == n else nums2[j]
            
            # Check if we found the correct partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Calculate median based on total length
                if total % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
        
        # This line should never be reached for valid inputs
        return 0.0

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [1, 3]
    nums2 = [2]
    print(solution.findMedianSortedArrays(nums1, nums2))  # 2.0
    
    # Example 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solution.findMedianSortedArrays(nums1, nums2))  # 2.5
    
    # Test case: One empty array
    nums1 = []
    nums2 = [1]
    print(solution.findMedianSortedArrays(nums1, nums2))  # 1.0
    
    # Test case: Both arrays have same elements
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    print(solution.findMedianSortedArrays(nums1, nums2))  # 2.0
    
    # Test case: All elements in one array are smaller
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(solution.findMedianSortedArrays(nums1, nums2))  # 3.5 