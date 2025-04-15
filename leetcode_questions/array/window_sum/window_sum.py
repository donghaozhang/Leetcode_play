def window_sum(nums, k):
    """
    Calculate the sum of all consecutive k numbers in the array
    :param nums: List[int], input array
    :param k: int, window size
    :return: List[int], sum of all windows
    """
    if not nums or k <= 0 or k > len(nums):
        return []
        
    n = len(nums)
    result = []
    
    # Calculate the sum of the first window
    window_sum = sum(nums[:k])
    result.append(window_sum)
    
    # Slide the window, subtract the leftmost number and add the rightmost number each time
    for i in range(n - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        result.append(window_sum)
        
    return result

def test_window_sum():
    # Test case 1
    nums1 = [1, 2, 7, 8, 5]
    k1 = 3
    assert window_sum(nums1, k1) == [10, 17, 20], f"Expected [10, 17, 20], but got {window_sum(nums1, k1)}"
    
    # Test case 2: Empty array
    assert window_sum([], 2) == [], "Expected empty array for empty input"
    
    # Test case 3: k greater than array length
    nums3 = [1, 2, 3]
    k3 = 4
    assert window_sum(nums3, k3) == [], "Expected empty array when k > len(nums)"
    
    # Test case 4: k = 1
    nums4 = [1, 2, 3]
    k4 = 1
    assert window_sum(nums4, k4) == [1, 2, 3], "Expected original array when k = 1"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_window_sum() 