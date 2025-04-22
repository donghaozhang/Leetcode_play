# Merge Two Sorted Lists

## Problem

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

## Examples

**Example 1:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**
```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**
```
Input: list1 = [], list2 = [0]
Output: [0]
```

## Constraints

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

## Approach: Two-Pointer Technique

The solution uses a two-pointer technique to merge the two sorted lists efficiently.

### Key Components:

1. **Dummy Head Node**:
   ```python
   dummy = ListNode(-1)
   current = dummy
   ```
   - Creates a dummy head to simplify the linked list construction
   - Allows us to easily return the merged list

2. **List Traversal**:
   ```python
   while list1 and list2:
       if list1.val <= list2.val:
           current.next = list1
           list1 = list1.next
       else:
           current.next = list2
           list2 = list2.next
       current = current.next
   ```
   - Compares nodes from both lists
   - Attaches the smaller node to the merged list
   - Moves the pointer of the list from which the node was taken

3. **Remaining Nodes**:
   ```python
   if list1:
       current.next = list1
   else:
       current.next = list2
   ```
   - Attaches any remaining nodes from either list
   - Handles cases where one list is longer than the other

## Complexity Analysis

- **Time Complexity**: O(n + m)
  - Where n and m are the lengths of the two linked lists
  - We process each node exactly once

- **Space Complexity**: O(1)
  - We only use a constant amount of extra space
  - The merged list is created by rearranging the existing nodes

## Why This Approach Works

1. **Efficiency**:
   - Processes each node exactly once
   - No additional space is needed for the merged list
   - Works with lists of different lengths

2. **Correctness**:
   - Maintains the sorted order of both lists
   - Properly handles empty lists
   - Preserves the original node structure

3. **Edge Cases**:
   - Handles empty lists
   - Handles lists of different lengths
   - Handles lists with duplicate values

## Example Walkthrough

For list1 = [1,2,4] and list2 = [1,3,4]:

1. **First Node**:
   - Compare 1 and 1
   - Attach first 1 from list1
   - Move list1 pointer

2. **Second Node**:
   - Compare 2 and 1
   - Attach 1 from list2
   - Move list2 pointer

3. **Third Node**:
   - Compare 2 and 3
   - Attach 2 from list1
   - Move list1 pointer

4. **Fourth Node**:
   - Compare 4 and 3
   - Attach 3 from list2
   - Move list2 pointer

5. **Fifth Node**:
   - Compare 4 and 4
   - Attach first 4 from list1
   - Move list1 pointer

6. **Final Node**:
   - Attach remaining 4 from list2
   - Result: [1,1,2,3,4,4] 