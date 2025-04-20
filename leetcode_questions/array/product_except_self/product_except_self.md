# Product of Array Except Self

## Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Examples

**Example 1:**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2:**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Approach

The naive approach would be to use division: calculate the product of all elements, then divide by the element at each position. However, the problem states we cannot use division (and this approach would also fail if there are zeros in the array).

Instead, we can use the following approach:

1. Create two arrays: 
   - `L[i]` will contain the product of all elements to the left of `i`.
   - `R[i]` will contain the product of all elements to the right of `i`.
   
2. For the first element, there are no elements to the left, so `L[0] = 1`. Similarly, for the last element, there are no elements to the right, so `R[length-1] = 1`.

3. Fill the `L` array from left to right:
   ```
   L[i] = L[i-1] * nums[i-1]
   ```

4. Fill the `R` array from right to left:
   ```
   R[i] = R[i+1] * nums[i+1]
   ```

5. The answer for each position is the product of the corresponding elements in `L` and `R`:
   ```
   answer[i] = L[i] * R[i]
   ```

## Solution

```python
def product_except_self(nums: List[int]) -> List[int]:
    length = len(nums)
    
    # Initialize arrays
    L = [1 for i in range(length)]
    R = [1 for i in range(length)]
    out = [1 for i in range(length)]
    
    # L[i] contains the product of all elements to the left of i
    for i in range(1, length):
        L[i] = L[i-1] * nums[i-1]
    
    # R[i] contains the product of all elements to the right of i
    R[length-1] = 1
    for i in range(length-1, 0, -1):
        R[i-1] = R[i] * nums[i]
    
    # The final answer is the product of L and R arrays
    for i in range(0, length):
        out[i] = L[i] * R[i]
    
    return out
```

## Time Complexity

- O(n): We perform three passes through the array, each taking O(n) time.

## Space Complexity

- O(n): We use three arrays of size n.

## Optimization for O(1) Extra Space

We can further optimize the space complexity to O(1) extra space (not counting the output array):

```python
def product_except_self(nums: List[int]) -> List[int]:
    length = len(nums)
    answer = [1] * length
    
    # answer[i] contains the product of all elements to the left of i
    for i in range(1, length):
        answer[i] = answer[i-1] * nums[i-1]
    
    # right contains the product of all elements to the right
    right = 1
    for i in range(length-1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    
    return answer
```

In this optimized solution:
1. We use the output array to store the left products first.
2. Then we use a single variable `right` to keep track of the right products as we iterate through the array from right to left.
3. We multiply each element in the output array by the corresponding right product.

This reduces the space complexity to O(1) extra space while maintaining O(n) time complexity. 