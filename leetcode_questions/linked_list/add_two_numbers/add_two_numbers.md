# Add Two Numbers

## Problem

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Examples

**Example 1:**
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Constraints

- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

## Approach: Digit-by-Digit Addition with Carry

The solution uses a digit-by-digit addition approach similar to how we add numbers manually, handling carry values appropriately.

### Key Components:

1. **Dummy Head Node**:
   ```python
   dummyHead = ListNode(0)
   curr = dummyHead
   ```
   - Creates a dummy head to simplify the linked list construction
   - Allows us to easily return the result list

2. **Carry Handling**:
   ```python
   carry = columnSum // 10
   newNode = ListNode(columnSum % 10)
   ```
   - Tracks the carry value for each digit addition
   - Creates new nodes with the appropriate digit value

3. **Node Traversal**:
   ```python
   l1 = l1.next if l1 else None
   l2 = l2.next if l2 else None
   ```
   - Handles lists of different lengths
   - Continues until both lists are exhausted and no carry remains

## Complexity Analysis

- **Time Complexity**: O(max(n, m))
  - Where n and m are the lengths of the two linked lists
  - We process each node exactly once

- **Space Complexity**: O(max(n, m))
  - The length of the new list is at most max(n, m) + 1
  - We create a new list to store the result

## Why This Approach Works

1. **Efficiency**:
   - Processes each digit exactly once
   - Handles carry values efficiently
   - Works with numbers of different lengths

2. **Correctness**:
   - Properly handles carry propagation
   - Correctly handles edge cases (zero, single digit)
   - Maintains the reverse order of digits

3. **Edge Cases**:
   - Handles lists of different lengths
   - Handles carry at the end of addition
   - Handles zero values appropriately

## Example Walkthrough

For l1 = [2,4,3] and l2 = [5,6,4]:

1. **First Digit**:
   - 2 + 5 = 7, carry = 0
   - New node: 7

2. **Second Digit**:
   - 4 + 6 = 10, carry = 1
   - New node: 0

3. **Third Digit**:
   - 3 + 4 + 1 (carry) = 8, carry = 0
   - New node: 8

4. **Result**:
   - [7, 0, 8] representing 807 