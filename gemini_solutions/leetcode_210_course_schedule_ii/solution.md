# topological_sort.md)
- 课程表 II / Course Schedule II [LeetCode 210]

## Problem Description

`210. Course Schedule II`

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

*   For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return *the ordering of courses you should take to finish all courses*. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

**Example 2:**

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

**Example 3:**

```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

**Constraints:**

*   `1 <= numCourses <= 2000`
*   `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
*   `prerequisites[i].length == 2`
*   `0 <= ai, bi < numCourses`
*   `ai != bi`
*   All the pairs `[ai, bi]` are **distinct**.

## Solution

Okay, let's break down the Course Schedule II problem.

**1. Explanation of the Problem**

The problem asks us to find a valid sequence of courses to take, given a set of prerequisites. A prerequisite `[a, b]` means we must complete course `b` before we can start course `a`. If it's possible to complete all courses while respecting these prerequisites, we should return one such valid order. If it's impossible (because the prerequisites form a cycle, like needing course A before B, and B before A), we should return an empty array.

This is a classic example of a **topological sort** problem on a directed graph. We can model the courses as nodes in a graph, and a prerequisite `[a, b]` as a directed edge from `b` to `a` ( `b -> a` ), signifying that `b` must come before `a`. The goal is to find a linear ordering of the nodes such that for every directed edge `u -> v`, node `u` comes before node `v` in the ordering. A topological sort is only possible if the graph is a Directed Acyclic Graph (DAG). If the graph contains a cycle, no such ordering exists.

