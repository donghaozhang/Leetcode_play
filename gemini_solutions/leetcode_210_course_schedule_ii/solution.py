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

