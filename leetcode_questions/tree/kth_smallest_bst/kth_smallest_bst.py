from typing import Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """
    查找BST中第k小的元素
    :param root: TreeNode，二叉搜索树根节点
    :param k: int，目标位置
    :return: int，第k小的元素值
    """
    # 记录当前访问的节点数和结果
    count = [0]
    result = [None]
    
    def inorder(node: Optional[TreeNode]) -> None:
        """
        中序遍历BST
        :param node: 当前节点
        """
        if not node or result[0] is not None:
            return
            
        # 访问左子树
        inorder(node.left)
        
        # 处理当前节点
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
            
        # 访问右子树
        inorder(node.right)
    
    inorder(root)
    return result[0]

def test_find_kth_smallest():
    """测试查找BST中第k小元素的实现"""
    # 测试用例1：基本BST
    #      5
    #    /   \
    #   3     7
    #  / \   / \
    # 2   4 6   8
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(8)
    
    assert find_kth_smallest(root1, 1) == 2, "Should find 1st smallest element"
    assert find_kth_smallest(root1, 3) == 4, "Should find 3rd smallest element"
    assert find_kth_smallest(root1, 7) == 8, "Should find 7th smallest element"
    
    # 测试用例2：单节点树
    root2 = TreeNode(1)
    assert find_kth_smallest(root2, 1) == 1, "Should handle single node tree"
    
    # 测试用例3：左偏树
    #   3
    #  /
    # 2
    #/
    #1
    root3 = TreeNode(3)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(1)
    
    assert find_kth_smallest(root3, 1) == 1, "Should handle left-skewed tree"
    assert find_kth_smallest(root3, 2) == 2, "Should handle left-skewed tree"
    assert find_kth_smallest(root3, 3) == 3, "Should handle left-skewed tree"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_kth_smallest() 