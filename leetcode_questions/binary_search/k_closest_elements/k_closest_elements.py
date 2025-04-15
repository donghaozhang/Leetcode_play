def find_k_closest_elements(arr, k, target):
    """
    Find k closest elements to the target value in a sorted array
    :param arr: List[int], sorted array
    :param k: int, number of elements to return
    :param target: int, target value
    :return: List[int], k closest elements to the target value
    """
    if not arr or k <= 0:
        return []
        
    # 1. Find the position closest to target
    left, right = 0, len(arr) - k
    
    while left + 1 < right:
        mid = (left + right) // 2
        if target - arr[mid] > arr[mid + k] - target:
            left = mid
        else:
            right = mid
            
    # 2. Compare two possible starting positions, choose the better one
    if right > 0 and target - arr[left] <= arr[left + k] - target:
        start = left
    else:
        start = right
        
    # 3. Return k elements starting from start
    return arr[start:start + k]

def find_k_closest_elements_two_pointers(arr, k, target):
    """
    Use the two-pointer method to find k closest elements to the target value
    :param arr: List[int], sorted array
    :param k: int, number of elements to return
    :param target: int, target value
    :return: List[int], k closest elements to the target value
    """
    if not arr or k <= 0:
        return []
        
    left = 0
    right = len(arr) - 1
    
    # 1. Remove len(arr) - k elements that are farther away
    while right - left >= k:
        if target - arr[left] <= arr[right] - target:
            right -= 1
        else:
            left += 1
            
    # 2. Return the remaining k elements
    return arr[left:right + 1]

def test_find_k_closest_elements():
    """Test finding closest elements"""
    # Test basic case
    arr1 = [1, 2, 3, 4, 5]
    assert find_k_closest_elements(arr1, 4, 3) == [1, 2, 3, 4], "Should find closest elements"
    assert find_k_closest_elements_two_pointers(arr1, 4, 3) == [1, 2, 3, 4], "Two pointers should find closest elements"
    
    # Test target value outside the array
    arr2 = [1, 2, 3, 4, 5]
    assert find_k_closest_elements(arr2, 4, -1) == [1, 2, 3, 4], "Should handle target outside array"
    assert find_k_closest_elements_two_pointers(arr2, 4, -1) == [1, 2, 3, 4], "Two pointers should handle target outside array"
    
    # Test k equal to array length
    arr3 = [1, 2, 3, 4, 5]
    assert find_k_closest_elements(arr3, 5, 3) == [1, 2, 3, 4, 5], "Should handle k equal to array length"
    assert find_k_closest_elements_two_pointers(arr3, 5, 3) == [1, 2, 3, 4, 5], "Two pointers should handle k equal to array length"
    
    # Test empty array
    assert find_k_closest_elements([], 2, 3) == [], "Should handle empty array"
    assert find_k_closest_elements_two_pointers([], 2, 3) == [], "Two pointers should handle empty array"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_k_closest_elements() 