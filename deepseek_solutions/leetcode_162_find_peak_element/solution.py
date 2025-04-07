def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

# Test cases
print(findPeakElement([1, 2, 3, 1]))  # Output: 2
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5 or 1
print(findPeakElement([1]))  # Output: 0
print(findPeakElement([1, 2]))  # Output: 1
print(findPeakElement([2, 1]))  # Output: 0
