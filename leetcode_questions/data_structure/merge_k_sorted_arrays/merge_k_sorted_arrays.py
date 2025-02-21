import heapq
from typing import List

def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """
    合并K个有序数组
    :param arrays: List[List[int]]，K个有序数组的列表
    :return: List[int]，合并后的有序数组
    """
    result = []
    # 创建最小堆，存储(值, 数组索引, 元素索引)
    heap = []
    
    # 将每个数组的第一个元素加入堆
    for i, array in enumerate(arrays):
        if array:  # 确保数组非空
            heapq.heappush(heap, (array[0], i, 0))
    
    # 不断从堆中取出最小值
    while heap:
        val, array_index, element_index = heapq.heappop(heap)
        result.append(val)
        
        # 如果当前数组还有下一个元素，将其加入堆
        if element_index + 1 < len(arrays[array_index]):
            next_element = arrays[array_index][element_index + 1]
            heapq.heappush(heap, (next_element, array_index, element_index + 1))
    
    return result

def merge_k_sorted_arrays_divide_conquer(arrays: List[List[int]]) -> List[int]:
    """
    使用分治法合并K个有序数组
    :param arrays: List[List[int]]，K个有序数组的列表
    :return: List[int]，合并后的有序数组
    """
    if not arrays:
        return []
    
    def merge_two_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
        """合并两个有序数组"""
        result = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        result.extend(arr1[i:])
        result.extend(arr2[j:])
        return result
    
    def merge_range(start: int, end: int) -> List[int]:
        """合并指定范围内的数组"""
        if start == end:
            return arrays[start]
        if start + 1 == end:
            return merge_two_arrays(arrays[start], arrays[end])
        
        mid = (start + end) // 2
        left = merge_range(start, mid)
        right = merge_range(mid + 1, end)
        return merge_two_arrays(left, right)
    
    return merge_range(0, len(arrays) - 1)

def test_merge_k_sorted_arrays():
    # 测试用例1：基本情况
    arrays1 = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    expected1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_k_sorted_arrays(arrays1) == expected1
    assert merge_k_sorted_arrays_divide_conquer(arrays1) == expected1
    
    # 测试用例2：包含空数组
    arrays2 = [
        [],
        [1, 3, 5],
        [2, 4, 6]
    ]
    expected2 = [1, 2, 3, 4, 5, 6]
    assert merge_k_sorted_arrays(arrays2) == expected2
    assert merge_k_sorted_arrays_divide_conquer(arrays2) == expected2
    
    # 测试用例3：数组长度不同
    arrays3 = [
        [1],
        [2, 3, 4],
        [5, 6]
    ]
    expected3 = [1, 2, 3, 4, 5, 6]
    assert merge_k_sorted_arrays(arrays3) == expected3
    assert merge_k_sorted_arrays_divide_conquer(arrays3) == expected3
    
    # 测试用例4：全部为空数组
    arrays4 = [[], [], []]
    expected4 = []
    assert merge_k_sorted_arrays(arrays4) == expected4
    assert merge_k_sorted_arrays_divide_conquer(arrays4) == expected4
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_merge_k_sorted_arrays() 