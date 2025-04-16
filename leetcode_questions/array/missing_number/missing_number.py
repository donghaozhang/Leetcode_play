from typing import List

class Solution:
    # Approach 1: Sorting (provided solution)
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 1):
            if i != nums[i]:
                return i
        return len(nums)
    
    # Approach 2: Mathematical approach - O(n) time, O(1) space
    def missingNumber_math(self, nums: List[int]) -> int:
        n = len(nums)
        # Sum of integers from 0 to n is n*(n+1)/2
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    # Approach 3: XOR approach - O(n) time, O(1) space
    def missingNumber_xor(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            # XOR the index and the value at that index
            result ^= i ^ nums[i]
        return result

# Test cases
def test_missing_number():
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 0, 1]
    print(f"Input: {nums1}")
    print(f"Output (Sorting): {solution.missingNumber(nums1)}")
    print(f"Output (Math): {solution.missingNumber_math(nums1)}")
    print(f"Output (XOR): {solution.missingNumber_xor(nums1)}")
    print(f"Expected: 2")
    print()
    
    # Test case 2
    nums2 = [0, 1]
    print(f"Input: {nums2}")
    print(f"Output (Sorting): {solution.missingNumber(nums2)}")
    print(f"Output (Math): {solution.missingNumber_math(nums2)}")
    print(f"Output (XOR): {solution.missingNumber_xor(nums2)}")
    print(f"Expected: 2")
    print()
    
    # Test case 3
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"Input: {nums3}")
    print(f"Output (Sorting): {solution.missingNumber(nums3)}")
    print(f"Output (Math): {solution.missingNumber_math(nums3)}")
    print(f"Output (XOR): {solution.missingNumber_xor(nums3)}")
    print(f"Expected: 8")
    print()
    
    # Test case 4 - Single element
    nums4 = [0]
    print(f"Input: {nums4}")
    print(f"Output (Sorting): {solution.missingNumber(nums4)}")
    print(f"Output (Math): {solution.missingNumber_math(nums4)}")
    print(f"Output (XOR): {solution.missingNumber_xor(nums4)}")
    print(f"Expected: 1")

if __name__ == "__main__":
    test_missing_number() 