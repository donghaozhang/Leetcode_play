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
