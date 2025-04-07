from typing import List

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    # Find the index of the closest element to x using binary search
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        # Compare the absolute differences between arr[mid] and x, and arr[mid + k] and x
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    # Return the k closest elements
    return arr[left:left + k]

# Test cases
print(findClosestElements([1, 2, 3, 4, 5], 4, 3))  # Output: [1, 2, 3, 4]
print(findClosestElements([1, 2, 3, 4, 5], 4, -1))  # Output: [1, 2, 3, 4]
print(findClosestElements([1, 5, 10, 15, 20], 3, 8))  # Output: [1, 5, 10]
print(findClosestElements([1, 2, 3, 4, 5], 2, 6))  # Output: [4, 5]
