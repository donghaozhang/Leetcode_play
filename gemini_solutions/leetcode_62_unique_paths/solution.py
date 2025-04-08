import math
import time

# Solution 1: Dynamic Programming (Space Optimized)
def uniquePaths_dp(m: int, n: int) -> int:
    """
    Calculates the number of unique paths using space-optimized DP.

    Args:
        m: The number of rows in the grid.
        n: The number of columns in the grid.

    Returns:
        The total number of unique paths.
    """
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

    # Use the smaller dimension for the dp array for better space optimization
    if m < n:
        m, n = n, m # Ensure n is the smaller dimension

    # dp_row represents the number of paths to reach cells in the current row
    # Initialize with 1s (representing the first row of the conceptual grid)
    dp_row = [1] * n

    # Iterate through the rows (starting from the second row, index 1)
    for i in range(1, m):
        # Iterate through the columns (starting from the second column, index 1)
        for j in range(1, n):
            # dp_row[j] currently holds the value from the previous row (paths from above)
            # dp_row[j-1] holds the updated value for the current row (paths from left)
            dp_row[j] = dp_row[j] + dp_row[j-1]

    # The last element contains the number of paths to the bottom-right cell
    return dp_row[n - 1]

# Solution 2: Combinatorial Approach
def uniquePaths_combinatorial(m: int, n: int) -> int:
    """
    Calculates the number of unique paths using combinatorics.

    Args:
        m: The number of rows in the grid.
        n: The number of columns in the grid.

    Returns:
        The total number of unique paths.
    """
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

    # Total number of moves needed
    total_moves = m + n - 2
    # Number of 'down' moves needed (or 'right' moves, choose the smaller for efficiency)
    k = min(m - 1, n - 1)

    # Calculate combinations: C(total_moves, k)
    # math.comb(n, k) calculates n! / (k! * (n-k)!)
    return math.comb(total_moves, k)

# --- Testing ---
def run_tests(solution_func):
    test_cases = [
        ((3, 7), 28),
        ((3, 2), 3),
        ((7, 3), 28),
        ((2, 3), 3),
        ((1, 1), 1),
        ((1, 10), 1),
        ((10, 1), 1),
        ((2, 2), 2),
        ((19, 13), 86493225), # Larger test case
        ((51, 9), 169884720), # Another larger test case
    ]

    print(f"--- Testing {solution_func.__name__} ---")
    all_passed = True
    for i, (inputs, expected) in enumerate(test_cases):
        m, n = inputs
        start_time = time.time()
        result = solution_func(m, n)
        end_time = time.time()
        duration = (end_time - start_time) * 1000 # milliseconds

        if result == expected:
            print(f"Test Case {i+1}: PASSED ({duration:.4f} ms)")
        else:
            print(f"Test Case {i+1}: FAILED")
            print(f"  Input: m={m}, n={n}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
            all_passed = False
            print("-" * 20)

    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")
    print("-" * 30)


# Run tests for both solutions
run_tests(uniquePaths_dp)
run_tests(uniquePaths_combinatorial)

# Example Usage
print("\nExample Usage:")
m1, n1 = 3, 7
print(f"Input: m={m1}, n={n1}")
print(f"DP Solution: {uniquePaths_dp(m1, n1)}")
print(f"Combinatorial Solution: {uniquePaths_combinatorial(m1, n1)}")

m2, n2 = 3, 2
print(f"\nInput: m={m2}, n={n2}")
print(f"DP Solution: {uniquePaths_dp(m2, n2)}")
print(f"Combinatorial Solution: {uniquePaths_combinatorial(m2, n2)}")
