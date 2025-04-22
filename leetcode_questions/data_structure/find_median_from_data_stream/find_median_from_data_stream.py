from heapq import heappush, heappop

class MedianFinder:
    """
    Find median from a stream of numbers using two heaps.
    """
    def __init__(self):
        """
        Initialize the data structure.
        - lo: max heap (using negative values)
        - hi: min heap
        """
        self.lo = []  # max heap
        self.hi = []  # min heap

    def addNum(self, num: int) -> None:
        """
        Add a number to the data structure.
        
        Args:
            num: Number to add
        """
        # Push to max heap (using negative value)
        heappush(self.lo, -num)
        
        # Push the largest from max heap to min heap
        heappush(self.hi, -heappop(self.lo))
        
        # Balance the heaps
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self) -> float:
        """
        Find the median of all numbers.
        
        Returns:
            Median value
        """
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (self.hi[0] - self.lo[0]) / 2

# Test cases
if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())  # 1.5
    medianFinder.addNum(3)
    print(medianFinder.findMedian())  # 2.0
    
    # Example 2: Single number
    print("\nExample 2:")
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    print(medianFinder.findMedian())  # 1.0
    
    # Example 3: Even number of elements
    print("\nExample 3:")
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    medianFinder.addNum(3)
    medianFinder.addNum(4)
    print(medianFinder.findMedian())  # 2.5
    
    # Example 4: Negative numbers
    print("\nExample 4:")
    medianFinder = MedianFinder()
    medianFinder.addNum(-1)
    medianFinder.addNum(-2)
    print(medianFinder.findMedian())  # -1.5 