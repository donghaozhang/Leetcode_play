# Container With Most Water

## Problem

You are given an integer array `height` of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

## Examples

**Example 1:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The container formed by lines at indices 1 and 8 (height values 8 and 7) has the largest area: min(8, 7) * (8 - 1) = 7 * 7 = 49
```

**Example 2:**
```
Input: height = [1,1]
Output: 1
```

## Approach: Two Pointer Technique

The key insight is that the area of water contained between two lines is determined by:
1. The width between the lines (difference in indices)
2. The height of the shorter line (water will overflow above the shorter line)

We can use a two-pointer approach, starting from both ends of the array:

1. Initialize two pointers, one at the beginning (`left = 0`) and one at the end (`right = length - 1`) of the array.
2. Calculate the area formed by the lines at these two pointers.
3. Move the pointer that points to the shorter line inward (since we want to find a potentially taller line).
4. Repeat steps 2-3 until the pointers meet.
5. Track the maximum area seen during this process.

The intuition is that if we move the pointer with the greater height inward, the width decreases and the height remains constrained by the shorter line, so the area can only decrease. Therefore, we always move the pointer with the shorter height.

## Solution

```python
def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area_value = 0
    
    while left < right:
        # Calculate width between two lines
        width = right - left
        
        # Calculate area based on the shorter line
        if height[right] > height[left]:
            area = width * height[left]
            left += 1  # Move left pointer inward
        else:
            area = width * height[right]
            right -= 1  # Move right pointer inward
            
        # Update maximum area
        max_area_value = max(max_area_value, area)
    
    return max_area_value
```

## Time Complexity

- O(n): We make a single pass through the array with the two pointers.

## Space Complexity

- O(1): We only use a constant amount of extra space regardless of the input size.

## Why This Approach Works

1. **Greedy Choice**: By always moving the pointer pointing to the shorter line, we eliminate the limiting factor for the current area and explore the possibility of finding a taller line that could potentially form a larger area.

2. **Optimality**: The algorithm ensures we consider all potentially optimal pairs of lines. When we move a pointer, we might decrease the width, but we're hoping to gain more in height to compensate. If we moved the pointer at the taller line, we'd decrease width and the height would still be limited by the shorter line, resulting in a definite decrease in area.

3. **Completeness**: By the time the two pointers meet, we've considered all potentially optimal pairs of lines. 