class ArrayReader:
    """
    Simulates an array reader for an array of unknown size
    """
    def __init__(self, arr):
        self.arr = arr
        
    def get(self, index):
        """
        Returns the value at the given index if valid, otherwise returns 2^31-1
        """
        if 0 <= index < len(self.arr):
            return self.arr[index]
        return 2**31 - 1

def search_big_sorted_array(reader, target):
    """
    Finds the first position of the target value in a sorted array of unknown size
    :param reader: ArrayReader, provides get(index) method to read the array
    :param target: int, target value
    :return: int, the first position of the target value, returns -1 if not found
    """
    if not reader:
        return -1
    
    # 1. Find the right boundary
    right = 1
    while reader.get(right - 1) < target:
        right *= 2
    
    # 2. Perform binary search within the determined range
    left = 0
    while left + 1 < right:
        mid = (left + right) // 2
        if reader.get(mid) >= target:
            right = mid
        else:
            left = mid
    
    # Check left and right boundaries
    if reader.get(left) == target:
        return left
    if reader.get(right) == target:
        return right
    
    return -1

def test_search_big_sorted_array():
    """Test searching in a big sorted array"""
    # Test basic case
    arr1 = [1, 3, 6, 9, 21, 21, 21, 29, 31]
    reader1 = ArrayReader(arr1)
    assert search_big_sorted_array(reader1, 21) == 4, "Should find first position"
    
    # Test target at the beginning
    arr2 = [1, 1, 1, 2, 3]
    reader2 = ArrayReader(arr2)
    assert search_big_sorted_array(reader2, 1) == 0, "Should find first position at beginning"
    
    # Test target at the end
    arr3 = [1, 2, 3, 4, 4]
    reader3 = ArrayReader(arr3)
    assert search_big_sorted_array(reader3, 4) == 3, "Should find first position at end"
    
    # Test target doesn't exist
    arr4 = [1, 2, 4, 5]
    reader4 = ArrayReader(arr4)
    assert search_big_sorted_array(reader4, 3) == -1, "Should return -1 when target not found"
    
    # Test large array
    arr5 = list(range(1000))  # Simulate a large array
    reader5 = ArrayReader(arr5)
    assert search_big_sorted_array(reader5, 500) == 500, "Should handle large array"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_search_big_sorted_array() 