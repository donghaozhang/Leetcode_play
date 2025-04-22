from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Find the k closest points to the origin using a max heap.
        
        Args:
            points: List of [x, y] coordinates
            k: Number of closest points to return
            
        Returns:
            List of k closest points to origin
        """
        # Create a max heap to store the k closest points
        # We store (-distance, x, y) to simulate a max heap using Python's min heap
        heap = []
        
        for x, y in points:
            # Calculate squared distance (no need for sqrt since we're just comparing)
            distance = -(x*x + y*y)
            
            if len(heap) < k:
                heapq.heappush(heap, (distance, x, y))
            else:
                # If current point is closer than the farthest in heap, replace it
                if distance > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (distance, x, y))
        
        # Extract the points from the heap
        return [[x, y] for (_, x, y) in heap]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    points = [[1, 3], [-2, 2]]
    k = 1
    print(solution.kClosest(points, k))  # [[-2, 2]]
    
    # Example 2
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(solution.kClosest(points, k))  # [[3, 3], [-2, 4]]
    
    # Test case: All points are the same distance
    points = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    k = 2
    print(solution.kClosest(points, k))  # Any 2 points
    
    # Test case: k equals length of points
    points = [[1, 1], [2, 2], [3, 3]]
    k = 3
    print(solution.kClosest(points, k))  # All points
    
    # Test case: Single point
    points = [[1, 1]]
    k = 1
    print(solution.kClosest(points, k))  # [[1, 1]] 