def binary_search(nums, target):
    """
    Find any position of the target value in a sorted array
    :param nums: List[int], sorted array
    :param target: int, target value
    :return: int, position of target value, returns -1 if not found
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def binary_search_practice(nums, target):
    """
    Find any position of the target value in a sorted array
    :param nums: List[int], sorted array
    :param target: int, target value
    :return: int, position of target value, returns -1 if not found
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def test_binary_search():
    """Test binary search"""
    # Test basic case
    nums1 = [1, 2, 3, 3, 4, 5, 10]
    print("binary_search(nums1, 3) = ", binary_search(nums1, 3))
    assert binary_search(nums1, 3) in [2, 3], "Should find target"
    assert binary_search_practice(nums1, 3) in [2, 3], "Should find target"
    
    # Test target at the beginning
    nums2 = [1, 1, 1, 2, 3]
    assert binary_search(nums2, 1) in [0, 1, 2], "Should find target at beginning"
    assert binary_search_practice(nums2, 1) in [0, 1, 2], "Should find target at beginning"

    # Test target at the end
    nums3 = [1, 2, 3, 4, 4]
    assert binary_search(nums3, 4) in [3, 4], "Should find target at end"
    assert binary_search_practice(nums3, 4) in [3, 4], "Should find target at end"
    
    # Test target not found
    nums4 = [1, 2, 4, 5]
    assert binary_search(nums4, 3) == -1, "Should return -1 when target not found"
    assert binary_search_practice(nums4, 3) == -1, "Should return -1 when target not found"
    
    # Test target in the middle
    nums5 = [1, 2, 3, 4, 5]
    assert binary_search(nums5, 3) in [2], "Should find target in the middle"
    assert binary_search_practice(nums5, 3) in [2], "Should find target in the middle"
    # Test target in the middle
    nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(nums6, 5) in [4], "Should find target in the middle"
    print("binary_search(nums6, 5) = ", binary_search(nums6, 5))
    assert binary_search_practice(nums6, 5) in [4], "Should find target in the middle"



    # Test empty array
    assert binary_search([], 1) == -1, "Should handle empty array"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_binary_search() 