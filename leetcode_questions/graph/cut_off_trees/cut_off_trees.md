# Cut Off Trees for Golf Event

## Problem

You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix where:
- 0 means the cell cannot be walked through
- 1 represents an empty cell that can be walked through
- A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

## Examples

**Example 1:**
```
Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
```

**Example 2:**
```
Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
Output: -1
Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
```

**Example 3:**
```
Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
Output: 6
Explanation: You can follow the same path as Example 1 to cut off all the trees.
Note that you can cut off the first tree at (0, 0) before making any steps.
```

## Constraints

- m == forest.length
- n == forest[i].length
- 1 <= m, n <= 50
- 0 <= forest[i][j] <= 10^9
- Heights of all trees are distinct.

## Approach: BFS with Priority Queue

The solution uses a combination of BFS and a priority queue to solve the problem. Here's how it works:

1. **Tree Collection**:
   - First, collect all trees and store them in a priority queue sorted by height
   - This ensures we process trees in order from shortest to tallest

2. **Path Finding**:
   - For each tree in order, find the shortest path from current position to the next tree
   - Use BFS to find the shortest path between two points
   - Keep track of visited cells to avoid cycles

3. **Tree Cutting**:
   - After reaching a tree, mark it as cut (set its value to 1)
   - Update the current position to the tree's location
   - Continue with the next tree in the priority queue

### Key Components:

1. **Priority Queue for Trees**:
   ```python
   trees = []
   for x in range(m):
       for y in range(n):
           height = forest[x][y]
           if height > 1:
               heapq.heappush(trees, (height, x, y))
   ```

2. **BFS Implementation**:
   ```python
   def bfs(start_x: int, start_y: int, target_x: int, target_y: int) -> int:
       queue = collections.deque([(start_x, start_y, 0)])
       visited = {(start_x, start_y)}
       
       while queue:
           x, y, steps = queue.popleft()
           if x == target_x and y == target_y:
               forest[x][y] = 1
               return steps
           
           for dx, dy in [(-1,0), (0,1), (0,-1), (1,0)]:
               nx, ny = x + dx, y + dy
               if (0 <= nx < m and 0 <= ny < n and 
                   forest[nx][ny] >= 1 and 
                   (nx, ny) not in visited):
                   queue.append((nx, ny, steps + 1))
                   visited.add((nx, ny))
       
       return -1
   ```

### Python Implementation:

```python
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        
        # Store all trees in priority queue
        trees = []
        for x in range(m):
            for y in range(n):
                height = forest[x][y]
                if height > 1:
                    heapq.heappush(trees, (height, x, y))
        
        def bfs(start_x: int, start_y: int, target_x: int, target_y: int) -> int:
            queue = collections.deque([(start_x, start_y, 0)])
            visited = {(start_x, start_y)}
            
            while queue:
                x, y, steps = queue.popleft()
                if x == target_x and y == target_y:
                    forest[x][y] = 1
                    return steps
                
                for dx, dy in [(-1,0), (0,1), (0,-1), (1,0)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < m and 0 <= ny < n and 
                        forest[nx][ny] >= 1 and 
                        (nx, ny) not in visited):
                        queue.append((nx, ny, steps + 1))
                        visited.add((nx, ny))
            
            return -1
        
        x, y = 0, 0
        total_steps = 0
        
        while trees:
            _, next_x, next_y = heapq.heappop(trees)
            steps = bfs(x, y, next_x, next_y)
            if steps == -1:
                return -1
            total_steps += steps
            x, y = next_x, next_y
        
        return total_steps
```

## Complexity Analysis

- **Time Complexity**: O(m²n²)
  - For each tree, we perform a BFS that can take O(mn) time
  - In the worst case, there can be O(mn) trees
  - Therefore, total time is O(m²n²)

- **Space Complexity**: O(mn)
  - Space needed for the priority queue: O(mn)
  - Space needed for BFS queue and visited set: O(mn)
  - Total space is O(mn)

## Why This Approach Works

1. **Optimal Path Finding**:
   - BFS guarantees the shortest path between two points
   - We process trees in order of height, ensuring we follow the required sequence
   - The visited set prevents revisiting cells, ensuring efficiency

2. **Correctness**:
   - The solution handles all edge cases
   - It correctly identifies when trees are unreachable
   - It maintains the forest state by marking cut trees as empty cells

3. **Efficiency**:
   - The priority queue ensures we process trees in the correct order
   - BFS is optimal for finding shortest paths in unweighted grids
   - The visited set prevents unnecessary exploration

## Example Walkthrough

For forest = [[1,2,3],[0,0,4],[7,6,5]]:

1. Collect trees in order: (2,0,1), (3,0,2), (4,1,2), (5,2,2), (6,2,1), (7,2,0)
2. Start at (0,0)
3. Find path to (0,1) - tree height 2
4. Find path to (0,2) - tree height 3
5. Find path to (1,2) - tree height 4
6. Find path to (2,2) - tree height 5
7. Find path to (2,1) - tree height 6
8. Find path to (2,0) - tree height 7
9. Total steps: 6 