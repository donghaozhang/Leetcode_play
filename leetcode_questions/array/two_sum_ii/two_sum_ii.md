# Two Sum II - Input Array is Sorted

## Problem

Given a **1-indexed** array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. These two numbers should be `numbers[index1]` and `numbers[index2]` where 1 ≤ `index1` < `index2` ≤ `numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

**Your solution must use only constant extra space.**

## Examples

**Example 1:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2:**
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

**Example 3:**
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

## Approach: Two Pointers

Since the input array is sorted, we can take advantage of this property to solve the problem efficiently using a two-pointer approach.

### Algorithm:

1. Initialize two pointers, `left` at the beginning of the array (index 0) and `right` at the end of the array (index n-1).
2. Compute the sum of elements at the `left` and `right` pointers.
3. If the sum equals the target, return the indices (adjusted for 1-indexing).
4. If the sum is less than the target, increment the `left` pointer to consider a larger value.
5. If the sum is greater than the target, decrement the `right` pointer to consider a smaller value.
6. Repeat steps 2-5 until a solution is found.

### Python Implementation:

```python
def two_sum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum < target:
            # Sum is too small, move left pointer to increase sum
            left += 1
        else:
            # Sum is too large, move right pointer to decrease sum
            right -= 1
    
    return []  # No solution found
```

## Complexity Analysis

- **Time Complexity**: O(n) where n is the length of the input array. In the worst case, we might need to scan through the entire array once.
- **Space Complexity**: O(1) as we only use a constant amount of extra space regardless of the input size.

## Why Two Pointers Works

The two-pointer approach works for this problem because the array is sorted:

1. When the sum is too small, we know that increasing the left pointer will increase the sum (since we'll be considering a larger value).
2. When the sum is too large, we know that decreasing the right pointer will decrease the sum (since we'll be considering a smaller value).
3. This way, we can systematically explore all possible pairs without having to check every combination.

This approach is more efficient than using a nested loop (which would be O(n²) time complexity) or a hash map (which would be O(n) in both time and space).

## Edge Cases and Considerations

- Since the problem guarantees exactly one solution, we don't need to handle the case where no solution exists.
- The array is 1-indexed in the problem statement, but 0-indexed in our code, so we need to adjust the returned indices.
- The constraints ensure the array has at least 2 elements, so no need to check for empty arrays.
- The two-pointer approach naturally ensures we don't use the same element twice, as required by the problem. 