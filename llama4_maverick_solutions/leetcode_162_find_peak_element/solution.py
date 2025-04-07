def findPeakElement(nums):
    """
    Finds the index of a peak element in the given array.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The index of a peak element.

    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        # If the middle element is less than the next one, 
        # then there must be a peak on the right side.
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        # If the middle element is greater than or equal to the next one, 
        # then there must be a peak on the left side (including mid).
        else:
            right = mid
    return left

# Test Cases
if __name__ == "__main__":
    # Example 1
    nums = [1, 2, 3, 1]
    print(findPeakElement(nums))  # Expected Output: 2

    # Example 2
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums))  # Expected Output: 1 or 5

    # Edge Case: Single Element
    nums = [5]
    print(findPeakElement(nums))  # Expected Output: 0

    # Edge Case: Increasing Array
    nums = [1, 2, 3, 4, 5]
    print(findPeakElement(nums))  # Expected Output: 4

    # Edge Case: Decreasing Array
    nums = [5, 4, 3, 2, 1]
    print(findPeakElement(nums))  # Expected Output: 0
