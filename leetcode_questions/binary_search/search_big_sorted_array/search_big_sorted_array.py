class ArrayReader:
    """
    模拟未知大小的数组读取器
    """
    def __init__(self, arr):
        self.arr = arr
        
    def get(self, index):
        """
        如果索引有效则返回数组中的值，否则返回2^31-1
        """
        if 0 <= index < len(self.arr):
            return self.arr[index]
        return 2**31 - 1

def search_big_sorted_array(reader, target):
    """
    在未知大小的有序数组中查找目标值的第一个位置
    :param reader: ArrayReader，提供get(index)方法读取数组
    :param target: int，目标值
    :return: int，目标值的第一个位置，如果不存在返回-1
    """
    if not reader:
        return -1
    
    # 1. 找到右边界
    right = 1
    while reader.get(right - 1) < target:
        right *= 2
    
    # 2. 在确定范围内二分查找
    left = 0
    while left + 1 < right:
        mid = (left + right) // 2
        if reader.get(mid) >= target:
            right = mid
        else:
            left = mid
    
    # 检查左右边界
    if reader.get(left) == target:
        return left
    if reader.get(right) == target:
        return right
    
    return -1

def test_search_big_sorted_array():
    """测试大数组搜索"""
    # 测试基本情况
    arr1 = [1, 3, 6, 9, 21, 21, 21, 29, 31]
    reader1 = ArrayReader(arr1)
    assert search_big_sorted_array(reader1, 21) == 4, "Should find first position"
    
    # 测试目标值在开头
    arr2 = [1, 1, 1, 2, 3]
    reader2 = ArrayReader(arr2)
    assert search_big_sorted_array(reader2, 1) == 0, "Should find first position at beginning"
    
    # 测试目标值在结尾
    arr3 = [1, 2, 3, 4, 4]
    reader3 = ArrayReader(arr3)
    assert search_big_sorted_array(reader3, 4) == 3, "Should find first position at end"
    
    # 测试目标值不存在
    arr4 = [1, 2, 4, 5]
    reader4 = ArrayReader(arr4)
    assert search_big_sorted_array(reader4, 3) == -1, "Should return -1 when target not found"
    
    # 测试大数组
    arr5 = list(range(1000))  # 模拟大数组
    reader5 = ArrayReader(arr5)
    assert search_big_sorted_array(reader5, 500) == 500, "Should handle large array"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_search_big_sorted_array() 