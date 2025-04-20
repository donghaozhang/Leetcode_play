from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """
    Given an integer array nums, return an array where each element at index i
    is the product of all elements in nums except nums[i].
    
    Args:
        nums: List of integers
        
    Returns:
        List where each element is the product of all elements except self
    """
    # The length of the input array 
    length = len(nums)
    
    # Initialize arrays
    L = [1 for i in range(length)]
    R = [1 for i in range(length)]
    out = [1 for i in range(length)]
    
    # L[i] contains the product of all elements to the left of i
    for i in range(1, length):
        L[i] = L[i-1] * nums[i-1]
    
    # R[i] contains the product of all elements to the right of i
    R[length-1] = 1
    for i in range(length-1, 0, -1):
        R[i-1] = R[i] * nums[i]
    
    # The final answer is the product of L and R arrays
    for i in range(0, length):
        out[i] = L[i] * R[i]
    
    return out

# Test cases
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 2, 3, 4]
    print(product_except_self(nums1))  # Expected output: [24, 12, 8, 6]
    
    # Example 2
    nums2 = [-1, 1, 0, -3, 3]
    print(product_except_self(nums2))  # Expected output: [0, 0, 9, 0, 0] 