# 3Sum Closest

## Problem Description
Given an integer array `nums` of length n and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

## Examples

### Example 1:
```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

### Example 2:
```
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
```

## Constraints
- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4

## Solution Approach
This problem is a variation of the 3Sum problem, but instead of finding triplets that sum exactly to zero, we need to find a triplet whose sum is closest to the target.

We can use a similar approach with sorting and two pointers:

1. **Sort the input array**: This will allow us to use the two-pointer technique efficiently.
2. **Fix one element** and use two pointers to find the other two elements.
3. **Track the closest sum**: For each triplet, calculate how close its sum is to the target and update if it's closer than the previous best.
4. **Optimize the search**: Move the pointers based on whether the current sum is greater or less than the target.

### Detailed Steps:

1. Sort the array in ascending order.
2. Initialize a variable `closest_sum` to store the sum closest to the target (initialized to infinity).
3. Iterate through the array with index `i` from 0 to n-3.
4. Skip duplicate values for the first element (if `nums[i] == nums[i-1]`).
5. For each valid first element `nums[i]`:
   - Set two pointers: `left = i + 1` and `right = n - 1`.
   - While `left < right`:
     - Calculate the current sum: `current_sum = nums[i] + nums[left] + nums[right]`.
     - If `|current_sum - target| < |closest_sum - target|`, update `closest_sum = current_sum`.
     - If `current_sum == target`, we can return immediately as this is the exact match.
     - If `current_sum < target`, increment `left` to try to get closer to the target.
     - If `current_sum > target`, decrement `right` to try to get closer to the target.
6. Return the `closest_sum`.

### Time Complexity:
- Sorting the array takes O(n log n) time.
- The two-pointer approach takes O(n²) time in the worst case.
- Overall time complexity: O(n²).

### Space Complexity:
- O(1) extra space (or O(log n) if considering space used by the sorting algorithm).

## Key Insights
1. **Use of sorting**: Sorting is key for the two-pointer approach to work efficiently.
2. **Early termination**: If we find a triplet with a sum exactly equal to the target, we can return immediately.
3. **Update strategy**: We update our answer when we find a sum that's closer to the target than our current closest sum.
4. **Pointer movement**: If the current sum is less than target, we move the left pointer to increase the sum; if the current sum is greater than target, we move the right pointer to decrease the sum.

## Code Implementation
```python
def threeSumClosest(self, nums: List[int], target: int) -> int:
    # Sort the array to use two pointers approach
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    
    for i in range(n - 2):
        # Skip duplicate values for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Two pointers approach for the remaining two elements
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # Update closest sum if current sum is closer to target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            # If we found exact match, return immediately
            if current_sum == target:
                return target
            
            # Adjust pointers based on comparison with target
            if current_sum < target:
                left += 1
            else:  # current_sum > target
                right -= 1
                
    return closest_sum
```

## Related Problems
- **3Sum**: Find all unique triplets that sum to zero.
- **3Sum Smaller**: Count triplets with sum less than target.
- **4Sum**: Find all unique quadruplets that sum to a given target. 