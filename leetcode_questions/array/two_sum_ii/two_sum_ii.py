from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Find two numbers in a sorted array that add up to the target.
    
    Args:
        numbers: A sorted array of integers (1-indexed in the problem)
        target: The target sum
        
    Returns:
        A list of two indices (1-indexed) whose elements sum to the target
    """
    # Two pointer approach - optimal for sorted arrays
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum < target:
            # Sum is too small, move left pointer to increase sum
            left += 1
        else:
            # Sum is too large, move right pointer to decrease sum
            right -= 1
    
    # Problem guarantees exactly one solution, but for completeness
    return []  # No solution found

# Test cases
if __name__ == "__main__":
    # Example 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Example 1: {two_sum(numbers1, target1)}")  # Expected: [1, 2]
    
    # Example 2
    numbers2 = [2, 3, 4]
    target2 = 6
    print(f"Example 2: {two_sum(numbers2, target2)}")  # Expected: [1, 3]
    
    # Example 3
    numbers3 = [-1, 0]
    target3 = -1
    print(f"Example 3: {two_sum(numbers3, target3)}")  # Expected: [1, 2]
    
    # Additional test case
    numbers4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target4 = 15
    print(f"Additional test: {two_sum(numbers4, target4)}")  # Expected: [5, 10] 