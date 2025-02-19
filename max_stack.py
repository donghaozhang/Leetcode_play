class MaxStack:
    def __init__(self):
        """
        初始化主栈和辅助栈
        """
        self.stack = []      # 主栈存储所有元素
        self.max_stack = []  # 辅助栈存储到当前为止的最大值

    def push(self, x: int) -> None:
        """
        将元素 x 压入主栈，同时更新辅助栈
        """
        self.stack.append(x)
        if self.max_stack:
            self.max_stack.append(max(x, self.max_stack[-1]))
        else:
            self.max_stack.append(x)

    def pop(self) -> int:
        """
        弹出并返回主栈的栈顶元素，同时同步辅助栈
        """
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        """
        返回主栈栈顶的元素
        """
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def peekMax(self) -> int:
        """
        返回当前栈中的最大元素（辅助栈栈顶）
        """
        if not self.max_stack:
            raise IndexError("peekMax from empty stack")
        return self.max_stack[-1]

    def popMax(self) -> int:
        """
        移除并返回栈中的最大元素（靠近栈顶的那个最大值）
        """
        if not self.stack:
            raise IndexError("popMax from empty stack")
        max_val = self.peekMax()
        buffer = []
        # 弹出元素直到遇到最大值
        while self.top() != max_val:
            buffer.append(self.pop())
        # 弹出该最大值
        self.pop()  # 此操作会弹出 max_val
        # 将临时存储的元素重新压入栈中
        while buffer:
            self.push(buffer.pop())
        return max_val


# 测试代码
def test_max_stack():
    max_stack = MaxStack()
    max_stack.push(5)
    max_stack.push(1)
    max_stack.push(5)
    assert max_stack.top() == 5, f"Expected top 5, got {max_stack.top()}"
    assert max_stack.peekMax() == 5, f"Expected peekMax 5, got {max_stack.peekMax()}"
    # popMax 应该移除靠近栈顶的那个最大值，即最后一个5
    assert max_stack.popMax() == 5, f"Expected popMax 5, got {max_stack.popMax()}"
    # 现在栈中剩下 [5,1]，top为1
    assert max_stack.top() == 1, f"Expected top 1, got {max_stack.top()}"
    assert max_stack.peekMax() == 5, f"Expected peekMax 5, got {max_stack.peekMax()}"
    # 如果 pop，则会移除1
    assert max_stack.pop() == 1, f"Expected pop 1, got {max_stack.pop()}"
    # 现在栈中只剩下 [5]
    assert max_stack.top() == 5, f"Expected top 5, got {max_stack.top()}"
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_max_stack() 