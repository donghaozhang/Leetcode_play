# k_sum_ii.md)
- 电话号码的字母组合 / Letter Combinations [LeetCode 17]

## Problem Description

```markdown
## 17. Letter Combinations of a Phone Number

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![Phone Keypad Mapping](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

**Example 1:**

**Input:** digits = "23"
**Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Example 2:**

**Input:** digits = ""
**Output:** []

**Example 3:**

**Input:** digits = "2"
**Output:** ["a","b","c"]

**Constraints:**

*   `0 <= digits.length <= 4`
*   `digits[i]` is a digit in the range `['2', '9']`.
```

## Solution

Okay, let's break down the "Letter Combinations of a Phone Number" problem (LeetCode 17).

## 1. Explanation of the Problem

The problem asks us to generate all possible letter combinations that can be formed from a given string of digits (from '2' to '9'). Each digit corresponds to a set of letters, similar to the layout on a standard telephone keypad. For example, '2' maps to "abc", '3' maps to "def", and so on.

If the input is "23", we need to find all combinations by taking one letter from the mapping of '2' and one letter from the mapping of '3'. The combinations would be:
*   'a' (from '2') + 'd' (from '3') = "ad"
*   'a' (from '2') + 'e' (from '3') = "ae"
*   'a' (from '2') + 'f' (from '3') = "af"
*   'b' (from '2') + 'd' (from '3') = "bd"
*   ... and so on, resulting in ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

The order of the combinations in the output list doesn't matter. If the input string is empty, the output should be an empty list.

## 2. Step-by-Step Approach

This problem can be solved effectively using **backtracking** (a form of recursion). The core idea is to build the combinations character by character.

1.  **Mapping:** Create a mapping (like a dictionary or hash map) to store the correspondence between digits ('2' through '9') and their respective letters.
    ```
    mapping = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }
    ```
2.  **Base Case:** If the input `digits` string is empty, return an empty list immediately.
3.  **Recursive Function (Backtracking):** Define a helper function, let's call it `backtrack`, which will recursively build the combinations. This function will take parameters like:
    *   `index`: The current index of the digit in the `digits` string we are considering.
    *   `current_combination`: The string built so far.
4.  **Recursive Logic:**
    *   **Base Case for Recursion:** If the `index` reaches the end of the `digits` string (i.e., `index == len(digits)`), it means we have formed a complete combination. Add the `current_combination` to our result list and return.
    *   **Recursive Step:**
        *   Get the current digit: `digit = digits[index]`.
        *   Get the corresponding letters for this digit from the `mapping`: `letters = mapping[digit]`.
        *   Iterate through each `letter` in `letters`:
            *   Make a recursive call to `backtrack` for the *next* index (`index + 1`) and append the current `letter` to the `current_combination` (e.g., `backtrack(index + 1, current_combination + letter)`).
5.  **Initialization:** Start the process by calling the `backtrack` function with initial values: `backtrack(0, "")`.
6.  **Result:** The function will populate a list with all the valid combinations. Return this list.

## 3. Python Solution

