"""
Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""

def max_subarray_kadane(nums):
    """
    Find the maximum sum of a contiguous subarray using Kadane's algorithm.
    
    Args:
        nums: List of integers
        
    Returns:
        int: Maximum subarray sum
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
        
    max_so_far = nums[0]
    max_ending_here = nums[0]
    
    for i in range(1, len(nums)):
        # Choose between extending previous subarray or starting new one
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        # Update global maximum
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far


def max_subarray_with_indices(nums):
    """
    Find the maximum sum of a contiguous subarray and return the sum along with the start and end indices.
    
    Args:
        nums: List of integers
        
    Returns:
        tuple: (max_sum, start_index, end_index)
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0, -1, -1
        
    max_so_far = nums[0]
    max_ending_here = nums[0]
    start = 0
    end = 0
    current_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > max_ending_here + nums[i]:
            # Start a new subarray
            max_ending_here = nums[i]
            current_start = i
        else:
            # Extend the existing subarray
            max_ending_here = max_ending_here + nums[i]
            
        if max_ending_here > max_so_far:
            # Update the best subarray found so far
            max_so_far = max_ending_here
            start = current_start
            end = i
            
    return max_so_far, start, end


def max_crossing_subarray(nums, left, mid, right):
    """
    Find the maximum subarray that crosses the midpoint.
    
    Args:
        nums: List of integers
        left: Left boundary index
        mid: Middle index
        right: Right boundary index
        
    Returns:
        int: Maximum sum of a subarray crossing the midpoint
    """
    # Find maximum subarray ending at mid (left part)
    left_sum = float('-inf')
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += nums[i]
        left_sum = max(left_sum, current_sum)
        
    # Find maximum subarray starting at mid+1 (right part)
    right_sum = float('-inf')
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += nums[i]
        right_sum = max(right_sum, current_sum)
        
    # Return sum of best left and right parts
    return left_sum + right_sum


def max_subarray_divide_conquer_helper(nums, left, right):
    """
    Helper function for the divide and conquer approach.
    
    Args:
        nums: List of integers
        left: Left boundary index
        right: Right boundary index
        
    Returns:
        int: Maximum subarray sum in the range [left, right]
    """
    # Base case: single element
    if left == right:
        return nums[left]
        
    mid = (left + right) // 2
    
    # Case 1: Maximum subarray in left half
    left_max = max_subarray_divide_conquer_helper(nums, left, mid)
    
    # Case 2: Maximum subarray in right half
    right_max = max_subarray_divide_conquer_helper(nums, mid + 1, right)
    
    # Case 3: Maximum subarray crossing midpoint
    cross_max = max_crossing_subarray(nums, left, mid, right)
    
    # Return the maximum of the three
    return max(left_max, right_max, cross_max)


def max_subarray_divide_conquer(nums):
    """
    Find the maximum sum of a contiguous subarray using divide and conquer approach.
    
    Args:
        nums: List of integers
        
    Returns:
        int: Maximum subarray sum
        
    Time Complexity: O(n log n)
    Space Complexity: O(log n) for the recursion stack
    """
    if not nums:
        return 0
        
    return max_subarray_divide_conquer_helper(nums, 0, len(nums) - 1)


def test_max_subarray():
    """
    Test function for maximum subarray algorithms.
    """
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),      # Standard case
        ([1], 1),                                   # Single element
        ([5, 4, -1, 7, 8], 23),                     # All positive except one
        ([-1, -2, -3, -4], -1),                     # All negative
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7),         # Mixed positive and negative
        ([0, 0, 0, 0], 0),                          # All zeros
        ([], 0),                                    # Empty array
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        # Test Kadane's algorithm
        result_kadane = max_subarray_kadane(nums)
        assert result_kadane == expected, f"Test case {i+1} failed for Kadane's algorithm: got {result_kadane}, expected {expected}"
        
        # Test divide and conquer approach
        result_dc = max_subarray_divide_conquer(nums)
        assert result_dc == expected, f"Test case {i+1} failed for divide and conquer approach: got {result_dc}, expected {expected}"
        
        # Test max_subarray_with_indices (only check the sum)
        if nums:
            result_indices, _, _ = max_subarray_with_indices(nums)
            assert result_indices == expected, f"Test case {i+1} failed for max_subarray_with_indices: got {result_indices}, expected {expected}"
    
    print("All test cases passed!")
    
    # Example usage of max_subarray_with_indices
    example = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, start, end = max_subarray_with_indices(example)
    print(f"Maximum subarray sum: {max_sum}")
    print(f"Maximum subarray: {example[start:end+1]} (indices {start} to {end})")


if __name__ == "__main__":
    test_max_subarray() 