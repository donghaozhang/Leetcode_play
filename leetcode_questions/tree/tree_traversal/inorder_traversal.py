from typing import List, Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    二叉树的中序遍历（递归实现）
    :param root: TreeNode，二叉树根节点
    :return: List[int]，遍历结果
    """
    result = []
    
    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        # 先访问左子树，再访问根节点，最后访问右子树
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result

def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    二叉树的中序遍历（迭代实现）
    :param root: TreeNode，二叉树根节点
    :return: List[int]，遍历结果
    """
    result = []
    stack = []
    curr = root
    
    while curr or stack:
        # 一直遍历到最左边的节点
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # 处理当前节点并转向右子树
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    
    return result

def test_inorder_traversal():
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
    
    expected = [4, 2, 5, 1, 3]
    
    # 测试递归实现
    assert inorder_traversal(root) == expected, \
        f"Recursive: Expected {expected}, but got {inorder_traversal(root)}"
    
    # 测试迭代实现
    assert inorder_traversal_iterative(root) == expected, \
        f"Iterative: Expected {expected}, but got {inorder_traversal_iterative(root)}"
    
    # 测试空树
    assert inorder_traversal(None) == [], "Should handle empty tree"
    assert inorder_traversal_iterative(None) == [], "Should handle empty tree"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_inorder_traversal() 