from typing import Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    翻转二叉树
    :param root: TreeNode，二叉树根节点
    :return: TreeNode，翻转后的二叉树根节点
    """
    if not root:
        return None
        
    # 交换左右子树
    root.left, root.right = root.right, root.left
    
    # 递归翻转左右子树
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    
    return root

def tree_to_list(root: Optional[TreeNode]) -> list:
    """将二叉树转换为层序遍历列表（用于测试）"""
    if not root:
        return []
        
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result

def test_invert_binary_tree():
    """测试翻转二叉树的实现"""
    # 测试用例1：基本二叉树
    #      4            4
    #    /   \       /   \
    #   2     7  => 7     2
    #  / \   / \   / \   / \
    # 1   3 6   9 9   6 3   1
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    
    inverted1 = invert_binary_tree(root1)
    assert tree_to_list(inverted1) == [4, 7, 2, 9, 6, 3, 1], \
        "Should correctly invert a complete binary tree"
    
    # 测试用例2：单节点树
    root2 = TreeNode(1)
    inverted2 = invert_binary_tree(root2)
    assert tree_to_list(inverted2) == [1], \
        "Should handle single node tree"
    
    # 测试用例3：空树
    assert invert_binary_tree(None) is None, \
        "Should handle empty tree"
    
    # 测试用例4：不平衡树
    #   1         1
    #  /           \
    # 2     =>      2
    #  \           /
    #   3         3
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.right = TreeNode(3)
    
    inverted4 = invert_binary_tree(root4)
    assert tree_to_list(inverted4) == [1, 2, 3], \
        "Should correctly invert an unbalanced tree"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_invert_binary_tree() 