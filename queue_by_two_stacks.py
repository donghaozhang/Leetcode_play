class MyQueue:
    def __init__(self):
        """
        初始化两个栈：
        stack1 用于处理入队操作
        stack2 用于处理出队操作
        """
        self.stack1 = []  # 用于入队
        self.stack2 = []  # 用于出队

    def push(self, x: int) -> None:
        """
        将元素 x 推入队列尾部
        """
        self.stack1.append(x)

    def _transfer(self) -> None:
        """
        当 stack2 为空时，将 stack1 中的所有元素转移到 stack2
        这样可以实现先进先出的顺序
        """
        if not self.stack2:  # 只有在 stack2 为空时才进行转移
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        """
        从队列首部移除元素并返回该元素
        """
        if self.empty():
            raise IndexError("pop from empty queue")
            
        self._transfer()
        return self.stack2.pop()

    def peek(self) -> int:
        """
        返回队列首部的元素
        """
        if self.empty():
            raise IndexError("peek from empty queue")
            
        self._transfer()
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        判断队列是否为空
        """
        return not self.stack1 and not self.stack2


# 测试代码
def test_my_queue():
    queue = MyQueue()
    
    # 测试用例 1：基本操作
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1, "peek 操作失败"
    assert queue.pop() == 1, "pop 操作失败"
    assert not queue.empty(), "empty 操作失败"
    
    # 测试用例 2：多次 push 和 pop
    queue.push(3)
    queue.push(4)
    assert queue.pop() == 2, "pop 操作失败"
    assert queue.pop() == 3, "pop 操作失败"
    assert queue.pop() == 4, "pop 操作失败"
    assert queue.empty(), "empty 操作失败"
    
    # 测试用例 3：交替 push 和 pop
    queue.push(5)
    assert queue.pop() == 5, "pop 操作失败"
    queue.push(6)
    queue.push(7)
    assert queue.peek() == 6, "peek 操作失败"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_my_queue() 