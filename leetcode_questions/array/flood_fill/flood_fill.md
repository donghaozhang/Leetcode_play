# Flood Fill

## Problem

Given an image represented by an m x n grid of integers `image`, where `image[i][j]` represents the pixel value of the image, perform a flood fill starting from the pixel `image[sr][sc]` with a new color.

To perform a flood fill:
1. Begin with the starting pixel and change its color to the new color
2. Perform the same process for each pixel that is directly adjacent (horizontally or vertically) and shares the same color as the starting pixel
3. Continue this process for all connected pixels of the same color
4. Return the modified image

## Examples

**Example 1:**
```
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
```

**Example 2:**
```
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
```

## Constraints

- m == image.length
- n == image[i].length
- 1 <= m, n <= 50
- 0 <= image[i][j], color < 2^16
- 0 <= sr < m
- 0 <= sc < n

## Approach: Depth-First Search (DFS)

The solution uses a depth-first search approach to perform the flood fill. Here's how it works:

1. **Initial Check**: 
   - Get the original color at the starting position
   - If the new color is the same as the original, return the image immediately

2. **DFS Function**:
   - Recursively visit all adjacent pixels (up, down, left, right)
   - Change the color of each visited pixel to the new color
   - Continue until no more connected pixels of the original color are found

### Key Components:

1. **Base Case**:
   ```python
   if original_color == newColor:
       return image
   ```

2. **DFS Implementation**:
   ```python
   def dfs(row: int, col: int):
       if image[row][col] == original_color:
           image[row][col] = newColor
           # Check adjacent pixels
           if row > 0: dfs(row - 1, col)
           if row < len(image) - 1: dfs(row + 1, col)
           if col > 0: dfs(row, col - 1)
           if col < len(image[0]) - 1: dfs(row, col + 1)
   ```

### Python Implementation:

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == newColor:
            return image
            
        def dfs(row: int, col: int):
            if image[row][col] == original_color:
                image[row][col] = newColor
                if row > 0: dfs(row - 1, col)
                if row < len(image) - 1: dfs(row + 1, col)
                if col > 0: dfs(row, col - 1)
                if col < len(image[0]) - 1: dfs(row, col + 1)
        
        dfs(sr, sc)
        return image
```

## Complexity Analysis

- **Time Complexity**: O(m * n)
  - In the worst case, we might need to visit every pixel in the image
  - Each pixel is visited exactly once

- **Space Complexity**: O(m * n)
  - The space is used by the recursion stack
  - In the worst case, the recursion stack can grow up to m * n levels deep

## Why This Approach Works

1. **Systematic Exploration**:
   - DFS ensures we visit all connected pixels of the same color
   - We only change colors of pixels that match the original color
   - The process stops when no more connected pixels of the original color are found

2. **Efficiency**:
   - Each pixel is visited exactly once
   - We avoid unnecessary work by checking if the new color is different from the original
   - The recursive approach naturally handles the connected nature of the pixels

3. **Correctness**:
   - The solution correctly handles all edge cases
   - It only changes colors of connected pixels
   - It maintains the original image structure

## Example Walkthrough

For image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2:

1. Start at position (1,1) with color 1
2. Change color to 2
3. Check adjacent pixels:
   - Up: (0,1) - color 1 → change to 2
   - Down: (2,1) - color 0 → skip
   - Left: (1,0) - color 1 → change to 2
   - Right: (1,2) - color 0 → skip
4. Continue with newly changed pixels:
   - From (0,1): check adjacent pixels
   - From (1,0): check adjacent pixels
5. Final result: [[2,2,2],[2,2,0],[2,0,1]] 