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