**2. Step-by-Step Approach (Using Kahn's Algorithm - BFS based)**

Kahn's algorithm is a common and intuitive way to perform topological sorting. Here's how it works:

1.  **Represent the Graph:**
    *   Create an adjacency list `adj` where `adj[i]` contains a list of courses that have course `i` as a prerequisite (i.e., if `[a, b]` is a prerequisite, there's an edge `b -> a`, so `a` is added to `adj[b]`).
    *   Create an array `in_degree` of size `numCourses`, initialized to zeros. `in_degree[i]` will store the number of prerequisites for course `i`.

2.  **Build Graph and In-Degrees:**
    *   Iterate through the `prerequisites` list. For each prerequisite `[a, b]`:
        *   Add `a` to the adjacency list of `b`: `adj[b].append(a)`.
        *   Increment the in-degree of `a`: `in_degree[a] += 1`.

3.  **Initialize the Queue:**
    *   Create a queue (e.g., `collections.deque`).
    *   Find all courses with an in-degree of 0 (courses with no prerequisites) and add them to the queue. These are the starting points.

4.  **Process Courses:**
    *   Initialize an empty list `result` to store the topological order.
    *   While the queue is not empty:
        *   Dequeue a course `u` from the front of the queue.
        *   Add `u` to the `result` list.
        *   For each neighbor `v` of `u` (i.e., for each course `v` that has `u` as a prerequisite, found in `adj[u]`):
            *   Decrement the in-degree of `v`: `in_degree[v] -= 1`. This signifies that one of its prerequisites (`u`) has been completed.
            *   If the in-degree of `v` becomes 0, it means all prerequisites for `v` are now met. Enqueue `v`.

5.  **Check for Cycles:**
    *   After the loop finishes, if the number of courses in the `result` list is equal to `numCourses`, then a valid topological sort was found. Return `result`.
    *   If the number of courses in `result` is less than `numCourses`, it means there was a cycle in the graph (some nodes never reached an in-degree of 0 because they were part of a cycle). Return an empty list `[]`.

**3. Python Solution**

```python
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Finds a valid course order using topological sort (Kahn's Algorithm).

        Args:
            numCourses: The total number of courses.
            prerequisites: A list of prerequisite pairs [a, b], meaning b must be taken before a.

        Returns:
            A list representing a valid course order, or an empty list if impossible.
        """

        # 1. Initialize graph representation and in-degrees
        adj = collections.defaultdict(list)
        in_degree = [0] * numCourses

        # 2. Build adjacency list and calculate in-degrees
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        # 3. Initialize the queue with courses having 0 in-degree
        queue = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])

        result = [] # To store the topological order

        # 4. Process the queue
        while queue:
            u = queue.popleft()
            result.append(u)

            # Process neighbors
            for v in adj[u]:
                in_degree[v] -= 1
                # If all prerequisites for v are met, add it to the queue
                if in_degree[v] == 0:
                    queue.append(v)

        # 5. Check if a valid order was found (all courses included)
        if len(result) == numCourses:
            return result
        else:
            # A cycle was detected
            return []

# --- Test Cases ---
def run_tests():
    sol = Solution()

    # Example 1: Simple linear dependency
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    expected1 = [0, 1]
    result1 = sol.findOrder(numCourses1, prerequisites1)
    print(f"Test Case 1: Input ({numCourses1}, {prerequisites1})")
    print(f"Output: {result1}")
    print(f"Expected: {expected1}")
    print(f"Pass: {result1 == expected1}")
    print("-" * 20)

    # Example 2: More complex DAG
    numCourses2 = 4
    prerequisites2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    # Expected can be [0, 1, 2, 3] or [0, 2, 1, 3]
    expected_options2 = [[0, 1, 2, 3], [0, 2, 1, 3]]
    result2 = sol.findOrder(numCourses2, prerequisites2)
    print(f"Test Case 2: Input ({numCourses2}, {prerequisites2})")
    print(f"Output: {result2}")
    print(f"Expected: {expected_options2[0]} or {expected_options2[1]}")
    print(f"Pass: {result2 in expected_options2}")
    print("-" * 20)

    # Example 3: Single course, no prerequisites
    numCourses3 = 1
    prerequisites3 = []
    expected3 = [0]
    result3 = sol.findOrder(numCourses3, prerequisites3)
    print(f"Test Case 3: Input ({numCourses3}, {prerequisites3})")
    print(f"Output: {result3}")
    print(f"Expected: {expected3}")
    print(f"Pass: {result3 == expected3}")
    print("-" * 20)

    # Test Case 4: Cycle detected
    numCourses4 = 2
    prerequisites4 = [[1, 0], [0, 1]]
    expected4 = []
    result4 = sol.findOrder(numCourses4, prerequisites4)
    print(f"Test Case 4: Input ({numCourses4}, {prerequisites4})")
    print(f"Output: {result4}")
    print(f"Expected: {expected4}")
    print(f"Pass: {result4 == expected4}")
    print("-" * 20)

    # Test Case 5: No prerequisites
    numCourses5 = 3
    prerequisites5 = []
    # Any permutation of [0, 1, 2] is valid. We check if the length is correct
    # and all elements are present.
    result5 = sol.findOrder(numCourses5, prerequisites5)
    print(f"Test Case 5: Input ({numCourses5}, {prerequisites5})")
    print(f"Output: {result5}")
    print(f"Expected: Any permutation of [0, 1, 2]")
    is_valid5 = len(result5) == numCourses5 and set(result5) == set(range(numCourses5))
    print(f"Pass: {is_valid5}")
    print("-" * 20)

    # Test Case 6: Disconnected components
    numCourses6 = 5
    prerequisites6 = [[1, 0], [3, 2]]
    # Expected: An order where 0 comes before 1, and 2 comes before 3.
    # Course 4 can be anywhere. e.g., [0, 2, 1, 3, 4], [2, 0, 3, 1, 4], [4, 0, 1, 2, 3] etc.
    result6 = sol.findOrder(numCourses6, prerequisites6)
    print(f"Test Case 6: Input ({numCourses6}, {prerequisites6})")
    print(f"Output: {result6}")
    print(f"Expected: A valid topological sort")
    # Basic validation: check length and content
    is_valid6 = len(result6) == numCourses6 and set(result6) == set(range(numCourses6))
    # More specific validation (check prerequisite order)
    valid_order6 = True
    if is_valid6:
        pos = {course: i for i, course in enumerate(result6)}
        if pos[0] >= pos[1] or pos[2] >= pos[3]:
            valid_order6 = False
    else:
        valid_order6 = False
    print(f"Pass: {is_valid6 and valid_order6}")
    print("-" * 20)

if __name__ == "__main__":
    run_tests()

```

**4. Complexity Analysis**

*   **Time Complexity:** O(V + E)
    *   V is the number of courses (`numCourses`).
    *   E is the number of prerequisites (`len(prerequisites)`).
    *   Building the adjacency list and calculating in-degrees takes O(E) time.
    *   Initializing the queue takes O(V) time in the worst case (scanning all courses).
    *   The main `while` loop processes each course (node) and each prerequisite (edge) exactly once. Dequeuing/Enqueuing takes O(1) on average. So, this part takes O(V + E).
    *   Overall complexity is dominated by O(V + E).

*   **Space Complexity:** O(V + E)
    *   The adjacency list `adj` can store up to O(E) edges in total across all nodes. In the worst case, it might take O(V + E) space.
    *   The `in_degree` array takes O(V) space.
    *   The `queue` can store up to O(V) courses in the worst case.
    *   The `result` list stores O(V) courses.
    *   Overall space complexity is O(V + E).