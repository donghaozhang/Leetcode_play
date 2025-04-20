from typing import List

def max_area(height: List[int]) -> int:
    """
    Find the container with the most water from a list of heights.
    
    Args:
        height: List of heights representing vertical lines
        
    Returns:
        Maximum amount of water a container can store
    """
    left, right = 0, len(height) - 1
    max_area_value = 0
    
    while left < right:
        # Calculate width between two lines
        width = right - left
        
        # Calculate height (limited by the shorter line)
        l_height = height[left]
        r_height = height[right]
        
        # Calculate area based on the shorter line
        if r_height > l_height:
            area = width * l_height
            left += 1  # Move left pointer inward
        else:
            area = width * r_height
            right -= 1  # Move right pointer inward
            
        # Update maximum area
        max_area_value = max(max_area_value, area)
    
    return max_area_value

# Test cases
if __name__ == "__main__":
    # Example 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(height1))  # Expected output: 49
    
    # Example 2
    height2 = [1, 1]
    print(max_area(height2))  # Expected output: 1
    
    # Additional test case
    height3 = [4, 3, 2, 1, 4]
    print(max_area(height3))  # Expected output: 16 