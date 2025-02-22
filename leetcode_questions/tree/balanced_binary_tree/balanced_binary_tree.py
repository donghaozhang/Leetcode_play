from typing import Optional, Tuple

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    判断二叉树是否平衡
    :param root: TreeNode，二叉树根节点
    :return: bool，是否是平衡二叉树
    """
    def check_height(node: Optional[TreeNode]) -> Tuple[bool, int]:
        """
        检查子树是否平衡并返回高度
        :param node: 当前节点
        :return: (是否平衡, 树高)
        """
        if not node:
            return True, 0
            
        # 检查左子树
        left_balanced, left_height = check_height(node.left)
        if not left_balanced:
            return False, 0
            
        # 检查右子树
        right_balanced, right_height = check_height(node.right)
        if not right_balanced:
            return False, 0
            
        # 检查当前节点是否平衡
        if abs(left_height - right_height) > 1:
            return False, 0
            
        # 返回当前树是否平衡及其高度
        return True, max(left_height, right_height) + 1
    
    balanced, _ = check_height(root)
    return balanced

def test_is_balanced():
    """测试平衡二叉树判断的实现"""
    # 测试用例1：平衡二叉树
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    assert is_balanced(root1), "Should be balanced"
    
    # 测试用例2：不平衡二叉树
    #      1
    #     /
    #    2
    #   /
    #  3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    assert not is_balanced(root2), "Should not be balanced"
    
    # 测试用例3：空树
    assert is_balanced(None), "Empty tree should be balanced"
    
    # 测试用例4：单节点树
    root4 = TreeNode(1)
    assert is_balanced(root4), "Single node tree should be balanced"
    
    # 测试用例5：复杂平衡树
    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    root5.left.left = TreeNode(4)
    root5.right.right = TreeNode(5)
    assert is_balanced(root5), "Should be balanced"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_is_balanced() 