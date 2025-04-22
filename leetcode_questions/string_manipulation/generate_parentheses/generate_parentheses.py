from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses.
        
        Args:
            n: Number of pairs of parentheses
            
        Returns:
            List of all valid combinations
        """
        def backtrack(S: str = '', left: int = 0, right: int = 0) -> None:
            """
            Backtracking helper function to generate valid parentheses combinations.
            
            Args:
                S: Current string being built
                left: Number of left parentheses used
                right: Number of right parentheses used
            """
            # Base case: we've used all parentheses
            if len(S) == 2 * n:
                self.ans.append(S)
                return
            
            # Add left parenthesis if we haven't used all of them
            if left < n:
                backtrack(S + '(', left + 1, right)
            
            # Add right parenthesis if we have more left than right
            if right < left:
                backtrack(S + ')', left, right + 1)

        # Start the backtracking process
        backtrack()
        return self.ans

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    n1 = 3
    print(f"Example 1: {solution.generateParenthesis(n1)}")  # Expected: ["((()))","(()())","(())()","()(())","()()()"]
    
    # Example 2
    solution = Solution()  # Reset for new test
    n2 = 1
    print(f"Example 2: {solution.generateParenthesis(n2)}")  # Expected: ["()"]
    
    # Additional test case
    solution = Solution()  # Reset for new test
    n3 = 2
    print(f"Additional test: {solution.generateParenthesis(n3)}")  # Expected: ["(())","()()"] 