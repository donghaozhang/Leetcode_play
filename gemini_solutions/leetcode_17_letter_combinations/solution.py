from typing import List

class Solution:
    """
    Solves the Letter Combinations of a Phone Number problem using backtracking.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generates all possible letter combinations for a given digit string.

        Args:
            digits: A string containing digits from '2'-'9'.

        Returns:
            A list of all possible letter combinations.
        """
        # Handle the edge case of an empty input string
        if not digits:
            return []

        # Mapping from digits to letters
        mapping = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        results = [] # To store the final combinations

        def backtrack(index: int, current_combination: str):
            """
            Recursive helper function to build combinations.

            Args:
                index: The current index in the digits string being processed.
                current_combination: The combination string built so far.
            """
            # Base case: If we have processed all digits
            if index == len(digits):
                results.append(current_combination)
                return # Stop recursion for this path

            # Get the current digit and its corresponding letters
            current_digit = digits[index]
            letters = mapping[current_digit]

            # Iterate through each possible letter for the current digit
            for letter in letters:
                # Recursively call for the next digit, appending the current letter
                backtrack(index + 1, current_combination + letter)

        # Start the backtracking process from the first digit (index 0)
        # with an empty initial combination
        backtrack(0, "")

        return results

# --- Test Cases ---

solver = Solution()

# Test Case 1: Example 1
digits1 = "23"
expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
output1 = solver.letterCombinations(digits1)
print(f"Input: digits = \"{digits1}\"")
print(f"Output: {output1}")
# Sort both lists to compare them regardless of order
print(f"Expected: {sorted(expected1)}")
print(f"Result matches expected: {sorted(output1) == sorted(expected1)}")
print("-" * 20)

# Test Case 2: Empty Input
digits2 = ""
expected2 = []
output2 = solver.letterCombinations(digits2)
print(f"Input: digits = \"{digits2}\"")
print(f"Output: {output2}")
print(f"Expected: {expected2}")
print(f"Result matches expected: {output2 == expected2}")
print("-" * 20)

# Test Case 3: Single Digit
digits3 = "2"
expected3 = ["a", "b", "c"]
output3 = solver.letterCombinations(digits3)
print(f"Input: digits = \"{digits3}\"")
print(f"Output: {output3}")
print(f"Expected: {sorted(expected3)}")
print(f"Result matches expected: {sorted(output3) == sorted(expected3)}")
print("-" * 20)

# Test Case 4: Longer Input with digits having 4 letters
digits4 = "79"
# 7: pqrs, 9: wxyz
expected4 = ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]
output4 = solver.letterCombinations(digits4)
print(f"Input: digits = \"{digits4}\"")
print(f"Output: {output4}")
print(f"Expected: {sorted(expected4)}")
print(f"Result matches expected: {sorted(output4) == sorted(expected4)}")
print("-" * 20)

# Test Case 5: Input with length 4
digits5 = "2345"
output5 = solver.letterCombinations(digits5)
print(f"Input: digits = \"{digits5}\"")
# Output will be large (3*3*3*3 = 81 combinations), just print the count
print(f"Output count: {len(output5)}")
print(f"Expected count: 81")
print(f"Result count matches expected: {len(output5) == 81}")
print("-" * 20)

