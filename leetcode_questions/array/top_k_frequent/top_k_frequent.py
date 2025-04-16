from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        # Use a min heap to keep track of the k most frequent elements
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract the numbers from the heap
        result = [item[1] for item in heap]
        
        return result
    
    # Alternative implementation using Counter
    def topKFrequent_counter(self, nums: List[int], k: int) -> List[int]:
        # Count frequency using Counter
        count = Counter(nums)
        
        # Use a min heap to keep track of the k most frequent elements
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract the numbers from the heap
        return [item[1] for item in heap]
    
    # Bucket sort approach (O(n) time complexity)
    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Create buckets where bucket[i] contains all numbers with frequency i
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        # Flatten buckets from highest frequency to lowest
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])
            if len(result) >= k:
                return result[:k]
        
        return result  # This should never be reached if k is valid

# Test cases
def test_top_k_frequent():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Test Case 1 Input: nums = {nums1}, k = {k1}")
    print(f"Output (Heap solution): {solution.topKFrequent(nums1, k1)}")
    print(f"Output (Counter solution): {solution.topKFrequent_counter(nums1, k1)}")
    print(f"Output (Bucket solution): {solution.topKFrequent_bucket(nums1, k1)}")
    print(f"Expected: [1, 2] (in any order)")
    print()
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print(f"Test Case 2 Input: nums = {nums2}, k = {k2}")
    print(f"Output (Heap solution): {solution.topKFrequent(nums2, k2)}")
    print(f"Output (Counter solution): {solution.topKFrequent_counter(nums2, k2)}")
    print(f"Output (Bucket solution): {solution.topKFrequent_bucket(nums2, k2)}")
    print(f"Expected: [1]")
    print()
    
    # Test case 3
    nums3 = [1, 2, 3, 1, 2, 1]
    k3 = 2
    print(f"Test Case 3 Input: nums = {nums3}, k = {k3}")
    print(f"Output (Heap solution): {solution.topKFrequent(nums3, k3)}")
    print(f"Output (Counter solution): {solution.topKFrequent_counter(nums3, k3)}")
    print(f"Output (Bucket solution): {solution.topKFrequent_bucket(nums3, k3)}")
    print(f"Expected: [1, 2] (in any order)")
    print()
    
    # Test case 4
    nums4 = [4, 1, -1, 2, -1, 2, 3]
    k4 = 2
    print(f"Test Case 4 Input: nums = {nums4}, k = {k4}")
    print(f"Output (Heap solution): {solution.topKFrequent(nums4, k4)}")
    print(f"Output (Counter solution): {solution.topKFrequent_counter(nums4, k4)}")
    print(f"Output (Bucket solution): {solution.topKFrequent_bucket(nums4, k4)}")
    print(f"Expected: [-1, 2] (in any order)")

if __name__ == "__main__":
    test_top_k_frequent() 