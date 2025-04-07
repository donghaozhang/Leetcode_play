def canJump(nums):
    """
    Determines whether it's possible to reach the last index of the given array by jumping from the first index.

    Args:
    nums (list): A list of integers where each element represents the maximum jump length at that position.

    Returns:
    bool: True if we can reach the last index, False otherwise.
    """
    max_reachable_index = 0
    for i, jump in enumerate(nums):
        # If the current index is beyond the max reachable index, return False
        if i > max_reachable_index:
            return False
        # Update the max reachable index
        max_reachable_index = max(max_reachable_index, i + jump)
    # If we've iterated through the entire array without returning False, we can reach the last index
    return True

# Test Cases
if __name__ == "__main__":
    # Example 1:
    nums = [2,3,1,1,4]
    print(canJump(nums))  # Expected Output: True
    
    # Example 2:
    nums = [3,2,1,0,4]
    print(canJump(nums))  # Expected Output: False
    
    # Additional Test Cases
    nums = [1]
    print(canJump(nums))  # Expected Output: True
    
    nums = [0]
    print(canJump(nums))  # Expected Output: True
    
    nums = [0,1]
    print(canJump(nums))  # Expected Output: False
    
    nums = [2,0,0]
    print(canJump(nums))  # Expected Output: True
