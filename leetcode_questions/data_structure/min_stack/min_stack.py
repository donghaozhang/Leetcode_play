class MinStack:
    """
    A stack that supports push, pop, top, and retrieving the minimum element in constant time.
    """
    def __init__(self):
        """
        Initialize the stack with an empty list.
        Each element in the stack is a tuple (value, current_min)
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        Push element val onto stack.
        
        Args:
            val: The value to push onto the stack
        """
        if not self.stack:
            self.stack.append((val, val))
            return
        
        current_min = self.stack[-1][1]
        self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        """
        Remove the element on top of the stack.
        """
        self.stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack.
        
        Returns:
            The top element of the stack
        """
        return self.stack[-1][0]

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        
        Returns:
            The minimum element in the stack
        """
        return self.stack[-1][1]

# Test cases
if __name__ == "__main__":
    # Example 1
    print("Example 1:")
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # -3
    minStack.pop()
    print(minStack.top())     # 0
    print(minStack.getMin())  # -2
    
    # Example 2: Single element
    print("\nExample 2:")
    minStack = MinStack()
    minStack.push(5)
    print(minStack.getMin())  # 5
    print(minStack.top())     # 5
    
    # Example 3: Multiple elements with same min
    print("\nExample 3:")
    minStack = MinStack()
    minStack.push(3)
    minStack.push(3)
    minStack.push(3)
    print(minStack.getMin())  # 3
    minStack.pop()
    print(minStack.getMin())  # 3 