def find_k_closest_elements(arr, k, target):
    """
    在排序数组中找到最接近目标值的k个数
    :param arr: List[int]，有序数组
    :param k: int，需要返回的元素个数
    :param target: int，目标值
    :return: List[int]，最接近目标值的k个数
    """
    if not arr or k <= 0:
        return []
        
    # 1. 找到最接近target的位置
    left, right = 0, len(arr) - k
    
    while left + 1 < right:
        mid = (left + right) // 2
        if target - arr[mid] > arr[mid + k] - target:
            left = mid
        else:
            right = mid
            
    # 2. 比较两个可能的起始位置，选择更优的一个
    if right > 0 and target - arr[left] <= arr[left + k] - target:
        start = left
    else:
        start = right
        
    # 3. 返回从start开始的k个数
    return arr[start:start + k]

def find_k_closest_elements_two_pointers(arr, k, target):
    """
    使用双指针方法找到最接近目标值的k个数
    :param arr: List[int]，有序数组
    :param k: int，需要返回的元素个数
    :param target: int，目标值
    :return: List[int]，最接近目标值的k个数
    """
    if not arr or k <= 0:
        return []
        
    left = 0
    right = len(arr) - 1
    
    # 1. 去掉 len(arr) - k 个较远的数
    while right - left >= k:
        if target - arr[left] <= arr[right] - target:
            right -= 1
        else:
            left += 1
            
    # 2. 返回剩下的k个数
    return arr[left:right + 1]

def test_find_k_closest_elements():
    """测试查找最接近元素"""
    # 测试基本情况
    arr1 = [1, 2, 3, 4, 5]
    assert find_k_closest_elements(arr1, 4, 3) == [1, 2, 3, 4], "Should find closest elements"
    assert find_k_closest_elements_two_pointers(arr1, 4, 3) == [1, 2, 3, 4], "Two pointers should find closest elements"
    
    # 测试目标值在数组外
    arr2 = [1, 2, 3, 4, 5]
    assert find_k_closest_elements(arr2, 4, -1) == [1, 2, 3, 4], "Should handle target outside array"
    assert find_k_closest_elements_two_pointers(arr2, 4, -1) == [1, 2, 3, 4], "Two pointers should handle target outside array"
    
    # 测试k等于数组长度
    arr3 = [1, 2, 3, 4, 5]
    assert find_k_closest_elements(arr3, 5, 3) == [1, 2, 3, 4, 5], "Should handle k equal to array length"
    assert find_k_closest_elements_two_pointers(arr3, 5, 3) == [1, 2, 3, 4, 5], "Two pointers should handle k equal to array length"
    
    # 测试空数组
    assert find_k_closest_elements([], 2, 3) == [], "Should handle empty array"
    assert find_k_closest_elements_two_pointers([], 2, 3) == [], "Two pointers should handle empty array"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_k_closest_elements() 