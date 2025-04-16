from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:
            # If the character is an closing bracket
            if char in mapping:
                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else "#"

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

# Test cases
def test_valid_parentheses():
    solution = Solution()
    
    # Test case 1
    s1 = "()"
    print(f"Input: {s1}")
    print(f"Output: {solution.isValid(s1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    s2 = "()[]{}"
    print(f"Input: {s2}")
    print(f"Output: {solution.isValid(s2)}")
    print(f"Expected: True")
    print()
    
    # Test case 3
    s3 = "(]"
    print(f"Input: {s3}")
    print(f"Output: {solution.isValid(s3)}")
    print(f"Expected: False")
    print()
    
    # Test case 4
    s4 = "([])"
    print(f"Input: {s4}")
    print(f"Output: {solution.isValid(s4)}")
    print(f"Expected: True")
    print()
    
    # Test case 5 - Extra unmatched opening bracket
    s5 = "([)]"
    print(f"Input: {s5}")
    print(f"Output: {solution.isValid(s5)}")
    print(f"Expected: False")

if __name__ == "__main__":
    test_valid_parentheses() 