class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert an integer to a Roman numeral.
        
        Args:
            num: An integer between 1 and 3999
            
        Returns:
            A string representing the Roman numeral version of the input
        """
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


def test_int_to_roman():
    """Test the intToRoman function with various examples"""
    solution = Solution()
    
    # Test case 1: Complex number with multiple symbols
    assert solution.intToRoman(3749) == "MMMDCCXLIX", f"Expected 'MMMDCCXLIX', got '{solution.intToRoman(3749)}'"
    
    # Test case 2: Number with basic symbols
    assert solution.intToRoman(58) == "LVIII", f"Expected 'LVIII', got '{solution.intToRoman(58)}'"
    
    # Test case 3: Number with subtractive forms
    assert solution.intToRoman(1994) == "MCMXCIV", f"Expected 'MCMXCIV', got '{solution.intToRoman(1994)}'"
    
    # Additional test cases
    assert solution.intToRoman(1) == "I", f"Expected 'I', got '{solution.intToRoman(1)}'"
    assert solution.intToRoman(4) == "IV", f"Expected 'IV', got '{solution.intToRoman(4)}'"
    assert solution.intToRoman(9) == "IX", f"Expected 'IX', got '{solution.intToRoman(9)}'"
    assert solution.intToRoman(49) == "XLIX", f"Expected 'XLIX', got '{solution.intToRoman(49)}'"
    assert solution.intToRoman(999) == "CMXCIX", f"Expected 'CMXCIX', got '{solution.intToRoman(999)}'"
    assert solution.intToRoman(3999) == "MMMCMXCIX", f"Expected 'MMMCMXCIX', got '{solution.intToRoman(3999)}'"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_int_to_roman() 