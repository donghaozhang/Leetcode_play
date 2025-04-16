# Valid Parentheses

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Example 4:**
```
Input: s = "([])"
Output: true
```

## Constraints

- 1 <= s.length <= 10^4
- `s` consists of parentheses only `'()[]{}'`.

## Approach

### English

This problem can be efficiently solved using a stack data structure. The approach works as follows:

1. Initialize an empty stack to keep track of opening brackets.
2. Create a hash map that maps each closing bracket to its corresponding opening bracket.
3. Scan the input string character by character:
   - If the current character is an opening bracket (`(`, `{`, `[`), push it onto the stack.
   - If the current character is a closing bracket (`)`, `}`, `]`), check if the stack is empty. If it is, return false because there's no matching opening bracket.
   - If the stack is not empty, pop the top element from the stack and check if it matches the corresponding opening bracket for the current closing bracket. If not, return false.
4. After processing all characters, if the stack is empty, return true (all brackets were properly matched and closed). Otherwise, return false (there are unmatched opening brackets).

The time complexity is O(n) where n is the length of the string, as we process each character once. The space complexity is also O(n) in the worst case, where all characters are opening brackets.

### Chinese

这个问题可以使用栈数据结构高效解决。解决方法如下：

1. 初始化一个空栈来跟踪开括号。
2. 创建一个哈希映射，将每个闭括号映射到其相应的开括号。
3. 逐字符扫描输入字符串：
   - 如果当前字符是开括号（`(`，`{`，`[`），将其推入栈中。
   - 如果当前字符是闭括号（`)`，`}`，`]`），检查栈是否为空。如果为空，返回 false，因为没有匹配的开括号。
   - 如果栈不为空，从栈中弹出顶部元素，并检查它是否与当前闭括号的相应开括号匹配。如果不匹配，返回 false。
4. 处理完所有字符后，如果栈为空，返回 true（所有括号都正确匹配和闭合）。否则，返回 false（有未匹配的开括号）。

时间复杂度为 O(n)，其中 n 是字符串的长度，因为我们每个字符只处理一次。空间复杂度在最坏情况下也是 O(n)，即所有字符都是开括号的情况。

## Complexity Analysis

### English

- **Time Complexity**: O(n), where n is the length of the input string. We scan each character in the string exactly once.
- **Space Complexity**: O(n) in the worst case. If the string contains only opening brackets, all of them will be pushed onto the stack.

### Chinese

- **时间复杂度**：O(n)，其中 n 是输入字符串的长度。我们对字符串中的每个字符只扫描一次。
- **空间复杂度**：最坏情况下为 O(n)。如果字符串只包含开括号，所有开括号都会被推入栈中。 