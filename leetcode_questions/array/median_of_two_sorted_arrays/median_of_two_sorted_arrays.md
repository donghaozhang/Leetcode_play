# Median of Two Sorted Arrays

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

## Examples

**Example 1:**
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

## Constraints

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

## Approach: Binary Search on Partition

The solution uses a binary search approach to find the correct partition point between the two arrays that gives us the median. The key insight is that we can find the median by finding a partition that divides the combined array into two equal halves (or nearly equal for odd lengths).

### Key Components:

1. **Array Partitioning**:
   ```python
   # Ensure nums1 is the smaller array
   if len(nums1) > len(nums2):
       nums1, nums2 = nums2, nums1
   ```

2. **Binary Search Setup**:
   ```python
   m, n = len(nums1), len(nums2)
   total = m + n
   half = (total + 1) // 2
   ```

3. **Partition Finding**:
   ```python
   while left <= right:
       i = (left + right) // 2
       j = half - i
       
       nums1_left = float('-inf') if i == 0 else nums1[i-1]
       nums1_right = float('inf') if i == m else nums1[i]
       nums2_left = float('-inf') if j == 0 else nums2[j-1]
       nums2_right = float('inf') if j == n else nums2[j]
   ```

4. **Median Calculation**:
   ```python
   if nums1_left <= nums2_right and nums2_left <= nums1_right:
       if total % 2 == 1:
           return max(nums1_left, nums2_left)
       else:
           return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
   ```

## Complexity Analysis

- **Time Complexity**: O(log(min(m, n)))
  - We perform binary search on the smaller array
  - Each iteration takes O(1) time
  - The number of iterations is logarithmic in the size of the smaller array

- **Space Complexity**: O(1)
  - We use only constant extra space
  - No additional data structures are created

## Why This Approach Works

1. **Efficiency**:
   - Achieves O(log(min(m, n))) time complexity
   - Avoids merging the arrays
   - Minimizes the number of comparisons

2. **Correctness**:
   - Finds the correct partition that divides the combined array into two equal halves
   - Handles both odd and even total lengths
   - Works for all edge cases (empty arrays, single element arrays, etc.)

3. **Partition Logic**:
   - The partition must satisfy:
     - All elements on the left side are less than or equal to all elements on the right side
     - The number of elements on both sides is equal (or differs by 1 for odd lengths)

## Example Walkthrough

For nums1 = [1, 3] and nums2 = [2]:

1. **Initial Setup**:
   - nums1 is already the smaller array
   - m = 2, n = 1
   - total = 3, half = 2

2. **First Partition**:
   - i = 1 (partition in nums1)
   - j = 1 (partition in nums2)
   - nums1_left = 1, nums1_right = 3
   - nums2_left = 2, nums2_right = inf
   - Check: 1 <= inf and 2 <= 3 → valid partition
   - Total is odd → return max(1, 2) = 2

The median is found in O(log(min(m, n))) time without merging the arrays. 