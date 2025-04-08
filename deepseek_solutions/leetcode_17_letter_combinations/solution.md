# k_sum_ii.md)
- 电话号码的字母组合 / Letter Combinations [LeetCode 17]

## Problem Description

# 17. Letter Combinations of a Phone Number

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![Telephone Keypad](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

### Example 1:
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Example 2:
```
Input: digits = ""
Output: []
```

### Example 3:
```
Input: digits = "2"
Output: ["a","b","c"]
```

### Constraints:
- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## Solution

### Explanation of the Problem
The problem requires us to generate all possible letter combinations that a given string of digits (from 2 to 9) could represent based on the traditional telephone keypad mapping. Each digit maps to a set of letters (e.g., 2 maps to "abc", 3 maps to "def", etc.). The task is to return all possible combinations of these letters corresponding to the input digits.

### Approach
1. **Mapping Digits to Letters**: First, we create a dictionary that maps each digit to its corresponding letters.
2. **Handle Edge Cases**: If the input string is empty, return an empty list.
3. **Backtracking/DFS**: We use a backtracking approach to explore all possible combinations:
   - Start with an empty combination.
   - For each digit in the input string, append each possible letter to the current combinations.
   - Recursively build combinations until all digits are processed.
4. **Base Case**: When the current combination's length equals the input digits' length, add it to the result list.

### Solution Code
```python
def letterCombinations(digits):
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, current_combination):
        if index == len(digits):
            result.append(''.join(current_combination))
            return
        
        current_digit = digits[index]
        for letter in digit_to_letters[current_digit]:
            current_combination.append(letter)
            backtrack(index + 1, current_combination)
            current_combination.pop()
    
    backtrack(0, [])
    return result
```

### Time and Space Complexity Analysis
- **Time Complexity**: O(3^N * 4^M), where N is the number of digits that map to 3 letters (2, 3, 4, 5, 6, 8) and M is the number of digits that map to 4 letters (7, 9). This is because for each digit, we branch out into 3 or 4 possible letters.
- **Space Complexity**: O(N + M) for the recursion stack, where N is the length of the digits string. The space for the result is O(3^N * 4^M) to store all combinations, but this is part of the output and not auxiliary space.

### Test Cases
```python
# Test Case 1
digits = "23"
print(letterCombinations(digits))
# Expected Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Test Case 2
digits = ""
print(letterCombinations(digits))
# Expected Output: []

# Test Case 3
digits = "2"
print(letterCombinations(digits))
# Expected Output: ["a","b","c"]

# Test Case 4
digits = "9"
print(letterCombinations(digits))
# Expected Output: ["w","x","y","z"]

# Test Case 5
digits = "234"
print(letterCombinations(digits))
# Expected Output: ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
#                   "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
#                   "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
```

These test cases cover various scenarios including empty input, single digit, multiple digits, and digits that map to both 3 and 4 letters. The solution should handle all these cases correctly.