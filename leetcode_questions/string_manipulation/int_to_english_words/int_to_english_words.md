# Integer to English Words

## Problem Description

Convert a non-negative integer to its English words representation. Given an integer, return its English representation in words.

## Examples

**Example 1:**
```
Input: num = 123
Output: "One Hundred Twenty Three"
```

**Example 2:**
```
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```

**Example 3:**
```
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

## Constraints

- 0 <= num <= 2^31 - 1

## Approach

### English

This problem can be solved by breaking it down into smaller units. In English, numbers are grouped by thousands (thousand, million, billion, etc.), and each group can be expressed using ones, tens, and hundreds.

The algorithm follows these steps:

1. Create helper functions to convert single digits (`one`), teens (`two_less_20`), tens (`ten`), and groups of three digits (`three`).
2. Split the number into groups of thousands: billions, millions, thousands, and the remaining portion.
3. Convert each group using the helper functions and append the appropriate suffix (billion, million, thousand).
4. Handle special cases like zero and ensure proper spacing between words.

The key insight is to recursively break down the problem into smaller, more manageable chunks. By converting each group of three digits separately and then combining them with the appropriate suffix, we can handle numbers of arbitrary size within the given constraints.

### Chinese

这个问题可以通过将数字分解为更小的单位来解决。在英语中，数字按千位分组（千、百万、十亿等），每个组可以用个位、十位和百位来表示。

算法步骤如下：

1. 创建辅助函数来转换个位数字（`one`）、十几（`two_less_20`）、十位（`ten`）和三位数字组（`three`）。
2. 将数字分成千位组：十亿、百万、千和剩余部分。
3. 使用辅助函数转换每个组，并附加适当的后缀（billion、million、thousand）。
4. 处理特殊情况，如零，并确保单词之间的适当间距。

关键的见解是递归地将问题分解为更小、更易于管理的块。通过单独转换每三位数字，然后将它们与适当的后缀组合，我们可以在给定约束内处理任意大小的数字。

## Complexity Analysis

### English

- **Time Complexity**: O(1), because the algorithm processes a fixed number of digits (at most 10 digits for a 32-bit integer).
- **Space Complexity**: O(1), as the output size is bounded by a constant (the longest possible output string has a fixed maximum length).

### Chinese

- **时间复杂度**：O(1)，因为算法处理固定数量的数字（32位整数最多10位）。
- **空间复杂度**：O(1)，因为输出大小由常数限制（最长可能的输出字符串具有固定的最大长度）。 