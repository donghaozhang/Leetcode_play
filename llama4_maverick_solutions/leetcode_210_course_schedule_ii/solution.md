# topological_sort.md)
- 课程表 II / Course Schedule II [LeetCode 210]

## Problem Description

## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.

- For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

Return _the ordering of courses you should take to finish all courses_. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

### Example 1:

**Input:** `numCourses = 2, prerequisites = [[1,0]]`
**Output:** `[0,1]`
**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is `[0, 1]`.

### Example 2:

**Input:** `numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
**Output:** `[0,2,1,3]`
**Explanation:** There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is `[0,1,2,3]`. Another correct ordering is `[0,2,1,3]`.

### Example 3:

**Input:** `numCourses = 1, prerequisites = []`
**Output:** `[0]`

### Constraints:

* `1 <= numCourses <= 2000`
* `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
* `prerequisites[i].length == 2`
* `0 <= a_i, b_i < numCourses`
* `a_i != b_i`
* All the pairs `[a_i, b_i]` are **distinct**.

## Solution

## Problem Explanation

The problem is to determine the order in which a student should take a set of courses, given a list of prerequisites that specify which courses must be taken before others. The input consists of the number of courses (`numCourses`) and a list of prerequisites (`prerequisites`), where each prerequisite is a pair of courses (`a_i`, `b_i`) indicating that course `b_i` must be taken before course `a_i`. The output is a list of courses in a valid order, or an empty list if it is impossible to finish all courses due to a cycle in the prerequisites.

## Step-by-Step Approach

1. **Build a Graph**: Create a directed graph where each node represents a course, and a directed edge from node `b_i` to node `a_i` represents the prerequisite relationship (`a_i`, `b_i`).
2. **Calculate In-Degree**: For each node (course), calculate its in-degree, which is the number of edges pointing to it. This represents the number of prerequisites for the course.
3. **Topological Sort**: Perform a topological sort on the graph. Start by enqueuing all nodes with an in-degree of 0 (courses with no prerequisites). Then, iteratively dequeue a node, decrease the in-degree of its neighbors, and enqueue any neighbor whose in-degree becomes 0.
4. **Check for Cycle**: If the number of nodes visited (courses taken) is less than the total number of courses, it indicates a cycle in the graph, and it is impossible to finish all courses. Return an empty list in this case.
5. **Return the Order**: Otherwise, return the list of courses in the order they were visited.

## Python Solution

```python
from collections import defaultdict, deque

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # Build the graph and calculate in-degree
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        in_degree[course] += 1
    
    # Initialize queue with nodes having in-degree 0
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    
    # Topological sort
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all courses can be finished
    if len(order) != numCourses:
        return []
    
    return order

# Test cases
if __name__ == "__main__":
    test_cases = [
        (2, [[1,0]], [0,1]),
        (4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3]),  # One valid order
        (4, [[1,0],[2,0],[3,1],[3,2]], [0,2,1,3]),  # Another valid order
        (1, [], [0]),
        (3, [[1,0],[2,1],[0,2]], []),  # Cycle
    ]
    
    for numCourses, prerequisites, expected in test_cases:
        result = findOrder(numCourses, prerequisites)
        print(f"Input: numCourses = {numCourses}, prerequisites = {prerequisites}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        assert result == expected or (len(expected) > 1 and result in [[0,2,1,3], [0,1,2,3]]), f"Test case failed for numCourses = {numCourses}, prerequisites = {prerequisites}"
        print("-" * 50)
```

## Time and Space Complexity Analysis

- **Time Complexity**: O(N + M), where N is the number of courses (`numCourses`) and M is the number of prerequisites. This is because we iterate over all prerequisites once to build the graph and calculate in-degrees, and then we visit each node once during the topological sort.
- **Space Complexity**: O(N + M), for storing the graph and the in-degrees of all nodes. The graph can have up to M edges, and we need O(N) space for in-degrees and the queue in the worst case.

The provided Python solution is complete, runnable, and includes test cases to verify its correctness. It handles various scenarios, including cases with cycles in the prerequisites.