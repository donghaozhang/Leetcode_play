from typing import List
import heapq
import collections

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        Calculate the minimum steps needed to cut all trees in order of their height.
        
        Args:
            forest: 2D list representing the forest where:
                   - 0 means obstacle
                   - 1 means empty cell
                   - >1 means tree with height
            
        Returns:
            Minimum steps needed to cut all trees, or -1 if impossible
        """
        m, n = len(forest), len(forest[0])
        
        # Store all trees in priority queue in (height, x, y) format
        trees = []
        for x in range(m):
            for y in range(n):
                height = forest[x][y]
                if height > 1:
                    heapq.heappush(trees, (height, x, y))
        
        def bfs(start_x: int, start_y: int, target_x: int, target_y: int) -> int:
            """
            Find shortest path from start to target using BFS.
            
            Args:
                start_x, start_y: Starting position
                target_x, target_y: Target position
                
            Returns:
                Minimum steps to reach target, or -1 if impossible
            """
            queue = collections.deque([(start_x, start_y, 0)])
            visited = {(start_x, start_y)}
            
            while queue:
                x, y, steps = queue.popleft()
                
                if x == target_x and y == target_y:
                    # Found the target tree, mark it as cut
                    forest[x][y] = 1
                    return steps
                
                # Check adjacent cells (up, right, left, down)
                for dx, dy in [(-1,0), (0,1), (0,-1), (1,0)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < m and 0 <= ny < n and 
                        forest[nx][ny] >= 1 and 
                        (nx, ny) not in visited):
                        queue.append((nx, ny, steps + 1))
                        visited.add((nx, ny))
            
            return -1
        
        # Start from (0,0) and cut trees in order
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

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    forest1 = [[1,2,3],[0,0,4],[7,6,5]]
    print(f"Example 1: {solution.cutOffTree(forest1)}")  # Expected: 6
    
    # Example 2
    forest2 = [[1,2,3],[0,0,0],[7,6,5]]
    print(f"Example 2: {solution.cutOffTree(forest2)}")  # Expected: -1
    
    # Example 3
    forest3 = [[2,3,4],[0,0,5],[8,7,6]]
    print(f"Example 3: {solution.cutOffTree(forest3)}")  # Expected: 6 