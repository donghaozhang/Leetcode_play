def canJump(nums):
    max_reach = 0
    n = len(nums)
    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            return True
    return max_reach >= n - 1

# Test cases
print(canJump([2,3,1,1,4]))  # Output: True
print(canJump([3,2,1,0,4]))  # Output: False
print(canJump([0]))          # Output: True (already at the last index)
print(canJump([1,0,1,0]))    # Output: False
print(canJump([2,0,0]))      # Output: True
