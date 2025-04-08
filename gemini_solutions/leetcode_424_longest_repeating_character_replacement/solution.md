# window_sum.md)
- 最长重复字符替换 / Longest Repeating Character Replacement [LeetCode 424]

## Problem Description

```markdown
### 424. Longest Repeating Character Replacement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

**Example 1:**

**Input:** s = "ABAB", k = 2
**Output:** 4
**Explanation:** Replace the two 'A's with two 'B's or vice versa.

**Example 2:**

**Input:** s = "AABABBA", k = 1
**Output:** 4
**Explanation:** Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may be other ways to achieve this answer too.

**Constraints:**

*   `1 <= s.length <= 10^5`
*   `s` consists of only uppercase English letters.
*   `0 <= k <= s.length`
```

## Solution

Okay, let's break down the "Longest Repeating Character Replacement" problem (LeetCode 424).

**1. Explanation of the Problem**

You're given a string `s` consisting of uppercase English letters and an integer `k`. You can change any character in the string to any other uppercase English letter up to `k` times. The goal is to find the length of the longest possible substring within `s` that can be made to consist of only a single, repeating character after performing at most `k` changes within that substring.

For example, if `s = "AABABBA"` and `k = 1`:
- Consider the substring "AABA" (length 4). It has 3 'A's and 1 'B'. We need to change 1 character (the 'B') to make it "AAAA". Since `1 <= k`, this is possible.
- Consider the substring "ABBA" (length 4). It has 2 'A's and 2 'B's. To make it "AAAA", we need 2 changes. To make it "BBBB", we need 2 changes. Since `k = 1`, we cannot make this substring consist of a single character.
- Consider the substring "BABB" (length 4). It has 1 'A' and 3 'B's. We need to change 1 character (the 'A') to make it "BBBB". Since `1 <= k`, this is possible.

The longest such substring we found has length 4.

**2. Step-by-Step Approach (Sliding Window)**

This problem screams "sliding window" because we're looking for the longest *substring* (a contiguous part of the string) that satisfies a certain property. The property involves counts of characters within the window and a limit `k`.

Here's the sliding window strategy:

1.  **Initialization:**
    *   Use two pointers, `left` and `right`, to define the current window `s[left...right]`. Initialize `left = 0`.
    *   Use a frequency map (like a dictionary or a fixed-size array of 26 for uppercase letters) called `counts` to store the counts of each character within the current window.
    *   Initialize `max_freq = 0`. This will store the frequency of the *most frequent* character within the current window.
    *   Initialize `max_len = 0`. This will store the maximum valid window length found so far.

2.  **Expand Window:**
    *   Iterate the `right` pointer from `0` to `len(s) - 1`.
    *   For each character `s[right]`:
        *   Increment its count in the `counts` map.
        *   Update `max_freq = max(max_freq, counts[s[right]])`. This keeps track of the highest frequency encountered for *any* character within the window ending at `right`.

3.  **Check Window Validity & Shrink if Necessary:**
    *   The current window size is `window_len = right - left + 1`.
    *   To make this window consist of only the most frequent character, we need to change all *other* characters. The number of changes required is `window_len - max_freq`.
    *   The window is valid *if* the number of changes needed is less than or equal to `k`: `window_len - max_freq <= k`.
    *   If the window is *invalid* (`window_len - max_freq > k`), we need to shrink the window from the left until it becomes valid again.
        *   Decrement the count of the character `s[left]` in the `counts` map.
        *   Increment the `left` pointer.
        *   **Optimization:** We *don't* need to recalculate `max_freq` precisely when shrinking. The `max_freq` we maintain represents the maximum frequency seen *so far* in windows ending at `right`. If the condition `window_len - max_freq > k` is met even with this potentially overestimated `max_freq`, the window is definitely invalid and needs shrinking. This optimization avoids iterating through the counts map on every shrink step.

4.  **Update Maximum Length:**
    *   After potentially shrinking the window (in step 3), the current window `s[left...right]` is guaranteed to be the largest possible window *ending at `right`* that satisfies the condition (or could potentially satisfy it if `max_freq` increases).
    *   The length of this window is `right - left + 1`.
    *   Update the overall maximum length found: `max_len = max(max_len, right - left + 1)`.

