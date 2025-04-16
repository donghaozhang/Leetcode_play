from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1: 
            return 0 
        
        left = [0 for i in range(n)]  # denotes max before this element including this
        right = [0 for i in range(n)]  # denotes max after this element including this
        
        left[0], right[-1] = height[0], height[-1] 
        
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
            
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
            
        total_water = 0
        for i in range(n):
            # water collected by this bar is the min of the max heights to its left and right, minus its own height
            water_at_this_position = min(left[i], right[i]) - height[i]
            total_water += water_at_this_position
            
        return total_water

# Test cases
def test_trap():
    solution = Solution()
    
    # Test case 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Input: {height1}")
    print(f"Output: {solution.trap(height1)}")
    print(f"Expected: 6")
    print()
    
    # Test case 2
    height2 = [4, 2, 0, 3, 2, 5]
    print(f"Input: {height2}")
    print(f"Output: {solution.trap(height2)}")
    print(f"Expected: 9")
    print()
    
    # Test case 3 - No water can be trapped
    height3 = [1, 2, 3, 4, 5]
    print(f"Input: {height3}")
    print(f"Output: {solution.trap(height3)}")
    print(f"Expected: 0")
    print()
    
    # Test case 4 - Empty array
    height4 = []
    print(f"Input: {height4}")
    print(f"Output: {solution.trap(height4)}")
    print(f"Expected: 0")
    print()
    
    # Test case 5 - Single element
    height5 = [5]
    print(f"Input: {height5}")
    print(f"Output: {solution.trap(height5)}")
    print(f"Expected: 0")

if __name__ == "__main__":
    test_trap() 