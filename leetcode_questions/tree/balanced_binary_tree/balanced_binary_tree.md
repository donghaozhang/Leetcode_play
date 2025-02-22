# 平衡二叉树

## 题目描述
给定一棵二叉树，判断它是否是平衡二叉树。
平衡二叉树的定义：任意节点的左右子树高度差不超过1。

## 示例
输入:
```
    1
   / \
  2   3
 / \
4   5
```
输出: true

输入:
```
    1
   /
  2
 /
3
```
输出: false

## 解题思路

### 自底向上（推荐）
1. **核心思想**
   - 后序遍历
   - 同时返回子树高度和是否平衡
   - 避免重复计算高度

2. **实现细节**
```python
def check_height(node):
    if not node:
        return True, 0
        
    left_balanced, left_height = check_height(node.left)
    right_balanced, right_height = check_height(node.right)
    
    if not left_balanced or not right_balanced:
        return False, 0
        
    if abs(left_height - right_height) > 1:
        return False, 0
        
    return True, max(left_height, right_height) + 1
```

### 自顶向下（不推荐）
1. **核心思想**
   - 分别计算左右子树高度
   - 存在重复计算
   - 时间复杂度较高

## 复杂度分析
- 时间复杂度：O(N)，每个节点只访问一次
- 空间复杂度：O(H)，H是树的高度，递归栈的深度

## 代码实现要点
1. 正确计算树高
2. 及时返回不平衡状态
3. 处理空节点情况
4. 避免重复计算

## 常见错误
1. 只检查当前节点
2. 忽略子树的平衡性
3. 高度计算错误
4. 重复计算树高

## 优化策略
1. 使用后序遍历
2. 合并高度计算和平衡检查
3. 提前返回不平衡状态
4. 避免重复遍历

## 相关题目
1. 二叉树的最大深度
2. 二叉树的最小深度
3. 验证二叉搜索树
4. 完全二叉树的判定 