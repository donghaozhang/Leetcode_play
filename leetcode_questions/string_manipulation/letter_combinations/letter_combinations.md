# Letter Combinations of a Phone Number

## Problem

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## Examples

**Example 1:**
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2:**
```
Input: digits = ""
Output: []
```

**Example 3:**
```
Input: digits = "2"
Output: ["a","b","c"]
```

## Constraints

- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

## Approach: Iterative Combination

The solution uses an iterative approach to build all possible combinations. Here's how it works:

1. **Phone Number Mapping**: Create a mapping of digits to their corresponding letters
2. **Combination Building**: 
   - Start with an empty list of combinations
   - For each digit in the input:
     - If it's the first digit, initialize combinations with its letters
     - Otherwise, combine existing combinations with new letters
3. **Edge Cases**: Handle empty input string appropriately

### Key Components:

1. **Phone Number Mapping**:
   ```python
   phone = {
       '2': 'abc',
       '3': 'def',
       '4': 'ghi',
       '5': 'jkl',
       '6': 'mno',
       '7': 'pqrs',
       '8': 'tuv',
       '9': 'wxyz'
   }
   ```

2. **Combination Function**:
   - Takes current combinations and next set of letters
   - Returns new combinations by appending each letter to each existing combination
   - Handles the first digit case separately

### Python Implementation:

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def combine_digits(current: List[str], next_letters: str) -> List[str]:
            if not current:
                return list(next_letters)
                
            output = []
            for combination in current:
                for letter in next_letters:
                    output.append(combination + letter)
            return output
        
        combinations = []
        for digit in digits:
            combinations = combine_digits(combinations, phone[digit])
            
        return combinations
```

## Complexity Analysis

- **Time Complexity**: O(4^N)
  - N is the length of the input digits
  - In the worst case, each digit has 4 letters (7 and 9)
  - We need to generate all possible combinations

- **Space Complexity**: O(4^N)
  - Space needed to store all combinations
  - Each combination takes O(N) space
  - Total space is O(N * 4^N)

## Why This Approach Works

1. **Systematic Combination**:
   - We build combinations one digit at a time
   - Each new digit's letters are combined with all existing combinations
   - This ensures we generate all possible combinations

2. **Efficiency**:
   - We only generate valid combinations
   - No duplicate combinations are created
   - The iterative approach avoids recursion overhead

3. **Memory Management**:
   - We reuse the combinations list
   - No unnecessary copies are made
   - Memory usage is optimized

## Example Walkthrough

For digits = "23":

1. First digit '2':
   - Combinations = ['a', 'b', 'c']

2. Second digit '3':
   - Combine each existing combination with 'd', 'e', 'f':
   - 'a' + 'd' = 'ad'
   - 'a' + 'e' = 'ae'
   - 'a' + 'f' = 'af'
   - 'b' + 'd' = 'bd'
   - 'b' + 'e' = 'be'
   - 'b' + 'f' = 'bf'
   - 'c' + 'd' = 'cd'
   - 'c' + 'e' = 'ce'
   - 'c' + 'f' = 'cf'

Final result: ["ad","ae","af","bd","be","bf","cd","ce","cf"] 