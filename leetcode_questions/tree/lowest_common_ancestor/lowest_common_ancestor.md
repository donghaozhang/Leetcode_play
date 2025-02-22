# 最近公共祖先

## 题目描述
给定一棵二叉树，找到两个节点的最近公共祖先（LCA）。
最近公共祖先是两个节点的公共祖先中，离它们最近的祖先节点。

## 示例
输入:
```
     3
   /   \
  5     1
 / \   / \
6   2 0   8
```
对于节点5和1，输出: 节点3
对于节点5和2，输出: 节点5

## 解题思路

### 方法一：递归查找（无父指针）
1. **核心思想**
   - 自底向上查找目标节点
   - 利用后序遍历的特性
   - 判断节点分布情况

2. **实现细节**
```python
def find_lca(root, p, q):
    if not root or root == p or root == q:
        return root
        
    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)
    
    if left and right:
        return root
    return left if left else right
```

### 方法二：利用父指针
1. **核心思想**
   - 记录一个节点的所有祖先
   - 查找另一个节点的祖先链
   - 找到第一个公共节点

2. **实现细节**
```python
def find_lca_with_parent(p, q):
    ancestors = set()
    while p:
        ancestors.add(p)
        p = p.parent
        
    while q:
        if q in ancestors:
            return q
        q = q.parent
```

## 复杂度分析
- 方法一：
  - 时间复杂度：O(N)，N是节点数
  - 空间复杂度：O(H)，H是树高
- 方法二：
  - 时间复杂度：O(H)，H是树高
  - 空间复杂度：O(H)

## 代码实现要点
1. 正确处理空节点
2. 处理目标节点是祖先的情况
3. 高效查找公共祖先
4. 父指针的正确使用

## 常见错误
1. 未考虑空树情况
2. 未处理节点不存在的情况
3. 递归返回值处理错误
4. 父指针使用不当

## 优化策略
1. 使用哈希表存储祖先
2. 路径压缩
3. 提前返回特殊情况
4. 避免重复遍历

## 相关题目
1. 二叉搜索树的最近公共祖先
2. 最深公共祖先
3. 带父指针的二叉树遍历
4. 二叉树的序列化与反序列化 