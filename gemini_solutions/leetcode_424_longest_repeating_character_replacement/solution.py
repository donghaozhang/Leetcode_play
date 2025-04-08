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

