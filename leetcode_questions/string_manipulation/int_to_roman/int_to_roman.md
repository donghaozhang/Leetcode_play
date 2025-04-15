# Integer to Roman

## Problem Description
Convert an integer to a Roman numeral.

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

1. If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

2. If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

3. Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

## Examples

### Example 1:
```
Input: num = 3749
Output: "MMMDCCXLIX"
Explanation:
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
```

### Example 2:
```
Input: num = 58
Output: "LVIII"
Explanation:
50 = L
 8 = VIII
```

### Example 3:
```
Input: num = 1994
Output: "MCMXCIV"
Explanation:
1000 = M
 900 = CM
  90 = XC
   4 = IV
```

## Constraints
- 1 <= num <= 3999

## Solution Approach
We can solve this problem using a greedy approach with a mapping of Roman numerals to integer values.

The algorithm is as follows:
1. Create a dictionary mapping key integer values to their Roman numeral representation, including the special subtractive forms.
2. Sort the keys of the dictionary in descending order.
3. Iterate through the dictionary, for each value:
   - Calculate how many times the current Roman numeral can be used (using integer division).
   - Append the Roman numeral to the result string that many times.
   - Subtract the value from the input number.
4. Continue until the input number becomes 0.

### Time Complexity
O(1) - The algorithm iterates through a fixed number of Roman numeral symbols.

### Space Complexity
O(1) - We only use a fixed-size dictionary for the mappings.

## Code Implementation
```python
def intToRoman(self, num: int) -> str:
    dict = {}
    dict[1000] = 'M'
    dict[900]  = 'CM'
    dict[500]  = 'D'
    dict[400]  = 'CD'
    dict[100]  = 'C'
    dict[90]   = 'XC'
    dict[50]   = 'L'
    dict[40]   = 'XL'
    dict[10]   = 'X'
    dict[9]    = 'IX'
    dict[5]    = 'V'
    dict[4]    = 'IV'
    dict[1]    = 'I'
    out = ''
    for key, item in dict.items():
        loc_num = num // key
        if loc_num > 0:
            num = num - loc_num * key
            out = out + item * loc_num
    return out
```

## Related Problems
- [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) - The reverse operation of this problem, converting a Roman numeral to an integer. 