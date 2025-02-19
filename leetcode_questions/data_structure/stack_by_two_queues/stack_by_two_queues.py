from collections import deque

class MyStack:
    def __init__(self):
        """
        初始化两个队列：q1 用于存储栈元素，q2 用作辅助队列。
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        将元素 x 压入栈中。
        时间复杂度 O(n)。
        """
        # 将 x 入队到 q2 中
        self.q2.append(x)
        # 将 q1 中的所有元素转移到 q2 中，使得 x 位于前端
        while self.q1:
            self.q2.append(self.q1.popleft())
        # 交换 q1 和 q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        移除并返回栈顶元素。
        时间复杂度 O(1)。
        """
        if self.q1:
            return self.q1.popleft()
        raise IndexError("pop from empty stack")

    def top(self) -> int:
        """
        获取栈顶元素。
        """
        if self.q1:
            return self.q1[0]
        raise IndexError("top from empty stack")

    def empty(self) -> bool:
        """
        如果栈为空则返回 True，否则返回 False。
        """
        return len(self.q1) == 0


# 测试代码
def test_my_stack():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    # 现在栈中的顺序应为 [2, 1]，栈顶为 2
    assert stack.top() == 2, f"Expected top is 2, got {stack.top()}"
    assert stack.pop() == 2, f"Expected pop returns 2, got {stack.pop()}"
    assert not stack.empty(), "Expected stack is not empty"
    assert stack.pop() == 1, "Expected pop returns 1"
    assert stack.empty(), "Expected stack is empty"
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_my_stack() 