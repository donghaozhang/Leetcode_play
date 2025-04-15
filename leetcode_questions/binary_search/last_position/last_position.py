def find_last_position(nums, target):
    """
    Find the last position of the target value in a sorted array
    :param nums: List[int], sorted array
    :param target: int, target value
    :return: int, the last position of target value, return -1 if not found
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid
            
    # Check the right boundary
    if nums[right] == target:
        return right
    # Check the left boundary
    if nums[left] == target:
        return left
        
    return -1

def find_last_position_practice(nums, target):
    """
    Find the last position of the target value in a sorted array
    :param nums: List[int], sorted array
    :param target: int, target value
    :return: int, the last position of target value, return -1 if not found
    """

    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid
            
    # Check the right boundary first because we are looking for the last position
    if nums[right] == target:
        return right
    # Then check the left boundary
    if nums[left] == target:
        return left
        
    return -1
    
def test_find_last_position():
    """Test finding the last position"""
    # Test basic case
    nums1 = [1, 2, 3, 3, 3, 4, 5]
    assert find_last_position(nums1, 3) == 4, "Should find last position"
    assert find_last_position_practice(nums1, 3) == 4, "Should find last position"
    
    # Test target at the beginning
    nums2 = [1, 1, 1, 2, 3]
    assert find_last_position(nums2, 1) == 2, "Should find last position at beginning"
    assert find_last_position_practice(nums2, 1) == 2, "Should find last position at beginning"
    
    # Test target at the end
    nums3 = [1, 2, 3, 4, 4]
    assert find_last_position(nums3, 4) == 4, "Should find last position at end"
    assert find_last_position_practice(nums3, 4) == 4, "Should find last position at end"
    # Test target not exist
    nums4 = [1, 2, 4, 5]
    assert find_last_position(nums4, 3) == -1, "Should return -1 when target not found"
    assert find_last_position_practice(nums4, 3) == -1, "Should return -1 when target not found"
    
    # Test empty array
    assert find_last_position([], 1) == -1, "Should handle empty array"
    assert find_last_position_practice([], 1) == -1, "Should handle empty array"
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_last_position() 