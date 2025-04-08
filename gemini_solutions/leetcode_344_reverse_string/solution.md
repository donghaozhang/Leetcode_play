# closest_bst_value.md)

## 字符串处理 (String Manipulation)
- 翻转字符串 / Reverse String [LeetCode 344]

## Problem Description

```markdown
### 344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with O(1) extra memory.

**Example 1:**

**Input:** s = ["h","e","l","l","o"]
**Output:** ["o","l","l","e","h"]

**Example 2:**

**Input:** s = ["H","a","n","n","a","h"]
**Output:** ["h","a","n","n","a","H"]

**Constraints:**

*   `1 <= s.length <= 10^5`
*   `s[i]` is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).
```

## Solution

Okay, let's tackle the LeetCode 344 "Reverse String" problem.

## 1. Problem Explanation

The goal is to reverse the order of characters within a given list (or array) of characters. The key constraints are:
1.  **In-place modification:** You cannot create a new list to store the reversed string. You must modify the original list directly.
2.  **O(1) extra space:** You can only use a constant amount of extra memory, regardless of the input string's length. This usually means using a few variables for indices or temporary storage during swaps, but not creating data structures whose size depends on the input size.

For example, if the input is `["h", "e", "l", "l", "o"]`, the list should be changed to `["o", "l", "l", "e", "h"]` after the function runs.

## 2. Step-by-Step Approach (Two-Pointer Method)

The most common and efficient way to reverse an array or list in-place with O(1) extra space is using the **two-pointer** technique:

1.  **Initialize Pointers:**
    *   Set a `left` pointer to the start of the list (index 0).
    *   Set a `right` pointer to the end of the list (index `len(s) - 1`).
2.  **Swap and Move:**
    *   While the `left` pointer is strictly less than the `right` pointer:
        *   Swap the characters at the `left` and `right` indices.
        *   Move the `left` pointer one step to the right (`left += 1`).
        *   Move the `right` pointer one step to the left (`right -= 1`).
3.  **Termination:**
    *   The loop stops when `left` becomes equal to or greater than `right`.
    *   If the list has an odd number of elements, the middle element will be pointed to by both `left` and `right` when they meet, and it doesn't need to be swapped.
    *   If the list has an even number of elements, the pointers will cross (`left` will become greater than `right`), and all elements will have been swapped correctly.

**Example Walkthrough (`s = ["h","e","l","l","o"]`)**

*   Initial: `left = 0`, `right = 4`, `s = ["h", "e", "l", "l", "o"]`
*   Iteration 1:
    *   `left < right` (0 < 4) is true.
    *   Swap `s[0]` ('h') and `s[4]` ('o'). `s` becomes `["o", "e", "l", "l", "h"]`.
    *   Increment `left` to 1.
    *   Decrement `right` to 3.
*   Iteration 2:
    *   `left < right` (1 < 3) is true.
    *   Swap `s[1]` ('e') and `s[3]` ('l'). `s` becomes `["o", "l", "l", "e", "h"]`.
    *   Increment `left` to 2.
    *   Decrement `right` to 2.
*   Iteration 3:
    *   `left < right` (2 < 2) is false. The loop terminates.
*   Final Result: `s = ["o", "l", "l", "e", "h"]`

## 3. Python Solution

```python
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

```

**Alternative Pythonic Solutions (also valid):**

While the two-pointer method is fundamental, Python offers more concise ways that also meet the requirements:

1.  **Using `list.reverse()` method:**
    ```python
    def reverseString_builtin(s: List[str]) -> None:
        s.reverse()
    ```
    This modifies the list in-place and is generally implemented efficiently (often in C), satisfying O(1) extra space.

2.  **Using Slice Assignment:**
    ```python
    def reverseString_slicing(s: List[str]) -> None:
        s[:] = s[::-1]
    ```
    `s[::-1]` creates a reversed *copy* of the list. The crucial part is `s[:] = ...`, which assigns the elements from the reversed copy back into the *original* list's memory space (slice assignment), thus performing an in-place modification. This also effectively uses O(1) extra space relative to the *final* state, although the intermediate reversed slice `s[::-1]` temporarily uses O(n) space. However, for LeetCode's O(1) space constraint in this context, slice assignment is usually accepted.

The two-pointer method is often preferred in interviews as it demonstrates a deeper understanding of the underlying algorithm without relying on language-specific built-ins.

**Complexity Analysis (Two-Pointer Method):**

*   **Time Complexity: O(n)**
    *   We iterate through roughly half of the list elements (`n/2`).
    *   In each iteration, we perform a constant number of operations (comparison, swap, increment, decrement).
    *   Therefore, the time complexity is proportional to `n`, which is O(n).
*   **Space Complexity: O(1)**
    *   We only use a few extra variables (`left`, `right`) to store indices.
    *   The space used by these variables does not grow with the size of the input list `s`.
    *   The swap operation in Python (`a, b = b, a`) might implicitly use a temporary variable, but this is still constant space.
    *   Therefore, the extra space complexity is O(1).

## 4. Test Cases

The Python code above includes a `run_test_case` helper function and several test cases to verify the `reverseString` function:

1.  **LeetCode Example 1:** `["h","e","l","l","o"]` -> `["o","l","l","e","h"]` (Odd length)
2.  **LeetCode Example 2:** `["H","a","n","n","a","h"]` -> `["h","a","n","n","a","H"]` (Even length, palindrome structure)
3.  **Single Element:** `["a"]` -> `["a"]` (Edge case)
4.  **Two Elements:** `["a", "b"]` -> `["b", "a"]` (Smallest case requiring a swap)
5.  **Even Length (Longer):** `["1", "2", "3", "4", "5", "6"]` -> `["6", "5", "4", "3", "2", "1"]`
6.  **Odd Length (Longer):** `["A", "B", "C", "D", "E"]` -> `["E", "D", "C", "B", "A"]`
7.  **Symbols:** `["!", "@", "#", "$"]` -> `["$", "#", "@", "!"]` (Test with non-alphanumeric characters)

These test cases cover various scenarios, including edge cases and different list lengths, ensuring the solution is robust.