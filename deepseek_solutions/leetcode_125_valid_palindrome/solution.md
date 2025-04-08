# reverse_string.md)
- 判断回文串 / Valid Palindrome [LeetCode 125]

## Problem Description

**125. Valid Palindrome**  

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.  

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.  

**Example 1:**  
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```  

**Example 2:**  
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```  

**Example 3:**  
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```  

**Constraints:**  
- `1 <= s.length <= 2 * 10^5`  
- `s` consists only of printable ASCII characters.

## Solution

### Problem Explanation
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). In this problem, we need to determine if a given string is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters (i.e., characters that are not letters or numbers).

### Approach
1. **Preprocess the String**: 
   - Convert all characters in the string to lowercase to handle case insensitivity.
   - Remove all non-alphanumeric characters from the string. This can be done by iterating through each character and checking if it is a letter or a digit.
   
2. **Check for Palindrome**:
   - Use two pointers, one starting at the beginning (left) and one at the end (right) of the processed string.
   - Compare the characters at these pointers. If they are not the same, the string is not a palindrome.
   - Move the left pointer forward and the right pointer backward until they meet or cross each other. If all corresponding characters match, the string is a palindrome.

### Solution Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

# Test cases
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(solution.isPalindrome("race a car"))  # False
print(solution.isPalindrome(" "))  # True
print(solution.isPalindrome("0P"))  # False
print(solution.isPalindrome("ab_a"))  # True
```

### Explanation
1. **Initialization**: Two pointers, `left` and `right`, are initialized to the start and end of the string, respectively.
2. **Skipping Non-Alphanumeric Characters**: The `left` pointer moves forward until it encounters an alphanumeric character, and the `right` pointer moves backward until it encounters an alphanumeric character.
3. **Comparison**: The characters at the `left` and `right` pointers are compared (case-insensitively). If they don't match, the function returns `False` immediately.
4. **Termination Condition**: The loop continues until the pointers meet or cross each other. If all corresponding characters match, the function returns `True`.

### Time and Space Complexity
- **Time Complexity**: O(n), where n is the length of the string. Each character is processed at most once by the two pointers.
- **Space Complexity**: O(1), since we are using constant extra space for the pointers and no additional data structures.

### Test Cases
1. **"A man, a plan, a canal: Panama"**: Processed string is "amanaplanacanalpanama", which is a palindrome.
2. **"race a car"**: Processed string is "raceacar", which is not a palindrome.
3. **" "**: Processed string is "", which is a palindrome.
4. **"0P"**: Processed string is "0p", where '0' != 'p', so not a palindrome.
5. **"ab_a"**: Processed string is "aba", which is a palindrome.

These test cases cover various scenarios including strings with spaces, punctuation, mixed cases, and edge cases like an empty string.