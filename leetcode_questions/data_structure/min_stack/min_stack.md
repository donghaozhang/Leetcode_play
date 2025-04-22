# Min Stack

## Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- `MinStack()` initializes the stack object
- `void push(int val)` pushes the element val onto the stack
- `void pop()` removes the element on the top of the stack
- `int top()` gets the top element of the stack
- `int getMin()` retrieves the minimum element in the stack

You must implement a solution with O(1) time complexity for each function.

## Examples

**Example 1:**
```
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## Constraints

- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin

## Approach: Stack with Min Tracking

The solution uses a stack where each element is a tuple containing:
1. The actual value
2. The minimum value in the stack up to that point

This approach allows us to maintain the minimum value in O(1) time while still supporting all other stack operations in O(1) time.

### Key Components:

1. **Stack Structure**:
   ```python
   def __init__(self):
       self.stack = []  # Each element is (value, current_min)
   ```

2. **Push Operation**:
   ```python
   def push(self, val: int) -> None:
       if not self.stack:
           self.stack.append((val, val))
           return
       
       current_min = self.stack[-1][1]
       self.stack.append((val, min(val, current_min)))
   ```

3. **Pop Operation**:
   ```python
   def pop(self) -> None:
       self.stack.pop()
   ```

4. **Top Operation**:
   ```python
   def top(self) -> int:
       return self.stack[-1][0]
   ```

5. **Get Minimum Operation**:
   ```python
   def getMin(self) -> int:
       return self.stack[-1][1]
   ```

## Complexity Analysis

- **Time Complexity**:
  - push: O(1)
  - pop: O(1)
  - top: O(1)
  - getMin: O(1)
  - All operations are constant time as required

- **Space Complexity**:
  - O(n) where n is the number of elements in the stack
  - Each element requires storage for both its value and the current minimum

## Why This Approach Works

1. **Efficiency**:
   - All operations are O(1) time
   - No need to recalculate minimum on pop
   - No need to maintain a separate data structure

2. **Correctness**:
   - Each element knows the minimum up to that point
   - When an element is popped, the next element already has the correct minimum
   - Handles all edge cases (empty stack, single element, etc.)

3. **Memory Optimization**:
   - Only stores necessary information
   - No redundant data
   - Efficient use of space

## Example Walkthrough

For the input sequence [-2, 0, -3]:

1. **Push -2**:
   - Stack: [(-2, -2)]
   - Current min: -2

2. **Push 0**:
   - Stack: [(-2, -2), (0, -2)]
   - Current min: -2

3. **Push -3**:
   - Stack: [(-2, -2), (0, -2), (-3, -3)]
   - Current min: -3

4. **Pop**:
   - Stack: [(-2, -2), (0, -2)]
   - Current min: -2

The minimum is always available in O(1) time by looking at the second element of the top tuple. 