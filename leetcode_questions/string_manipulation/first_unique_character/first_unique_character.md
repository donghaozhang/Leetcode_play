# First Unique Character in a String

## Problem Description

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

## Examples

**Example 1:**
```
Input: s = "leetcode"
Output: 0
Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.
```

**Example 2:**
```
Input: s = "loveleetcode"
Output: 2
```

**Example 3:**
```
Input: s = "aabb"
Output: -1
```

## Constraints

- 1 <= s.length <= 10^5
- `s` consists of only lowercase English letters.

## Approach

### English

This problem can be solved in two passes through the string:

1. First Pass: Count the frequency of each character in the string using a hash map.
   - Iterate through each character of the string.
   - For each character, update its count in the hash map.

2. Second Pass: Find the first character with a count of 1.
   - Iterate through the string again, maintaining the original order.
   - For each character, check its count in the hash map.
   - Return the index of the first character with a count of 1.
   - If no such character exists, return -1.

The time complexity is O(n) where n is the length of the string, as we need to traverse the string twice. The space complexity is O(k) where k is the size of the character set (in this case, k is at most 26 for lowercase English letters).

### Chinese

这个问题可以通过两次遍历字符串来解决：

1. 第一次遍历：使用哈希映射计算字符串中每个字符的频率。
   - 遍历字符串的每个字符。
   - 对于每个字符，在哈希映射中更新其计数。

2. 第二次遍历：找到计数为1的第一个字符。
   - 再次遍历字符串，保持原始顺序。
   - 对于每个字符，检查其在哈希映射中的计数。
   - 返回计数为1的第一个字符的索引。
   - 如果不存在这样的字符，则返回-1。

时间复杂度为O(n)，其中n是字符串的长度，因为我们需要遍历字符串两次。空间复杂度为O(k)，其中k是字符集的大小（在这种情况下，k最多为26个小写英文字母）。

## Complexity Analysis

### English

- **Time Complexity**: O(n), where n is the length of the string. We need to traverse the string twice.
- **Space Complexity**: O(k), where k is the size of the character set. In this problem, since we're dealing with lowercase English letters, k is at most 26, so the space complexity is O(1) as it's a constant.

### Chinese

- **时间复杂度**：O(n)，其中n是字符串的长度。我们需要遍历字符串两次。
- **空间复杂度**：O(k)，其中k是字符集的大小。在这个问题中，由于我们处理的是小写英文字母，k最多为26，所以空间复杂度为O(1)，因为它是一个常数。 