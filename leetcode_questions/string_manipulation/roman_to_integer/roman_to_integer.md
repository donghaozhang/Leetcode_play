# Roman to Integer

## Problem Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X` + `II`. The number `27` is written as `XXVII`, which is `XX` + `V` + `II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## Examples

**Example 1:**
```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

**Example 2:**
```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 3:**
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## Constraints

- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## Approach

### English

The key insight to this problem is understanding how Roman numerals work, particularly the subtraction rule. In a Roman numeral, if a smaller value comes before a larger value, it represents subtraction; otherwise, it represents addition.

We can simplify the solution by reading the Roman numeral from right to left:

1. Initialize a variable `total` to 0 and a variable `prev_value` to 0 to keep track of the previous numeral's value.
2. Iterate through the string from right to left.
3. For each character:
   - Get its integer value from the mapping.
   - If the current value is greater than or equal to the previous value, add it to the total.
   - If the current value is less than the previous value (indicating subtraction), subtract it from the total.
   - Update the previous value to the current value for the next iteration.
4. Return the final total.

This approach correctly handles all cases, including the six subtraction instances (IV, IX, XL, XC, CD, CM).

### Chinese

解决这个问题的关键是理解罗马数字的工作原理，特别是减法规则。在罗马数字中，如果一个较小的值出现在较大的值之前，它表示减法；否则，它表示加法。

我们可以通过从右到左读取罗马数字来简化解决方案：

1. 初始化一个变量 `total` 为 0 和一个变量 `prev_value` 为 0，用于跟踪前一个数字的值。
2. 从右到左遍历字符串。
3. 对于每个字符：
   - 从映射中获取其整数值。
   - 如果当前值大于或等于前一个值，将其加到总数中。
   - 如果当前值小于前一个值（表示减法），从总数中减去它。
   - 将前一个值更新为当前值，为下一次迭代做准备。
4. 返回最终总数。

这种方法正确处理了所有情况，包括六种减法实例（IV、IX、XL、XC、CD、CM）。

## Complexity Analysis

### English

- **Time Complexity**: O(n), where n is the length of the input string. We traverse the string once.
- **Space Complexity**: O(1), as we use a fixed-size dictionary to store the mappings of Roman numerals to integers, and only a few variables to keep track of the calculation.

### Chinese

- **时间复杂度**：O(n)，其中 n 是输入字符串的长度。我们遍历字符串一次。
- **空间复杂度**：O(1)，因为我们使用固定大小的字典来存储罗马数字到整数的映射，并且只使用几个变量来跟踪计算。 