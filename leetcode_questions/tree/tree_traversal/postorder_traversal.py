from typing import List, Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    二叉树的后序遍历（递归实现）
    :param root: TreeNode，二叉树根节点
    :return: List[int]，遍历结果
    """
    result = []
    
    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        # 先访问左右子树，再访问根节点
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    
    dfs(root)
    return result

def postorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    二叉树的后序遍历（迭代实现）
    :param root: TreeNode，二叉树根节点
    :return: List[int]，遍历结果
    """
    if not root:
        return []
    
    result = []
    stack = [(root, False)]  # (节点, 是否已访问过右子树)
    
    while stack:
        node, visited = stack.pop()
        
        if visited:
            # 如果已经访问过右子树，就可以访问当前节点
            result.append(node.val)
        else:
            # 按照 根->右->左 的顺序压栈，这样出栈顺序就是 左->右->根
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
    
    return result

def test_postorder_traversal():
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
    
    expected = [4, 5, 2, 3, 1]
    
    # 测试递归实现
    assert postorder_traversal(root) == expected, \
        f"Recursive: Expected {expected}, but got {postorder_traversal(root)}"
    
    # 测试迭代实现
    assert postorder_traversal_iterative(root) == expected, \
        f"Iterative: Expected {expected}, but got {postorder_traversal_iterative(root)}"
    
    # 测试空树
    assert postorder_traversal(None) == [], "Should handle empty tree"
    assert postorder_traversal_iterative(None) == [], "Should handle empty tree"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_postorder_traversal() 