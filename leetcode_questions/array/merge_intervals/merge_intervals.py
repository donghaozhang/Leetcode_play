from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        list_len = len(intervals)
        if list_len == 1 or list_len == 0:
            return intervals
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged

# Test cases
def test_merge_intervals():
    solution = Solution()
    
    # Test case 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print("Test Case 1 Input:", intervals1)
    print("Test Case 1 Output:", solution.merge(intervals1))
    print("Expected Output: [[1,6],[8,10],[15,18]]")
    print()
    
    # Test case 2
    intervals2 = [[1,4],[4,5]]
    print("Test Case 2 Input:", intervals2)
    print("Test Case 2 Output:", solution.merge(intervals2))
    print("Expected Output: [[1,5]]")
    print()
    
    # Test case 3: Empty array
    intervals3 = []
    print("Test Case 3 Input:", intervals3)
    print("Test Case 3 Output:", solution.merge(intervals3))
    print("Expected Output: []")
    print()
    
    # Test case 4: Single interval
    intervals4 = [[1,5]]
    print("Test Case 4 Input:", intervals4)
    print("Test Case 4 Output:", solution.merge(intervals4))
    print("Expected Output: [[1,5]]")
    print()
    
    # Test case 5: No overlapping intervals
    intervals5 = [[1,2],[3,4],[5,6]]
    print("Test Case 5 Input:", intervals5)
    print("Test Case 5 Output:", solution.merge(intervals5))
    print("Expected Output: [[1,2],[3,4],[5,6]]")
    print()
    
    # Test case 6: All overlapping intervals
    intervals6 = [[1,10],[2,9],[3,8],[4,7]]
    print("Test Case 6 Input:", intervals6)
    print("Test Case 6 Output:", solution.merge(intervals6))
    print("Expected Output: [[1,10]]")

if __name__ == "__main__":
    test_merge_intervals() 