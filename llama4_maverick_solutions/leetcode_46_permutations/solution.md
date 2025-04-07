# bst_iterator.md)
- 全排列 / Permutations [LeetCode 46]

## Problem Description

## 46. Permutations
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

### Example 1:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3:
```
Input: nums = [1]
Output: [[1]]
```

### Constraints:
* `1 <= nums.length <= 6`
* `-10 <= nums[i] <= 10`
* All the integers of `nums` are **unique**.

## Solution

## Problem Explanation
The problem requires generating all possible permutations of a given array of distinct integers. A permutation is an arrangement of objects in a specific order. For example, given the array `[1, 2, 3]`, the possible permutations are `[1, 2, 3]`, `[1, 3, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[3, 1, 2]`, and `[3, 2, 1]`.

## Step-by-Step Approach
To solve this problem, we can use a backtracking approach. Here's a step-by-step breakdown:

1. **Understand the Problem**: We need to generate all permutations of the input array `nums`.
2. **Choose an Approach**: Backtracking is a suitable approach for this problem because it allows us to explore all possible configurations (permutations in this case) by making choices and then undoing them when they don't lead to a valid solution.
3. **Design the Backtracking Algorithm**:
   - Start with an empty permutation and the full list of numbers.
   - At each step, choose a number from the remaining numbers that hasn't been used yet in the current permutation.
   - Add this number to the current permutation and recursively generate all permutations with this number fixed in the current position.
   - Once all numbers have been used (i.e., the permutation is complete), add it to the result list.
   - Backtrack by removing the last added number from the permutation and trying the next available number.
4. **Implement the Algorithm**: Use a recursive function to implement the backtracking algorithm. The function should take the current permutation and the remaining numbers as parameters.

## Python Solution
```python
def permute(nums):
    """
    Generates all permutations of the given list of distinct integers.

    Args:
    nums (list): A list of distinct integers.

    Returns:
    list: A list of lists, where each sublist is a permutation of the input list.
    """
    def backtrack(start, end):
        # If we have filled the permutation, add it to the result
        if start == end:
            result.append(nums[:])  # Use nums[:] to create a copy of nums
        for i in range(start, end):
            # Swap the current number with the start number
            nums[start], nums[i] = nums[i], nums[start]
            # Recur for the remaining numbers
            backtrack(start + 1, end)
            # Backtrack by swapping back
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0, len(nums))
    return result

# Test cases
print(permute([1, 2, 3]))  # Expected: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
print(permute([0, 1]))    # Expected: [[0, 1], [1, 0]]
print(permute([1]))       # Expected: [[1]]
```

## Time and Space Complexity Analysis
- **Time Complexity**: The time complexity is O(N!), where N is the number of elements in the input array. This is because there are N! permutations for N distinct numbers, and we generate all of them.
- **Space Complexity**: The space complexity is O(N!), as we need to store all N! permutations in the result list. Additionally, the recursion stack can go up to a depth of N, so the space complexity also includes O(N) for the recursion stack. However, O(N!) dominates for N > 1.

## Test Cases
The provided Python solution includes test cases to verify its correctness. These test cases cover different scenarios, including arrays of length 1, 2, and 3, to ensure the function generates all permutations correctly. Additional test cases can be added to further validate the function's behavior with different inputs.