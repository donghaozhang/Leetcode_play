class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of a 32-bit signed integer.
        
        Args:
            x: The integer to reverse
            
        Returns:
            The reversed integer, or 0 if the reversed number overflows
        """
        sign = [1, -1][x < 0]  # Determine the sign of the input
        rev, x = 0, abs(x)     # Work with positive numbers
        
        while x:
            x, mod = divmod(x, 10)  # Get the last digit
            rev = rev * 10 + mod    # Build the reversed number
            
            # Check for 32-bit integer overflow
            if rev > 2**31 - 1:
                return 0
                
        return sign * rev

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    x = 123
    print(solution.reverse(x))  # 321
    
    # Example 2
    x = -123
    print(solution.reverse(x))  # -321
    
    # Example 3
    x = 120
    print(solution.reverse(x))  # 21
    
    # Test case: Overflow
    x = 1534236469
    print(solution.reverse(x))  # 0
    
    # Test case: Single digit
    x = 5
    print(solution.reverse(x))  # 5
    
    # Test case: Zero
    x = 0
    print(solution.reverse(x))  # 0 