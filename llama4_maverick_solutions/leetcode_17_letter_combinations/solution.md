# k_sum_ii.md)
- 电话号码的字母组合 / Letter Combinations [LeetCode 17]

## Problem Description

## 17. Letter Combinations of a Phone Number
### Medium

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#### Example 1:
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

#### Example 2:
```
Input: digits = ""
Output: []
```

#### Example 3:
```
Input: digits = "2"
Output: ["a","b","c"]
```

#### Constraints:
* `0 <= digits.length <= 4`
* `digits[i]` is a digit in the range `['2', '9']`.

## Solution

## Problem Explanation
The problem requires generating all possible letter combinations that a given string of digits (from 2 to 9 inclusive) could represent, based on a standard telephone keypad mapping. The input is a string of digits, and the output is a list of all possible letter combinations.

Key constraints and edge cases:
- The input string can be empty.
- The length of the input string is between 0 and 4.
- Each digit in the input string is between '2' and '9' (inclusive).
- The digit '1' is not mapped to any letters.

## Step-by-Step Approach
1. **Define the Mapping**: Create a dictionary that maps each digit to its corresponding letters based on the telephone keypad layout.
2. **Handle Edge Case**: If the input string is empty, return an empty list.
3. **Initialize Result**: Start with an empty list or a list containing an empty string to handle the base case for the recursion or iteration.
4. **Iterate Through Digits**: For each digit in the input string, iterate through the current combinations (or the initial empty string), and for each letter corresponding to the current digit, append it to the current combinations to form new combinations.
5. **Update Result**: After processing each digit, update the list of combinations to be used for the next digit.
6. **Return Final Combinations**: After processing all digits, return the final list of combinations.

## Python Solution
```python
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []

    # Mapping of digits to their corresponding letters
    phone_mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(combination, next_digits):
        # If there is no more digits to process, append the current combination to the output
        if len(next_digits) == 0:
            output.append(combination)
        # Otherwise, process the next available digit
        else:
            for letter in phone_mapping[next_digits[0]]:
                # Recursively call the function with the current combination and the remaining digits
                backtrack(combination + letter, next_digits[1:])

    output = []
    backtrack("", digits)
    return output

# Test Cases
print(letterCombinations("23"))  # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations(""))    # Expected: []
print(letterCombinations("2"))   # Expected: ["a","b","c"]
```

## Time and Space Complexity Analysis
- **Time Complexity**: O(4^n) where n is the length of the input string. This is because in the worst case (when the input string consists entirely of '7' or '9'), each digit can map to 4 letters, leading to 4^n possible combinations.
- **Space Complexity**: O(n) for the recursion stack in the worst case, where n is the length of the input string. The space required to store the output is O(4^n) as there can be up to 4^n combinations.

## Test Cases
The provided Python solution includes test cases to verify its correctness:
- `letterCombinations("23")` should return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
- `letterCombinations("")` should return `[]`.
- `letterCombinations("2")` should return `["a","b","c"]`.

These test cases cover various scenarios, including an empty input string, a single digit, and a string of two digits, ensuring the solution behaves as expected under different conditions.