# Kth Largest Element in an Array

## Problem

Given an integer array `nums` and an integer `k`, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

## Examples

**Example 1:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Approaches

There are several ways to solve this problem with different time and space complexities:

### Approach 1: Built-in Heap Function

Python's `heapq` module provides a convenient `nlargest` function that can find the k largest elements in a list.

```python
def find_kth_largest_heap(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
```

- **Time Complexity**: O(n log k) - where n is the length of the array.
- **Space Complexity**: O(k) - for storing the k largest elements.

### Approach 2: Min Heap of Size K

We can maintain a min heap of size k, which will hold the k largest elements seen so far:

1. Initialize an empty min heap.
2. Iterate through the array:
   - Add each element to the heap
   - If the heap size exceeds k, remove the smallest element
3. After processing all elements, the root of the heap will be the kth largest element.

```python
def find_kth_largest_min_heap(nums: List[int], k: int) -> int:
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return min_heap[0]
```

- **Time Complexity**: O(n log k) - we perform n heap operations, each taking O(log k) time.
- **Space Complexity**: O(k) - for storing the k largest elements.

### Approach 3: QuickSelect Algorithm

QuickSelect is an optimal approach for this problem that avoids sorting the entire array. It's based on the QuickSort algorithm but only processes one partition:

1. Choose a pivot element from the array.
2. Partition the array around the pivot (elements less than pivot on left, greater on right).
3. If the pivot is at the kth position, return it.
4. If the pivot is at a position less than k, recursively search the right subarray.
5. If the pivot is at a position greater than k, recursively search the left subarray.

```python
def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    # Convert k to index in sorted array (0-indexed)
    k = len(nums) - k
    
    def quickselect(left, right):
        if left == right:
            return nums[left]
        
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1
        
        nums[right], nums[store_index] = nums[store_index], nums[right]
        
        if store_index == k:
            return nums[store_index]
        elif store_index > k:
            return quickselect(left, store_index - 1)
        else:
            return quickselect(store_index + 1, right)
    
    return quickselect(0, len(nums) - 1)
```

- **Time Complexity**: 
  - Average case: O(n) - the algorithm typically only processes a fraction of the array.
  - Worst case: O(n²) - rare with random pivot selection.
- **Space Complexity**: O(1) - the algorithm works in place.

### Approach 4: Sorting

The most straightforward approach is to sort the array and return the kth element from the end:

```python
def find_kth_largest_sorting(nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k-1]
```

- **Time Complexity**: O(n log n) - dominated by the sorting operation.
- **Space Complexity**: O(n) - for storing the sorted array.

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Pros | Cons |
|----------|-----------------|------------------|------|------|
| Built-in Heap | O(n log k) | O(k) | Easy to implement | Doesn't control internal implementation |
| Min Heap | O(n log k) | O(k) | Efficient for large arrays with small k | Not the fastest for all cases |
| QuickSelect | Average: O(n) <br> Worst: O(n²) | O(1) | Optimal average time complexity, in-place | Worst case can be slow |
| Sorting | O(n log n) | O(n) | Simple to understand | Inefficient for large arrays |

## When to Use Each Approach

- **Built-in Heap Function**: When simplicity and readability are priorities.
- **Min Heap of Size K**: When k is much smaller than n and consistent performance is needed.
- **QuickSelect**: When optimal average-case performance is needed and memory is limited.
- **Sorting**: For very small arrays or when the code needs to be extremely simple.

## Edge Cases to Consider

- Array with duplicate elements (note: problem states we want kth largest, not kth distinct)
- k = 1 (largest element) or k = length of array (smallest element)
- Array with negative numbers
- Random input that causes worst-case behavior for QuickSelect 