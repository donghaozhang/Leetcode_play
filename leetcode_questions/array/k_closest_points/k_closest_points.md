# K Closest Points to Origin

## Problem

Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)² + (y1 - y2)²).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

## Examples

**Example 1:**
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

**Example 2:**
```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

## Constraints

- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4

## Approach: Max Heap

The solution uses a max heap to maintain the k closest points. The key insight is that we can keep track of the k smallest distances without sorting the entire array.

### Key Components:

1. **Heap Initialization**:
   ```python
   heap = []  # Will store (-distance, x, y) to simulate max heap
   ```

2. **Distance Calculation**:
   ```python
   distance = -(x*x + y*y)  # Negative for max heap, squared for efficiency
   ```

3. **Heap Management**:
   ```python
   if len(heap) < k:
       heapq.heappush(heap, (distance, x, y))
   else:
       if distance > heap[0][0]:
           heapq.heappop(heap)
           heapq.heappush(heap, (distance, x, y))
   ```

4. **Result Extraction**:
   ```python
   return [[x, y] for (_, x, y) in heap]
   ```

## Complexity Analysis

- **Time Complexity**: O(n log k)
  - We process each point once: O(n)
  - Each heap operation takes O(log k) time
  - Overall: O(n log k)

- **Space Complexity**: O(k)
  - We maintain a heap of size k
  - No additional space is used

## Why This Approach Works

1. **Efficiency**:
   - Better than sorting (O(n log n)) when k << n
   - Only maintains k elements in memory
   - Avoids calculating square roots by using squared distances

2. **Correctness**:
   - Always maintains the k closest points
   - Handles all edge cases (k = 1, k = n, etc.)
   - Works for any point distribution

3. **Optimizations**:
   - Uses squared distances to avoid sqrt calculations
   - Simulates max heap using negative values
   - Only updates heap when necessary

## Example Walkthrough

For points = [[1,3],[-2,2]] and k = 1:

1. **Process (1,3)**:
   - Distance = -(1² + 3²) = -10
   - Heap: [(-10, 1, 3)]

2. **Process (-2,2)**:
   - Distance = -((-2)² + 2²) = -8
   - -8 > -10, so replace
   - Heap: [(-8, -2, 2)]

3. **Result**:
   - Extract points: [[-2, 2]]

The solution efficiently finds the k closest points without sorting the entire array. 