from typing import List
import collections

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generate all possible letter combinations that a phone number could represent.
        
        Args:
            digits: String containing digits from 2-9
            
        Returns:
            List of all possible letter combinations
        """
        if not digits:
            return []
            
        # Create phone number to letters mapping
        phone = collections.defaultdict(str)
        phone['2'] = 'abc'
        phone['3'] = 'def'
        phone['4'] = 'ghi'
        phone['5'] = 'jkl'
        phone['6'] = 'mno'
        phone['7'] = 'pqrs'
        phone['8'] = 'tuv'
        phone['9'] = 'wxyz'
        
        def combine_digits(current: List[str], next_letters: str) -> List[str]:
            """
            Combine current combinations with next set of letters.
            
            Args:
                current: List of current combinations
                next_letters: String of letters to combine with
                
            Returns:
                List of new combinations
            """
            if not current:
                return list(next_letters)
                
            output = []
            for combination in current:
                for letter in next_letters:
                    output.append(combination + letter)
            return output
        
        # Build combinations digit by digit
        combinations = []
        for digit in digits:
            combinations = combine_digits(combinations, phone[digit])
            
        return combinations

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    digits1 = "23"
    print(f"Example 1: {solution.letterCombinations(digits1)}")  # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    # Example 2
    digits2 = ""
    print(f"Example 2: {solution.letterCombinations(digits2)}")  # Expected: []
    
    # Example 3
    digits3 = "2"
    print(f"Example 3: {solution.letterCombinations(digits3)}")  # Expected: ["a","b","c"]
    
    # Additional test case
    digits4 = "234"
    print(f"Additional test: {solution.letterCombinations(digits4)}")  # Expected: combinations of 3 letters 