# Find Median from Data Stream

## Problem

Design a data structure that supports the following two operations:
1. `addNum(num)`: Add a number to the data structure
2. `findMedian()`: Return the median of all numbers added so far

The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values.

## Examples

**Example 1:**
```
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output:
[null, null, null, 1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

## Constraints

- -10^5 <= num <= 10^5
- At least one element before calling findMedian
- At most 5 * 10^4 calls to addNum and findMedian

## Approach: Two Heaps

The solution uses two heaps to maintain the median efficiently:

1. **Max Heap (lo)**: Stores the smaller half of numbers
2. **Min Heap (hi)**: Stores the larger half of numbers

Key properties:
- Size difference between heaps is at most 1
- All numbers in max heap <= all numbers in min heap
- Median is either:
  - The top of max heap (if sizes are unequal)
  - The average of both heap tops (if sizes are equal)

### Key Components:

1. **Heap Management**:
   ```python
   def addNum(self, num: int) -> None:
       # Push to max heap (using negative value)
       heappush(self.lo, -num)
       
       # Push the largest from max heap to min heap
       heappush(self.hi, -heappop(self.lo))
       
       # Balance the heaps
       if len(self.lo) < len(self.hi):
           heappush(self.lo, -heappop(self.hi))
   ```

2. **Median Calculation**:
   ```python
   def findMedian(self) -> float:
       if len(self.lo) > len(self.hi):
           return -self.lo[0]
       return (self.hi[0] - self.lo[0]) / 2
   ```

## Complexity Analysis

- **Time Complexity**:
  - addNum: O(log n) for heap operations
  - findMedian: O(1) for accessing heap tops
  - Overall: O(log n) per number added

- **Space Complexity**:
  - O(n) to store all numbers in the heaps
  - Each number is stored exactly once

## Why This Approach Works

1. **Efficiency**:
   - O(log n) insertion time
   - O(1) median lookup
   - No need to sort the entire list

2. **Correctness**:
   - Maintains the two halves of the sorted list
   - Preserves the median property
   - Handles both odd and even cases

3. **Memory Optimization**:
   - Only stores necessary information
   - No redundant data
   - Efficient heap operations

## Follow-up Solutions

1. **If all numbers are in [0, 100]**:
   - Use counting sort
   - Maintain counts for each number
   - O(1) insertion, O(100) median lookup
   - Space: O(100)

2. **If 99% of numbers are in [0, 100]**:
   - Use counting sort for [0, 100]
   - Use two heaps for outliers
   - Most operations O(1)
   - Rare cases O(log n)

## Example Walkthrough

For the input sequence [1, 2, 3]:

1. **Add 1**:
   - lo: [-1]
   - hi: []
   - Median: 1

2. **Add 2**:
   - lo: [-1]
   - hi: [2]
   - Median: (1 + 2) / 2 = 1.5

3. **Add 3**:
   - lo: [-2, -1]
   - hi: [3]
   - Median: 2 