5.  **Return Result:**
    *   After the `right` pointer has traversed the entire string, `max_len` will hold the length of the longest valid substring. Return `max_len`.

**3. Python Solution**

```python
import collections

class Solution:
    """
    Solves the Longest Repeating Character Replacement problem using a sliding window.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring containing the same letter
        after performing at most k replacements.

        Args:
            s: The input string.
            k: The maximum number of replacements allowed.

        Returns:
            The length of the longest valid substring.
        """
        n = len(s)
        if n == 0:
            return 0

        counts = collections.defaultdict(int) # Frequency map for chars in window
        left = 0                             # Left pointer of the window
        max_len = 0                          # Stores the maximum valid window length found
        max_freq = 0                         # Stores the frequency of the most frequent char in the window

        for right in range(n):
            # Expand the window by including the character at 'right'
            current_char = s[right]
            counts[current_char] += 1

            # Update the frequency of the most frequent character in the window
            # This is the maximum frequency seen *so far* in any window ending at 'right'
            max_freq = max(max_freq, counts[current_char])

            # Calculate the number of characters we need to replace in the current window
            # window_length = right - left + 1
            # replacements_needed = window_length - max_freq
            replacements_needed = (right - left + 1) - max_freq

            # Check if the current window is valid (needs <= k replacements)
            # If not, shrink the window from the left until it becomes valid
            if replacements_needed > k:
                # Remove the character at 'left' from the window
                left_char = s[left]
                counts[left_char] -= 1
                # Optional: clean up count if it becomes zero
                # if counts[left_char] == 0:
                #     del counts[left_char]

                # Move the left pointer one step to the right
                left += 1
                # NOTE: We DO NOT need to recalculate max_freq here.
                # The logic relies on max_freq being the max frequency encountered.
                # If the window is invalid, shrinking it by moving 'left' maintains
                # or decreases the window size. max_len tracks the largest valid size.

            # Update the maximum length found so far.
            # The current window size (right - left + 1) represents the largest
            # window ending at 'right' that could potentially satisfy the condition.
            max_len = max(max_len, right - left + 1)

        return max_len

# --- Test Cases ---

def run_tests():
    sol = Solution()
    test_cases = [
        # Provided Examples
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),

        # Edge Cases
        ("AAAA", 2, 4),        # Already repeating
        ("ABCDE", 1, 2),       # Small k, diverse string
        ("ABBB", 2, 4),        # k allows changing the single 'A'
        ("AAAB", 0, 3),        # k = 0, find longest existing repeating substring
        ("BAAA", 0, 3),        # k = 0
        ("A", 1, 1),           # Single character string
        ("", 1, 0),            # Empty string
        ("ABCDEFG", 0, 1),     # k = 0, all unique chars

        # More Complex Cases
        ("ABAA", 0, 2),
        ("ABBBACDEFG", 2, 5), # Window "BBBBA" -> change A, C -> needs 2 <= k=2. Length 5.
        ("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 7, 10) # Requires careful tracing or running
    ]

    print("Running Test Cases...\n")
    passed_all = True
    for i, (s, k, expected) in enumerate(test_cases):
        result = sol.characterReplacement(s, k)
        status = "Passed" if result == expected else "Failed"
        if result != expected:
            passed_all = False
        print(f"Test Case {i + 1}:")
        print(f"  Input:    s='{s}', k={k}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {result}")
        print(f"  Result:   {status}")
        print("-" * 25)

    print(f"\nOverall Result: {'All tests passed!' if passed_all else 'Some tests failed.'}")

# To run the tests:
run_tests()

```

**Complexity Analysis:**

*   **Time Complexity:** O(N), where N is the length of the string `s`. The `right` pointer iterates through the string exactly once. The `left` pointer also moves forward at most N times. Operations inside the loop (dictionary access/update, max calculation) take O(1) time on average (or O(alpha) where alpha is the alphabet size, 26 here, which is constant). Therefore, the overall time complexity is linear.
*   **Space Complexity:** O(1) or O(alpha). The `counts` dictionary (or array) stores frequencies for at most 26 distinct uppercase English characters. Thus, the space used is constant, independent of the input string length N.

This sliding window approach efficiently finds the longest substring satisfying the condition within the given constraints.