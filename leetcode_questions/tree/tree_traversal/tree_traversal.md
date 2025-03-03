# 二叉树的三种遍历

## 题目描述
实现二叉树的三种基本遍历方式：
1. 先序遍历（Pre-order）：根->左->右
2. 中序遍历（In-order）：左->根->右
3. 后序遍历（Post-order）：左->右->根

要求：每种遍历都提供递归和迭代两种实现方式。

## 示例
输入:
```
    1
   / \
  2   3
 / \
4   5
```

输出:
- 先序遍历: [1, 2, 4, 5, 3]
- 中序遍历: [4, 2, 5, 1, 3]
- 后序遍历: [4, 5, 2, 3, 1]

## 解题思路

### 1. 递归实现
- 定义递归函数，处理当前节点
- 根据遍历顺序调用递归函数和添加节点值
- 递归终止条件是节点为空

### 2. 迭代实现
- 使用栈来模拟递归过程
- 先序遍历：直接压栈，先右后左
- 中序遍历：一直往左走，处理节点后转向右子树
- 后序遍历：使用标记法或双栈法

### 复杂度分析
- 时间复杂度：O(n)，n是节点数量
- 空间复杂度：
  - 递归：O(h)，h是树的高度
  - 迭代：O(h)，h是树的高度

## 代码实现要点
1. 正确理解三种遍历的顺序
2. 迭代实现时注意栈的使用
3. 处理空树的边界情况
4. 保持代码的可读性和可维护性

## 应用场景
1. 先序遍历：树的序列化、目录打印
2. 中序遍历：二叉搜索树的有序遍历
3. 后序遍历：树的释放、求表达式值

## 常见错误
1. 遍历顺序混淆
2. 栈操作顺序错误
3. 递归终止条件不完整
4. 未处理边界情况 