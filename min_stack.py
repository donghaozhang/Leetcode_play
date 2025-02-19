class MinStack:
    def __init__(self):
        """
        初始化主栈和辅助栈
        """
        self.stack = []     # 主栈存储所有元素
        self.min_stack = [] # 辅助栈存储当前的最小值

    def push(self, x: int) -> None:
        """
        将元素 x 压入主栈，同时更新最小值辅助栈
        """
        self.stack.append(x)
        # 如果辅助栈为空或 x 小于等于当前最小值，则将 x 压入辅助栈
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        """
        弹出主栈顶元素，同时同步更新辅助栈
        """
        if not self.stack:
            return
        top_val = self.stack.pop()
        # 如果出栈的值等于当前辅助栈栈顶，则辅助栈也弹出
        if self.min_stack and top_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """
        返回主栈的栈顶元素
        """
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        """
        返回辅助栈的栈顶元素，即当前最小值
        """
        if not self.min_stack:
            raise IndexError("getMin from empty stack")
        return self.min_stack[-1]


# 测试代码
def test_min_stack():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3, f"Expected -3, got {min_stack.getMin()}"
    min_stack.pop()
    assert min_stack.top() == 0, f"Expected 0, got {min_stack.top()}"
    assert min_stack.getMin() == -2, f"Expected -2, got {min_stack.getMin()}"
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_min_stack() 