```python
from typing import List

class Solution:
    """
    Solves the Letter Combinations of a Phone Number problem using backtracking.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generates all possible letter combinations for a given digit string.

        Args:
            digits: A string containing digits from '2'-'9'.

        Returns:
            A list of all possible letter combinations.
        """
        # Handle the edge case of an empty input string
        if not digits:
            return []

        # Mapping from digits to letters
        mapping = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        results = [] # To store the final combinations

        def backtrack(index: int, current_combination: str):
            """
            Recursive helper function to build combinations.

            Args:
                index: The current index in the digits string being processed.
                current_combination: The combination string built so far.
            """
            # Base case: If we have processed all digits
            if index == len(digits):
                results.append(current_combination)
                return # Stop recursion for this path

            # Get the current digit and its corresponding letters
            current_digit = digits[index]
            letters = mapping[current_digit]

            # Iterate through each possible letter for the current digit
            for letter in letters:
                # Recursively call for the next digit, appending the current letter
                backtrack(index + 1, current_combination + letter)

        # Start the backtracking process from the first digit (index 0)
        # with an empty initial combination
        backtrack(0, "")

        return results

# --- Test Cases ---

solver = Solution()

# Test Case 1: Example 1
digits1 = "23"
expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
output1 = solver.letterCombinations(digits1)
print(f"Input: digits = \"{digits1}\"")
print(f"Output: {output1}")
# Sort both lists to compare them regardless of order
print(f"Expected: {sorted(expected1)}")
print(f"Result matches expected: {sorted(output1) == sorted(expected1)}")
print("-" * 20)

# Test Case 2: Empty Input
digits2 = ""
expected2 = []
output2 = solver.letterCombinations(digits2)
print(f"Input: digits = \"{digits2}\"")
print(f"Output: {output2}")
print(f"Expected: {expected2}")
print(f"Result matches expected: {output2 == expected2}")
print("-" * 20)

# Test Case 3: Single Digit
digits3 = "2"
expected3 = ["a", "b", "c"]
output3 = solver.letterCombinations(digits3)
print(f"Input: digits = \"{digits3}\"")
print(f"Output: {output3}")
print(f"Expected: {sorted(expected3)}")
print(f"Result matches expected: {sorted(output3) == sorted(expected3)}")
print("-" * 20)

# Test Case 4: Longer Input with digits having 4 letters
digits4 = "79"
# 7: pqrs, 9: wxyz
expected4 = ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]
output4 = solver.letterCombinations(digits4)
print(f"Input: digits = \"{digits4}\"")
print(f"Output: {output4}")
print(f"Expected: {sorted(expected4)}")
print(f"Result matches expected: {sorted(output4) == sorted(expected4)}")
print("-" * 20)

# Test Case 5: Input with length 4
digits5 = "2345"
output5 = solver.letterCombinations(digits5)
print(f"Input: digits = \"{digits5}\"")
# Output will be large (3*3*3*3 = 81 combinations), just print the count
print(f"Output count: {len(output5)}")
print(f"Expected count: 81")
print(f"Result count matches expected: {len(output5) == 81}")
print("-" * 20)

```

### Complexity Analysis:

*   **Time Complexity:** `O(N * 4^N)`
    *   Let `N` be the length of the input `digits` string.
    *   Let `M` be the maximum number of letters a digit can map to (which is 4, for '7' and '9').
    *   The backtracking algorithm explores a tree structure. The maximum depth of the recursion is `N`.
    *   At each level `i` (corresponding to the `i`-th digit), we branch out based on the number of letters for that digit (at most `M`).
    *   The total number of leaf nodes in the recursion tree (representing complete combinations) is at most `M^N`. In the worst case (digits like '7' or '9'), this is `4^N`.
    *   Generating each combination involves building a string of length `N`. In Python, string concatenation `current_combination + letter` creates a new string, which takes `O(N)` time at the deepest levels.
    *   Therefore, the total time complexity is roughly the number of combinations multiplied by the time to create each combination: `O(N * M^N)`, which simplifies to `O(N * 4^N)` in the worst case.

*   **Space Complexity:** `O(N * 4^N)`
    *   **Recursion Stack:** The maximum depth of the recursion call stack is `N`. Each stack frame stores some local variables and the `current_combination` string being built. The space used by the stack is `O(N)`.
    *   **Output Storage:** The primary space usage comes from storing the `results`. There can be up to `M^N` (or `4^N`) combinations, and each combination has a length of `N`. Storing all these combinations requires `O(N * M^N)` or `O(N * 4^N)` space.
    *   Thus, the overall space complexity is dominated by the output storage: `O(N * 4^N)`. If the space required for the output is not considered, the space complexity is `O(N)` due to the recursion depth.

## 4. Test Cases

Here are the test cases covered in the Python code above:

1.  `digits = "23"` -> `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]` (Standard case)
2.  `digits = ""` -> `[]` (Empty input)
3.  `digits = "2"` -> `["a", "b", "c"]` (Single digit input)
4.  `digits = "79"` -> `["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]` (Includes digits with 4 letters)
5.  `digits = "2345"` -> (Checks the count for a longer input, expected count is 3 * 3 * 3 * 3 = 81)