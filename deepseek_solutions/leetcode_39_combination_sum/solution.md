# string_permutation_ii.md)
- 组合总和 / Combination Sum [LeetCode 39]

## Problem Description

# 39. Combination Sum

## Description

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

## Examples

### Example 1:
**Input:** candidates = [2,3,6,7], target = 7  
**Output:** [[2,2,3],[7]]  
**Explanation:**  
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.  
7 is a candidate, and 7 = 7.  
These are the only two combinations.

### Example 2:
**Input:** candidates = [2,3,5], target = 8  
**Output:** [[2,2,2,2],[2,3,3],[3,5]]  

### Example 3:
**Input:** candidates = [2], target = 1  
**Output:** []  

## Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are distinct.
- `1 <= target <= 40`

## Solution

### Problem Explanation
The problem requires us to find all unique combinations of numbers from a given list `candidates` such that the sum of the numbers in each combination equals the `target`. Each number in `candidates` can be used an unlimited number of times in a combination. The solution should return these combinations in any order, and each combination should be unique in terms of the frequency of the numbers used.

### Approach
1. **Backtracking**: This is a classic backtracking problem where we explore all possible combinations by recursively adding candidates to the current combination and checking if the sum meets the target.
2. **Sorting**: First, sort the `candidates` array to facilitate early termination in the backtracking process. If at any point the current candidate makes the sum exceed the target, we can skip the rest of the candidates since they are larger.
3. **Recursive Exploration**: For each candidate, we start from the current position (to avoid duplicate combinations in different orders) and keep adding the same candidate until the sum exceeds the target. Then we backtrack and try the next candidate.
4. **Base Cases**: 
   - If the sum equals the target, add the current combination to the result.
   - If the sum exceeds the target, return and backtrack.

### Solution Code
```python
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
```

### Explanation
1. **Backtracking Function**: The `backtrack` function is defined to explore combinations. It starts from a given index to avoid reusing the same elements in different orders, which would lead to duplicate combinations.
2. **Path Management**: The current combination (`path`) is built by adding each candidate, and the function is called recursively with the updated remaining target. If the remaining target becomes zero, the current path is added to the result.
3. **Early Termination**: By sorting the candidates and checking if the current candidate exceeds the remaining target, we avoid unnecessary recursive calls, thus optimizing the solution.
4. **Test Cases**: The provided test cases verify the correctness of the solution, including edge cases like an empty result when the target is smaller than all candidates.

### Complexity Analysis
- **Time Complexity**: The time complexity is O(N^(T/M + 1)), where N is the number of candidates, T is the target, and M is the minimal value among the candidates. This is because in the worst case, the algorithm explores all possible combinations (with repetitions) up to the target value.
- **Space Complexity**: The space complexity is O(T/M) for the recursion stack, where T is the target and M is the smallest candidate. This is due to the depth of the recursion tree, which can go up to T/M in the worst case (using the smallest element repeatedly). The space for storing results is not counted towards the space complexity as it is part of the output.