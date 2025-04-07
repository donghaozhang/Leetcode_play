def combinationSum(candidates, target):
    """
    Returns a list of all unique combinations of candidates that sum up to target.
    
    :param candidates: A list of distinct integers.
    :type candidates: List[int]
    :param target: The target sum.
    :type target: int
    :return: A list of lists, where each sublist is a combination of candidates that sum up to target.
    :rtype: List[List[int]]
    """
    def backtrack(remain, comb, start):
        """
        Helper function to perform backtracking.
        
        :param remain: The remaining sum to reach the target.
        :type remain: int
        :param comb: The current combination of numbers.
        :type comb: List[int]
        :param start: The starting index for the next number to consider.
        :type start: int
        """
        if remain == 0:
            result.append(list(comb))
            return
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i)
            comb.pop()
    
    candidates.sort()
    result = []
    backtrack(target, [], 0)
    return result

# Test cases
print(combinationSum([2,3,6,7], 7))  # Expected: [[2, 2, 3], [7]]
print(combinationSum([2,3,5], 8))    # Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(combinationSum([2], 1))        # Expected: []
