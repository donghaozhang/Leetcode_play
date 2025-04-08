import heapq # Although the DP approach is better, let's keep the import for context if needed

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Finds the nth ugly number using a dynamic programming approach.

        An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

        Args:
            n: The position of the desired ugly number (1-based index).

        Returns:
            The nth ugly number.
        """
        if n <= 0:
            return 0 # Or raise an error based on constraints/expectations
        if n == 1:
            return 1

        # Initialize DP array to store ugly numbers
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1

        # Initialize pointers for factors 2, 3, and 5
        p2 = 0
        p3 = 0
        p5 = 0

        for i in range(1, n):
            # Calculate the next potential ugly numbers
            next_ugly_2 = ugly_numbers[p2] * 2
            next_ugly_3 = ugly_numbers[p3] * 3
            next_ugly_5 = ugly_numbers[p5] * 5

            # Find the minimum of the candidates
            next_ugly = min(next_ugly_2, next_ugly_3, next_ugly_5)
            ugly_numbers[i] = next_ugly

            # Advance the pointers for the factors that generated the minimum
            # Use separate 'if' statements, not 'elif', because multiple
            # factors might produce the same minimum (e.g., 6 = 2*3 = 3*2)
            if next_ugly == next_ugly_2:
                p2 += 1
            if next_ugly == next_ugly_3:
                p3 += 1
            if next_ugly == next_ugly_5:
                p5 += 1

        # The nth ugly number is the last element in the array
        return ugly_numbers[n - 1]

# --- Test Cases ---

solver = Solution()

# Example 1
n1 = 10
expected1 = 12
result1 = solver.nthUglyNumber(n1)
print(f"Input: n = {n1}")
print(f"Output: {result1}")
print(f"Expected: {expected1}")
print(f"Pass: {result1 == expected1}\n")

# Example 2
n2 = 1
expected2 = 1
result2 = solver.nthUglyNumber(n2)
print(f"Input: n = {n2}")
print(f"Output: {result2}")
print(f"Expected: {expected2}")
print(f"Pass: {result2 == expected2}\n")

# Additional Test Cases
n3 = 7
expected3 = 8 # Sequence: 1, 2, 3, 4, 5, 6, 8
result3 = solver.nthUglyNumber(n3)
print(f"Input: n = {n3}")
print(f"Output: {result3}")
print(f"Expected: {expected3}")
print(f"Pass: {result3 == expected3}\n")

n4 = 11
expected4 = 15 # Sequence: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15
result4 = solver.nthUglyNumber(n4)
print(f"Input: n = {n4}")
print(f"Output: {result4}")
print(f"Expected: {expected4}")
print(f"Pass: {result4 == expected4}\n")

n5 = 1690 # Max constraint
expected5 = 2123366400 # Known result for n=1690
result5 = solver.nthUglyNumber(n5)
print(f"Input: n = {n5}")
print(f"Output: {result5}")
print(f"Expected: {expected5}")
print(f"Pass: {result5 == expected5}\n")

