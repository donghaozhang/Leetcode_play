from typing import List
import copy # Needed for deep copying test cases

def reverseString(s: List[str]) -> None:
    """
    Reverses a list of characters in-place using the two-pointer method.

    Args:
        s: The list of characters to be reversed.

    Returns:
        None. The modification is done in-place.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Swap characters at left and right pointers
        s[left], s[right] = s[right], s[left]

        # Move pointers towards the center
        left += 1
        right -= 1

# --- Test Cases ---

def run_test_case(test_name, input_list, expected_output):
    """Helper function to run a single test case."""
    print(f"--- Running Test Case: {test_name} ---")
    # Create a deep copy to avoid modifying the original test input list
    # across different test runs if the function were buggy.
    list_copy = copy.deepcopy(input_list)
    print(f"Input:    {list_copy}")
    reverseString(list_copy) # Modify in-place
    print(f"Output:   {list_copy}")
    print(f"Expected: {expected_output}")
    assert list_copy == expected_output, f"Test Failed: Expected {expected_output}, got {list_copy}"
    print("Result:   Passed!")
    print("-" * (len(test_name) + 25))
    print() # Add a newline for better readability


# Test Case 1: Example 1 from LeetCode
input1 = ["h", "e", "l", "l", "o"]
expected1 = ["o", "l", "l", "e", "h"]
run_test_case("LeetCode Example 1", input1, expected1)

# Test Case 2: Example 2 from LeetCode
input2 = ["H", "a", "n", "n", "a", "h"]
expected2 = ["h", "a", "n", "n", "a", "H"]
run_test_case("LeetCode Example 2", input2, expected2)

# Test Case 3: Single Element
input3 = ["a"]
expected3 = ["a"]
run_test_case("Single Element", input3, expected3)

# Test Case 4: Two Elements
input4 = ["a", "b"]
expected4 = ["b", "a"]
run_test_case("Two Elements", input4, expected4)

# Test Case 5: Even Number of Elements (Longer)
input5 = ["1", "2", "3", "4", "5", "6"]
expected5 = ["6", "5", "4", "3", "2", "1"]
run_test_case("Even Length", input5, expected5)

# Test Case 6: Odd Number of Elements (Longer)
input6 = ["A", "B", "C", "D", "E"]
expected6 = ["E", "D", "C", "B", "A"]
run_test_case("Odd Length", input6, expected6)

# Test Case 7: List with Symbols
input7 = ["!", "@", "#", "$"]
expected7 = ["$", "#", "@", "!"]
run_test_case("Symbols", input7, expected7)

