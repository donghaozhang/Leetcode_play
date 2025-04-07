def search(nums: list[int], target: int) -> int:
    """
    Searches for a target element in a possibly rotated sorted array.

    Args:
    - nums: A list of integers sorted in ascending order but possibly rotated.
    - target: The target element to be searched.

    Returns:
    - The index of the target element if found; otherwise, -1.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If the target is found, return its index
        if nums[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            # If the target is within the range of the left half, continue search there
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # If the target is within the range of the right half, continue search there
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    # If the target is not found, return -1
    return -1

# Test Cases
if __name__ == "__main__":
    test_cases = [
        {"nums": [4,5,6,7,0,1,2], "target": 0, "expected": 4},
        {"nums": [4,5,6,7,0,1,2], "target": 3, "expected": -1},
        {"nums": [1], "target": 0, "expected": -1},
        {"nums": [1], "target": 1, "expected": 0},
        {"nums": [2, 1], "target": 2, "expected": 0},
        {"nums": [3, 1], "target": 1, "expected": 1},
    ]
    
    for test_case in test_cases:
        result = search(test_case["nums"], test_case["target"])
        assert result == test_case["expected"], f"Expected {test_case['expected']} but got {result}"
        print(f"Test case passed: nums = {test_case['nums']}, target = {test_case['target']}, result = {result}")
