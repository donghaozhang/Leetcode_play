# string_permutation_ii.md)
- 组合总和 / Combination Sum [LeetCode 39]

## Problem Description

## Combination Sum
<div class="description__24sA"><div class="css-1m3w5jl"><p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return <em>a list of all <strong>unique combinations</strong> of </em><code>candidates</code><em> where the chosen numbers sum to </em><code>target</code><em>.</em> You may return the combinations in <strong>any order</strong>.</p>

<p>The <strong>same</strong> number may be used among the candidates an <strong>unlimited number of times</strong>. Two combinations are unique if the <strong>frequency</strong> of at least one of the chosen numbers is different.</p>

<p>The test cases are generated such that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>2 &lt;= candidates[i] &lt;= 40</code></li>
	<li>All elements of <code>candidates</code> are <strong>distinct</strong>.</li>
	<li><code>1 &lt;= target &lt;= 40</code></li>
</ul>
</div></div>

## Solution

## Problem Explanation

The problem requires finding all unique combinations of numbers in a given array `candidates` that sum up to a target integer `target`. The numbers in `candidates` are distinct, and each number can be used any number of times in a combination.

Key constraints and edge cases:

- The `candidates` array contains distinct integers.
- The length of `candidates` is between 1 and 30.
- Each element in `candidates` is between 2 and 40.
- The `target` is between 1 and 40.
- The number of unique combinations that sum up to `target` is less than 150.
- The same number can be used multiple times in a combination.
- Two combinations are considered unique if the frequency of at least one of the chosen numbers is different.

Input: An array of distinct integers `candidates` and a target integer `target`.
Output: A list of all unique combinations of `candidates` that sum up to `target`.

Subtle requirements:

- The order of the combinations in the output does not matter.
- The order of numbers within a combination does not matter.

## Step-by-Step Approach

1. **Sort the Candidates Array**: First, sort the `candidates` array in ascending order. This is done to ensure that the combinations are generated in a systematic order, making it easier to avoid duplicates.

2. **Backtracking**: Use a backtracking approach to generate all combinations. Start with an empty combination and a remaining sum equal to `target`.

3. **Recursive Exploration**: For each number in `candidates`, check if adding it to the current combination would exceed the remaining sum. If not, add the number to the current combination and recursively explore further combinations with the updated remaining sum.

4. **Base Cases**:
   - If the remaining sum becomes 0, it means a valid combination has been found, so add it to the result list.
   - If the remaining sum becomes negative, stop exploring the current combination as it exceeds the target.

5. **Avoiding Duplicates**: Since the same number can be used multiple times and the `candidates` array is sorted, ensure that the backtracking explores all possible combinations without duplicates by considering each candidate starting from the current index.

6. **Result**: Collect all valid combinations in a result list and return it.

## Python Solution

```python
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
```

## Time and Space Complexity Analysis

- **Time Complexity**: The time complexity is O(N^(T/M) + N log N), where N is the length of `candidates`, T is the `target`, and M is the minimum value in `candidates`. The N log N comes from sorting the `candidates` array. The backtracking can potentially explore up to N^(T/M) combinations in the worst case.
- **Space Complexity**: The space complexity is O(T/M + N), where T/M represents the maximum depth of the recursion call stack (i.e., the maximum length of a combination), and N is for storing the result. In the worst case, the recursion call stack can go up to T/M levels deep.

## Test Cases

The provided Python solution includes test cases to verify its correctness:

1. `combinationSum([2,3,6,7], 7)` should return `[[2, 2, 3], [7]]`.
2. `combinationSum([2,3,5], 8)` should return `[[2, 2, 2, 2], [2, 3, 3], [3, 5]]`.
3. `combinationSum([2], 1)` should return `[]`.

These test cases cover different scenarios, including finding multiple combinations, handling cases where no combination sums up to the target, and ensuring that the same number can be used multiple times in a combination.