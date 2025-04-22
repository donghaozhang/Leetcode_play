# Generate Parentheses

## Problem

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples

**Example 1:**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**
```
Input: n = 1
Output: ["()"]
```

## Constraints

- 1 <= n <= 8

## Approach: Backtracking

The solution uses a backtracking approach to generate all valid combinations of parentheses. Here's how it works:

1. We start with an empty string and keep track of the number of left and right parentheses used.
2. At each step, we can add a left parenthesis if we haven't used all n left parentheses.
3. We can add a right parenthesis only if we have more left parentheses than right parentheses.
4. When the string length reaches 2n, we've found a valid combination.

### Key Components:

1. **Base Case**:
   - When the string length equals 2n, we've used all parentheses
   - Add the current string to the result list

2. **Recursive Cases**:
   - Add a left parenthesis if count < n
   - Add a right parenthesis if right count < left count

### Python Implementation:

```python
class Solution:
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(S: str = '', left: int = 0, right: int = 0) -> None:
            if len(S) == 2 * n:
                self.ans.append(S)
                return
            
            if left < n:
                backtrack(S + '(', left + 1, right)
            
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return self.ans
```

## Complexity Analysis

- **Time Complexity**: O(4^n/√n)
  - This is the nth Catalan number, which is the number of valid parentheses combinations
  - Each valid sequence has at most n steps during the backtracking procedure

- **Space Complexity**: O(4^n/√n)
  - Space needed to store all valid combinations
  - O(n) space for the recursion stack

## Why This Approach Works

1. **Validity Guarantee**: 
   - By only adding right parentheses when right < left, we ensure the sequence is always valid
   - This prevents invalid combinations like "())" from being generated

2. **Completeness**:
   - The approach generates all possible valid combinations
   - No valid combination is missed because we explore all possible paths

3. **Efficiency**:
   - We only explore valid paths, pruning invalid ones early
   - No duplicate combinations are generated

## Example Walkthrough

For n = 2, the process works like this:

1. Start with empty string ""
2. Add "(" (left = 1, right = 0)
3. Can add another "(" or ")"
   - If "(", get "(("
     - Must add ")" twice to get "(())"
   - If ")", get "()"
     - Can add "(" to get "()("
       - Must add ")" to get "()()"

This generates all valid combinations: ["(())", "()()"] 