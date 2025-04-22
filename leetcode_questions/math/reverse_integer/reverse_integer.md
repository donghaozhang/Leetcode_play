# Reverse Integer

## Problem

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], then return 0.

## Examples

**Example 1:**
```
Input: x = 123
Output: 321
```

**Example 2:**
```
Input: x = -123
Output: -321
```

**Example 3:**
```
Input: x = 120
Output: 21
```

## Constraints

- -2³¹ <= x <= 2³¹ - 1

## Approach: Digit by Digit Reversal

The solution uses a digit-by-digit approach to reverse the integer while checking for overflow at each step.

### Key Components:

1. **Sign Handling**:
   ```python
   sign = [1, -1][x < 0]  # Determine the sign of the input
   rev, x = 0, abs(x)     # Work with positive numbers
   ```

2. **Digit Extraction and Reversal**:
   ```python
   while x:
       x, mod = divmod(x, 10)  # Get the last digit
       rev = rev * 10 + mod    # Build the reversed number
   ```

3. **Overflow Check**:
   ```python
   if rev > 2**31 - 1:
       return 0
   ```

## Complexity Analysis

- **Time Complexity**: O(log x)
  - The number of iterations is equal to the number of digits in x
  - Each iteration performs constant time operations

- **Space Complexity**: O(1)
  - We use a constant amount of extra space
  - No additional data structures are required

## Why This Approach Works

1. **Efficiency**:
   - Processes each digit exactly once
   - Uses constant space
   - Early termination on overflow detection

2. **Correctness**:
   - Properly handles negative numbers
   - Correctly detects and handles overflow
   - Preserves leading zeros in the reversed number

3. **Edge Cases**:
   - Handles single-digit numbers
   - Handles zero
   - Handles numbers with trailing zeros
   - Handles maximum and minimum 32-bit integers

## Example Walkthrough

For x = 123:

1. **Initial Setup**:
   - sign = 1 (positive)
   - rev = 0
   - x = 123

2. **First Iteration**:
   - x, mod = divmod(123, 10) → x = 12, mod = 3
   - rev = 0 * 10 + 3 = 3

3. **Second Iteration**:
   - x, mod = divmod(12, 10) → x = 1, mod = 2
   - rev = 3 * 10 + 2 = 32

4. **Third Iteration**:
   - x, mod = divmod(1, 10) → x = 0, mod = 1
   - rev = 32 * 10 + 1 = 321

5. **Final Result**:
   - Return sign * rev = 1 * 321 = 321

The solution efficiently reverses the digits while maintaining the sign and checking for overflow at each step. 