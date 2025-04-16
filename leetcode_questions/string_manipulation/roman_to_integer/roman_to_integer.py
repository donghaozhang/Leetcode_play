from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping Roman numerals to their integer values
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through the string from right to left
        for char in reversed(s):
            current_value = roman_dict[char]
            
            # If current value is greater than or equal to the previous value, add it
            # Otherwise, subtract it (handles cases like IV, IX, XL, etc.)
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
                
            prev_value = current_value
            
        return total

# Test cases
def test_roman_to_integer():
    solution = Solution()
    
    # Test case 1
    s1 = "III"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {solution.romanToInt(s1)}")
    print(f"Expected: 3")
    print(f"Explanation: III = 3.")
    print()
    
    # Test case 2
    s2 = "LVIII"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {solution.romanToInt(s2)}")
    print(f"Expected: 58")
    print(f"Explanation: L = 50, V= 5, III = 3.")
    print()
    
    # Test case 3
    s3 = "MCMXCIV"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {solution.romanToInt(s3)}")
    print(f"Expected: 1994")
    print(f"Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.")
    print()
    
    # Test case 4 - Single character
    s4 = "M"
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {solution.romanToInt(s4)}")
    print(f"Expected: 1000")
    print()
    
    # Test case 5 - All subtraction cases
    s5 = "IV" + "IX" + "XL" + "XC" + "CD" + "CM"
    print(f"Input: s = \"{s5}\"")
    print(f"Output: {solution.romanToInt(s5)}")
    print(f"Expected: 1443")
    print(f"Explanation: IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900.")

if __name__ == "__main__":
    test_roman_to_integer() 