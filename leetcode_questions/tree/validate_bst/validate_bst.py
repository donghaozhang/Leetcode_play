from typing import Optional, Tuple

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    验证二叉搜索树
    :param root: TreeNode，二叉树根节点
    :return: bool，是否是有效的二叉搜索树
    """
    def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        """
        递归验证节点值是否在有效范围内
        :param node: 当前节点
        :param min_val: 最小值限制
        :param max_val: 最大值限制
        :return: bool，是否有效
        """
        if not node:
            return True
            
        # 检查当前节点值是否在有效范围内
        if node.val <= min_val or node.val >= max_val:
            return False
            
        # 递归验证左右子树
        return validate(node.left, min_val, node.val) and \
               validate(node.right, node.val, max_val)
    
    return validate(root, float('-inf'), float('inf'))

def test_is_valid_bst():
    """测试验证二叉搜索树的实现"""
    # 测试用例1：有效的BST
    #      5
    #    /   \
    #   3     7
    #  / \   / \
    # 1   4 6   8
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(8)
    assert is_valid_bst(root1), "Should be a valid BST"
    
    # 测试用例2：无效的BST（右子树有小于根节点的值）
    #      5
    #    /   \
    #   3     7
    #  / \   / \
    # 1   4 2   8
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(7)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(4)
    root2.right.left = TreeNode(2)  # 违反BST性质
    root2.right.right = TreeNode(8)
    assert not is_valid_bst(root2), "Should not be a valid BST"
    
    # 测试用例3：单节点树
    root3 = TreeNode(1)
    assert is_valid_bst(root3), "Single node should be a valid BST"
    
    # 测试用例4：空树
    assert is_valid_bst(None), "Empty tree should be a valid BST"
    
    # 测试用例5：包含相等值的树
    #      5
    #    /   \
    #   3     5
    root5 = TreeNode(5)
    root5.left = TreeNode(3)
    root5.right = TreeNode(5)
    assert not is_valid_bst(root5), "Tree with duplicate values should not be valid"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_is_valid_bst() 