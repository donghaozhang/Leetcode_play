# 用两个栈实现队列问题解析

## 问题描述
使用两个栈来实现队列的以下操作：
- **push(x)**：将元素 x 推入队列尾部
- **pop()**：从队列首部移除元素并返回该元素
- **peek()**：返回队列首部的元素
- **empty()**：判断队列是否为空

要求除了栈以外，不能使用其他数据结构。

例如：
```
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
```

## 解题思路

### 方法：双栈模拟
使用两个栈 `stack1` 和 `stack2` 来实现队列：
- `stack1` 用于处理入队操作（push）
- `stack2` 用于处理出队操作（pop/peek）

1. **push 操作**
   - 直接将元素压入 stack1

2. **pop/peek 操作**
   - 如果 stack2 为空，将 stack1 中的所有元素依次弹出并压入 stack2
   - 从 stack2 弹出/查看栈顶元素
   - 这样可以实现先进先出的顺序

3. **empty 操作**
   - 当两个栈都为空时，队列为空

### 关键点
- 只有在 stack2 为空时，才需要将 stack1 的元素转移到 stack2
- 一旦转移，必须将 stack1 的所有元素都转移到 stack2
- 在 stack2 非空时，不能进行转移操作，否则会打乱顺序

## 复杂度分析
- **push**：O(1)
- **pop**：均摊 O(1)
  - 最坏情况下需要 O(n) 将 stack1 的元素转移到 stack2
  - 但每个元素最多只会被转移一次
- **peek**：与 pop 相同
- **empty**：O(1)

## 空间复杂度
- O(n)，其中 n 是队列中元素的数量
- 所有元素都需要存储在两个栈中的某一个 