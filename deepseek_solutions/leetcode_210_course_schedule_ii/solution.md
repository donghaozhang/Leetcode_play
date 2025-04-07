# topological_sort.md)
- 课程表 II / Course Schedule II [LeetCode 210]

## Problem Description

# 210. Course Schedule II

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

### Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

### Example 2:
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

### Example 3:
```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

### Constraints:
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`
- All the pairs `[ai, bi]` are distinct.

## Solution

### Problem Explanation
The problem is about determining the order in which courses should be taken given their prerequisites. This is a classic topological sorting problem where we need to arrange the courses in such a way that every course is taken only after all its prerequisites have been completed. If there's a cycle in the prerequisites, it's impossible to complete all courses, and we should return an empty array.

### Approach
1. **Graph Representation**: Represent the courses and their prerequisites as a directed graph. Each course is a node, and a directed edge from node `b` to node `a` indicates that course `a` requires course `b` to be completed first.
2. **Indegree Calculation**: For each node, calculate the number of incoming edges (indegree), which represents the number of prerequisites that need to be completed before taking that course.
3. **Topological Sort using Kahn's Algorithm**:
   - **Initialization**: Start with nodes that have an indegree of 0 (no prerequisites) and add them to a queue.
   - **Processing**: For each node in the queue, remove it from the graph (conceptually), and reduce the indegree of its neighbors. If any neighbor's indegree becomes 0, add it to the queue.
   - **Result Collection**: The nodes are added to the result list in the order they are processed.
4. **Cycle Detection**: If the result list's length is less than the number of courses, it means there's a cycle in the graph, and we return an empty array.

### Solution Code
```python
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize the graph and in_degree array
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # Build the graph and in_degree
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        # Initialize the queue with courses having 0 in_degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []
        
        while queue:
            course = queue.popleft()
            result.append(course)
            
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == numCourses else []
```

### Time and Space Complexity Analysis
- **Time Complexity**: O(V + E), where V is the number of courses (numCourses) and E is the number of prerequisites. Each node and edge is processed exactly once.
- **Space Complexity**: O(V + E), for storing the graph and in_degree array. The queue can take up to O(V) space in the worst case.

### Test Cases
1. **Example 1**:
   - Input: `numCourses = 2`, `prerequisites = [[1,0]]`
   - Output: `[0,1]`
   - Explanation: Course 0 must be taken before course 1.

2. **Example 2**:
   - Input: `numCourses = 4`, `prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
   - Output: `[0,1,2,3]` or `[0,2,1,3]`
   - Explanation: Multiple valid orders exist where all prerequisites are satisfied.

3. **Example 3**:
   - Input: `numCourses = 1`, `prerequisites = []`
   - Output: `[0]`
   - Explanation: Only one course with no prerequisites.

4. **Cycle Detection**:
   - Input: `numCourses = 2`, `prerequisites = [[0,1],[1,0]]`
   - Output: `[]`
   - Explanation: The courses have a cyclic dependency, making it impossible to complete both.

5. **No Prerequisites**:
   - Input: `numCourses = 3`, `prerequisites = []`
   - Output: `[0,1,2]` (or any permutation)
   - Explanation: No prerequisites mean any order is valid.

These test cases cover typical scenarios, including no prerequisites, multiple valid orders, and cyclic dependencies.