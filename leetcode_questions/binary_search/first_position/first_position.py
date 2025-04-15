def find_first_position(nums, target):
    """
    Find the first position of the target value in a sorted array
    :param nums: List[int], sorted array
    :param target: int, target value
    :return: int, the first position of target value, return -1 if not found
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid
            
    # Check left boundary
    if nums[left] == target:
        return left
    # Check right boundary
    if nums[right] == target:
        return right
        
    return -1

def find_first_position_practice(nums, target):
    """
    Find the first position of the target value in a sorted array
    :param nums: List[int], sorted array
    :param target: int, target value
    :return: int, the first position of target value, return -1 if not found
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        elif nums[mid] < target:
            left = mid 
    
    if nums[left] == target:
        return left
    
    if nums[right] == target:
        return right
    
    return -1


def test_find_first_position():
    """Test find the first position"""
    # Test basic case
    nums1 = [1, 2, 3, 3, 3, 4, 5]
    assert find_first_position(nums1, 3) == 2, "Should find first position"
    assert find_first_position_practice(nums1, 3) == 2, "Should find first position"
    
    # Test target at the beginning
    nums2 = [1, 1, 1, 2, 3]
    assert find_first_position(nums2, 1) == 0, "Should find first position at beginning"
    assert find_first_position_practice(nums2, 1) == 0, "Should find first position at beginning"
    # Test target at the end
    nums3 = [1, 2, 3, 4, 4]
    assert find_first_position(nums3, 4) == 3, "Should find first position at end"
    assert find_first_position_practice(nums3, 4) == 3, "Should find first position at end"

    # Test target not exist
    nums4 = [1, 2, 4, 5]
    assert find_first_position(nums4, 3) == -1, "Should return -1 when target not found"
    assert find_first_position_practice(nums4, 3) == -1, "Should return -1 when target not found"
    # Test empty array
    assert find_first_position([], 1) == -1, "Should handle empty array"
    assert find_first_position_practice([], 1) == -1, "Should handle empty array"
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_first_position()
