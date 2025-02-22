from typing import List, Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    二叉树的先序遍历（递归实现）
    :param root: TreeNode，二叉树根节点
    :return: List[int]，遍历结果
    """
    result = []
    
    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        # 先访问根节点，再访问左右子树
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result

def preorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    二叉树的先序遍历（迭代实现）
    :param root: TreeNode，二叉树根节点
    :return: List[int]，遍历结果
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # 先压入右子节点，再压入左子节点，这样出栈时就是先左后右
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

def test_preorder_traversal():
    # 构建测试用例
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    expected = [1, 2, 4, 5, 3]
    
    # 测试递归实现
    assert preorder_traversal(root) == expected, \
        f"Recursive: Expected {expected}, but got {preorder_traversal(root)}"
    
    # 测试迭代实现
    assert preorder_traversal_iterative(root) == expected, \
        f"Iterative: Expected {expected}, but got {preorder_traversal_iterative(root)}"
    
    # 测试空树
    assert preorder_traversal(None) == [], "Should handle empty tree"
    assert preorder_traversal_iterative(None) == [], "Should handle empty tree"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_preorder_traversal() 