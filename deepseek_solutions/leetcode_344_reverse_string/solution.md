# closest_bst_value.md)

## 字符串处理 (String Manipulation)
- 翻转字符串 / Reverse String [LeetCode 344]

## Problem Description

**344. Reverse String**

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

**Example 1:**
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:**
```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

**Constraints:**
- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

## Solution

### Explanation of the Problem
The problem requires us to reverse a string that is given as an array of characters in-place. This means we should not use any additional space (O(1) space complexity) and must modify the original array directly. 

For example, the input `["h","e","l","l","o"]` should be reversed to `["o","l","l","e","h"]`.

### Approach
1. **Two-pointer technique**: We can use two pointers, one starting at the beginning of the array (left pointer) and the other at the end (right pointer).
2. **Swap characters**: Swap the characters at the left and right pointers.
3. **Move pointers inward**: Increment the left pointer and decrement the right pointer after each swap.
4. **Termination condition**: Continue swapping until the left pointer is no longer less than the right pointer.

This approach ensures that we only perform O(n/2) swaps (where n is the length of the string), resulting in O(n) time complexity and O(1) space complexity.

### Solution Code
```python
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test cases
test1 = ["h","e","l","l","o"]
reverseString(test1)
print(test1)  # Output: ["o","l","l","e","h"]

test2 = ["H","a","n","n","a","h"]
reverseString(test2)
print(test2)  # Output: ["h","a","n","n","a","H"]

test3 = ["a"]
reverseString(test3)
print(test3)  # Output: ["a"]

test4 = ["a", "b"]
reverseString(test4)
print(test4)  # Output: ["b", "a"]
```

### Explanation
1. **Initialization**: Start with `left` at index 0 and `right` at the last index of the array.
2. **Swapping**: Swap the elements at `left` and `right` indices. For example, in the first test case, "h" (index 0) and "o" (index 4) are swapped first.
3. **Pointer Adjustment**: Move `left` forward and `right` backward. Continue this process until `left` is no longer less than `right`.
4. **Termination**: The loop stops when all necessary swaps are done, leaving the array reversed in-place.

### Time and Space Complexity
- **Time Complexity**: O(n), where n is the number of characters in the string. Each character is swapped once (or twice if counted individually, but it's linear).
- **Space Complexity**: O(1), as no additional space is used apart from a few variables for pointers.

### Test Cases
1. **Test Case 1**: `["h","e","l","l","o"]` becomes `["o","l","l","e","h"]`.
2. **Test Case 2**: `["H","a","n","n","a","h"]` becomes `["h","a","n","n","a","H"]`.
3. **Test Case 3**: `["a"]` remains `["a"]` as it's a single character.
4. **Test Case 4**: `["a", "b"]` becomes `["b", "a"]`.

These test cases cover various scenarios including even-length, odd-length, single-character, and two-character strings to ensure the solution works correctly.