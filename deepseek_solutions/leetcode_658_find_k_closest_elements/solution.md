# search_big_sorted_array.md)
- 找到K个最接近的元素 / Find K Closest Elements [LeetCode 658]

## Problem Description

Here is the full description of LeetCode problem #658, "Find K Closest Elements," as it appears on LeetCode:

---

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

- `|a - x| < |b - x|`, or
- `|a - x| == |b - x|` and `a < b`

**Example 1:**

```
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

**Example 2:**

```
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
```

**Constraints:**

- `1 <= k <= arr.length`
- `1 <= arr.length <= 10^4`
- `arr` is sorted in **ascending** order.
- `-10^4 <= arr[i], x <= 10^4`

--- 

Let me know if you'd like any further clarification or assistance with this problem!

## Solution

### Problem Explanation
We are given a sorted array `arr`, an integer `k`, and a target value `x`. We need to find the `k` closest elements to `x` in the array. The result should be sorted in ascending order. The "closest" elements are determined by the absolute difference from `x`. If two elements have the same difference, the smaller one is considered closer.

### Approach
1. **Binary Search to Find the Closest Element**: First, we find the position of the element in the array that is closest to `x` using binary search. This helps us locate the starting point around which the `k` closest elements will lie.
2. **Two Pointers to Expand the Window**: Once we have the closest element, we use two pointers (left and right) to expand the window around this element to include the `k` closest elements. The left pointer moves leftwards, and the right pointer moves rightwards, comparing the elements at these positions to decide which one is closer to `x`.
3. **Select the k Closest Elements**: After expanding the window to include `k` elements, we slice the array from `left` to `right` and return the result.

### Solution Code
```python
def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - k
    
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]

# Test cases
test1 = [1,2,3,4,5]
k1 = 4
x1 = 3
print(findClosestElements(test1, k1, x1))  # Output: [1,2,3,4]

test2 = [1,2,3,4,5]
k2 = 4
x2 = -1
print(findClosestElements(test2, k2, x2))  # Output: [1,2,3,4]

test3 = [1,1,1,10,10,10]
k3 = 1
x3 = 9
print(findClosestElements(test3, k3, x3))  # Output: [10]

test4 = [1,3,6,7,8]
k4 = 3
x4 = 5
print(findClosestElements(test4, k4, x4))  # Output: [3,6,7]
```

### Explanation
1. **Binary Search for Window Start**: The binary search is used to find the starting index of the `k` closest elements. The condition `x - arr[mid] > arr[mid + k] - x` checks if the element at `mid + k` is closer to `x` than the element at `mid`. If true, the window is moved to the right; otherwise, it stays or moves left.
2. **Window Selection**: Once the binary search completes, `left` will be at the starting index of the `k` closest elements. The result is then simply the subarray from `left` to `left + k`.

### Time and Space Complexity
- **Time Complexity**: O(log(n - k) + k), where `n` is the length of the array. The binary search runs in O(log(n - k)) time, and slicing the array takes O(k) time.
- **Space Complexity**: O(1) if we consider the output space as not part of the space complexity (since the output is required). Otherwise, O(k) for storing the result.

### Test Cases
1. **Test Case 1**: The closest 4 elements to 3 in [1,2,3,4,5] are [1,2,3,4].
2. **Test Case 2**: The closest 4 elements to -1 in [1,2,3,4,5] are [1,2,3,4] because all elements are larger than -1.
3. **Test Case 3**: The closest 1 element to 9 in [1,1,1,10,10,10] is [10].
4. **Test Case 4**: The closest 3 elements to 5 in [1,3,6,7,8] are [3,6,7] as they are the nearest to 5.