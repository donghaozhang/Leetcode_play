from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] = char_count[char] + 1
            else:
                char_count[char] = 1
                
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
                
        return -1

# Test cases
def test_first_unique_character():
    solution = Solution()
    
    # Test case 1
    s1 = "leetcode"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {solution.firstUniqChar(s1)}")
    print(f"Expected: 0")
    print(f"Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.")
    print()
    
    # Test case 2
    s2 = "loveleetcode"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {solution.firstUniqChar(s2)}")
    print(f"Expected: 2")
    print()
    
    # Test case 3
    s3 = "aabb"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {solution.firstUniqChar(s3)}")
    print(f"Expected: -1")
    print()
    
    # Test case 4 - Empty string
    s4 = ""
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {solution.firstUniqChar(s4)}")
    print(f"Expected: -1")
    print()
    
    # Test case 5 - All characters appear once
    s5 = "abcdef"
    print(f"Input: s = \"{s5}\"")
    print(f"Output: {solution.firstUniqChar(s5)}")
    print(f"Expected: 0")

if __name__ == "__main__":
    test_first_unique_character() 