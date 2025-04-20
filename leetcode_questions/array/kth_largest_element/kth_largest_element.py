from typing import List
import heapq
import random

def find_kth_largest_heap(nums: List[int], k: int) -> int:
    """
    Find the kth largest element in the array using a heap.
    
    Args:
        nums: List of integers
        k: The k value for kth largest
        
    Returns:
        The kth largest element
    """
    # One-liner using built-in function
    return heapq.nlargest(k, nums)[-1]

def find_kth_largest_min_heap(nums: List[int], k: int) -> int:
    """
    Find the kth largest element using a min heap of size k.
    
    Args:
        nums: List of integers
        k: The k value for kth largest
        
    Returns:
        The kth largest element
    """
    # Create a min heap of size k
    min_heap = []
    
    for num in nums:
        # Add the current element to the heap
        heapq.heappush(min_heap, num)
        
        # If heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # The root of the heap is the kth largest element
    return min_heap[0]

def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    """
    Find the kth largest element using the QuickSelect algorithm.
    
    Args:
        nums: List of integers
        k: The k value for kth largest
        
    Returns:
        The kth largest element
    """
    # Convert k to index in sorted array (0-indexed)
    k = len(nums) - k
    
    def quickselect(left, right):
        # If the list contains only one element, return that element
        if left == right:
            return nums[left]
        
        # Choose a random pivot to avoid worst-case performance
        pivot_index = random.randint(left, right)
        
        # Move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # Partition the array around the pivot
        store_index = left
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1
        
        # Move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        
        # If we found the kth smallest element, return it
        if store_index == k:
            return nums[store_index]
        # If k is smaller, look in the left subarray
        elif store_index > k:
            return quickselect(left, store_index - 1)
        # If k is larger, look in the right subarray
        else:
            return quickselect(store_index + 1, right)
    
    return quickselect(0, len(nums) - 1)

def find_kth_largest_sorting(nums: List[int], k: int) -> int:
    """
    Find the kth largest element by sorting the array.
    
    Args:
        nums: List of integers
        k: The k value for kth largest
        
    Returns:
        The kth largest element
    """
    # Sort the array in descending order and return the kth element
    return sorted(nums, reverse=True)[k-1]

# Test cases
if __name__ == "__main__":
    # Example 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    
    print("Example 1:")
    print(f"Heap approach: {find_kth_largest_heap(nums1, k1)}")  # Expected: 5
    print(f"Min-heap approach: {find_kth_largest_min_heap(nums1, k1)}")  # Expected: 5
    print(f"QuickSelect approach: {find_kth_largest_quickselect(nums1, k1)}")  # Expected: 5
    print(f"Sorting approach: {find_kth_largest_sorting(nums1, k1)}")  # Expected: 5
    
    # Example 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    
    print("\nExample 2:")
    print(f"Heap approach: {find_kth_largest_heap(nums2, k2)}")  # Expected: 4
    print(f"Min-heap approach: {find_kth_largest_min_heap(nums2, k2)}")  # Expected: 4
    print(f"QuickSelect approach: {find_kth_largest_quickselect(nums2, k2)}")  # Expected: 4
    print(f"Sorting approach: {find_kth_largest_sorting(nums2, k2)}")  # Expected: 4
    
    # Additional test case
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k3 = 3
    
    print("\nAdditional test case:")
    print(f"Heap approach: {find_kth_largest_heap(nums3, k3)}")  # Expected: 8
    print(f"Min-heap approach: {find_kth_largest_min_heap(nums3, k3)}")  # Expected: 8
    print(f"QuickSelect approach: {find_kth_largest_quickselect(nums3, k3)}")  # Expected: 8
    print(f"Sorting approach: {find_kth_largest_sorting(nums3, k3)}")  # Expected: 8 