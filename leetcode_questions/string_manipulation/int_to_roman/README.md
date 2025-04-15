# Integer to Roman [LeetCode 12]

## Problem Overview
Convert an integer to a Roman numeral.

### Roman Numeral Rules
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

With special subtractive forms: IV (4), IX (9), XL (40), XC (90), CD (400), and CM (900).

## Files
- [int_to_roman.py](int_to_roman.py) - Implementation of the solution
- [int_to_roman.md](int_to_roman.md) - Detailed explanation of the problem and solution

## Quick Example
```
Input: 1994
Output: "MCMXCIV"
Explanation:
M = 1000, CM = 900, XC = 90, IV = 4
```

## Solution Approach
We use a greedy approach to build the Roman numeral from largest to smallest values:

1. Map each significant value to its Roman numeral representation
2. Iterate through values in descending order, appending symbols as needed
3. Continue until the input number is reduced to zero

## Time and Space Complexity
- Time Complexity: O(1)
- Space Complexity: O(1)

## LeetCode Link
[Integer to Roman - LeetCode Problem 12](https://leetcode.com/problems/integer-to-roman/) 