def combinationSum(candidates, target):
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        for i in range(start, len(candidates)):
            num = candidates[i]
            if num > remaining:
                continue
            path.append(num)
            backtrack(i, path, remaining - num)
            path.pop()
    
    result = []
    candidates.sort()
    backtrack(0, [], target)
    return result

# Test cases
def test_combinationSum():
    # Example 1
    candidates1 = [2,3,6,7]
    target1 = 7
    assert combinationSum(candidates1, target1) == [[2,2,3],[7]]
    
    # Example 2
    candidates2 = [2,3,5]
    target2 = 8
    assert combinationSum(candidates2, target2) == [[2,2,2,2],[2,3,3],[3,5]]
    
    # Example 3
    candidates3 = [2]
    target3 = 1
    assert combinationSum(candidates3, target3) == []
    
    # Additional test case
    candidates4 = [3,5,8]
    target4 = 11
    assert combinationSum(candidates4, target4) == [[3,3,5],[3,8]]
    
    print("All test cases pass")

test_combinationSum()
