class Solution:
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0, len(nums))
        return result

# Test cases
solution = Solution()
print(solution.permute([1,2,3]))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(solution.permute([0,1]))     # Output: [[0,1],[1,0]]
print(solution.permute([1]))       # Output: [[1]]
