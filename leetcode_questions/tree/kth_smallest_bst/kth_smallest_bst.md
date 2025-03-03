# BST中第k小的元素

## 题目描述
给定一棵二叉搜索树（BST）和一个整数k，找到树中第k小的元素。

## 示例
输入:
```
     5
   /   \
  3     7
 / \   / \
2   4 6   8
```
k = 3
输出: 4

## 解题思路

### 中序遍历
1. **核心思想**
   - BST的中序遍历是升序序列
   - 计数访问的节点数
   - 找到第k个访问的节点

2. **实现细节**
```python
def inorder(node):
    if not node or result[0] is not None:
        return
        
    inorder(node.left)
    
    count[0] += 1
    if count[0] == k:
        result[0] = node.val
        return
        
    inorder(node.right)
```

## 复杂度分析
- 时间复杂度：
  - 平均情况：O(H + k)，H是树高，k是目标位置
  - 最坏情况：O(N)，N是节点总数
  - 原因：需要遍历根到目标节点的路径，以及所有小于目标节点的节点
- 空间复杂度：O(H)，递归栈的深度

### 复杂度分析详解
1. **为什么是O(H + k)**
   - 需要O(H)时间找到最小节点
   - 然后需要O(k)时间访问k个节点
   - 在平衡BST中，H = logN

2. **最坏情况分析**
   - 当树退化为链表时，H = N
   - 当k = N时，需要访问所有节点
   - 因此最坏情况是O(N)

## 代码实现要点
1. 正确实现中序遍历
2. 维护访问节点计数
3. 及时终止遍历
4. 处理边界情况

## 常见错误
1. 遍历顺序错误
2. 计数逻辑错误
3. 未处理空树
4. 未处理k超出范围

## 优化策略
1. 使用迭代实现减少空间
2. 记录节点数提前判断
3. 维护节点计数信息
4. 缓存常用查询结果

## 相关题目
1. BST的中序遍历
2. BST的验证
3. BST的插入和删除
4. BST的前驱和后继 