# 3Sum

## Problem Description
Given an integer array `nums`, find all triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k` (elements at distinct indices)
- `nums[i] + nums[j] + nums[k] == 0` (sum to zero)

The solution set must not contain duplicate triplets.

## Examples

### Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Note that the order of the output and the order of the triplets does not matter.
```

### Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

### Example 3:
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

## Constraints
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

## Solution Approach
The problem can be solved efficiently using a sorting-based two-pointer approach:

1. **Sort the input array**: This is key for efficiently handling duplicates and using the two-pointer technique.
2. **Iterate through each element** as a potential first element of the triplet.
3. **Use two pointers** (left and right) to find the other two elements that sum to the target.
4. **Skip duplicates** to avoid returning the same triplet multiple times.

### Detailed Steps:

1. Sort the array in ascending order.
2. Iterate through the array with index `i` from 0 to n-3 (since we need at least 3 elements).
3. Skip duplicate values for the first element (if `nums[i] == nums[i-1]`).
4. For each valid first element `nums[i]`:
   - Set two pointers: `left = i + 1` and `right = n - 1`.
   - While `left < right`:
     - Calculate `sum = nums[i] + nums[left] + nums[right]`.
     - If `sum < 0`, increment `left` to increase the sum.
     - If `sum > 0`, decrement `right` to decrease the sum.
     - If `sum == 0`, we found a triplet:
       - Add `[nums[i], nums[left], nums[right]]` to the result.
       - Skip any duplicate values for `nums[left]` and `nums[right]`.
       - Move both pointers inward to find more triplets.

### Time Complexity:
- Sorting the array takes O(n log n) time.
- The two-pointer approach takes O(n²) time in the worst case.
- Overall time complexity: O(n²).

### Space Complexity:
- O(1) extra space for the algorithm itself (excluding the output array).
- The output array size depends on the number of valid triplets found.

## Key Insights
1. **Sorting** helps in two ways: it makes duplicate handling easier and enables the two-pointer approach.
2. **Handling duplicates** is crucial to avoid reporting the same triplet multiple times.
3. The **two-pointer technique** is more efficient than a naive three-nested-loop approach, which would be O(n³).

## Code Implementation
```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    # Sort the array to handle duplicates and use two pointers approach
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Two pointers approach for the remaining two elements
        left, right = i + 1, n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                # Sum is too small, move left pointer to increase the sum
                left += 1
            elif total > 0:
                # Sum is too large, move right pointer to decrease the sum
                right -= 1
            else:
                # Found a triplet with sum = 0
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicate values for second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate values for third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers to find more triplets
                left += 1
                right -= 1
                
    return result
```

## Related Problems
- **Two Sum**: Find a pair of elements that sum to a target.
- **4Sum**: Find quadruplets that sum to a target.
- **3Sum Closest**: Find a triplet with sum closest to a target. 