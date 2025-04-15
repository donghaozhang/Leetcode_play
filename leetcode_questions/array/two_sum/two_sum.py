from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers such that they add up to target
    :param nums: List[int], input array
    :param target: int, target sum
    :return: List[int], indices of the two numbers
    """
    hash_map = {}  # Create an empty hash map
    for index, num in enumerate(nums):
        needed = target - num
        if needed in hash_map:
            return [hash_map[needed], index]  # Return the indices of the numbers forming the required sum
        hash_map[num] = index  # Store the index of the current number

def test_two_sum():
    """Test cases for the two_sum function"""
    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    assert sorted(result1) == [0, 1], f"Expected [0, 1], but got {result1}"
    
    # Test case 2: Numbers in different order
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    assert sorted(result2) == [1, 2], f"Expected [1, 2], but got {result2}"
    
    # Test case 3: Duplicate numbers
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    assert sorted(result3) == [0, 1], f"Expected [0, 1], but got {result3}"
    
    # Test case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    result4 = two_sum(nums4, target4)
    assert sorted(result4) == [2, 4], f"Expected [2, 4], but got {result4}"
    
    # Test case 5: Larger array
    nums5 = [1, 5, 8, 3, 9, 2, 7, 4]
    target5 = 10
    result5 = two_sum(nums5, target5)
    assert nums5[result5[0]] + nums5[result5[1]] == target5, f"Sum of elements at indices {result5} does not equal {target5}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum() 