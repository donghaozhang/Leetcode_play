from typing import Optional, Tuple

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_minimum_subtree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    找到和最小的子树
    :param root: TreeNode，二叉树根节点
    :return: TreeNode，和最小的子树的根节点
    """
    if not root:
        return None
        
    # 用于存储全局最小和及其对应的子树根节点
    min_sum = float('inf')
    result = None
    
    def get_subtree_sum(node: Optional[TreeNode]) -> int:
        """
        计算子树的和并更新全局最小值
        :param node: 当前节点
        :return: int，子树和
        """
        nonlocal min_sum, result
        
        if not node:
            return 0
            
        # 递归计算左右子树的和
        left_sum = get_subtree_sum(node.left)
        right_sum = get_subtree_sum(node.right)
        
        # 计算当前子树的总和
        curr_sum = left_sum + right_sum + node.val
        
        # 更新全局最小和
        if curr_sum < min_sum:
            min_sum = curr_sum
            result = node
            
        return curr_sum
    
    get_subtree_sum(root)
    return result

def test_find_minimum_subtree():
    """测试最小子树和的实现"""
    # 测试用例1：基本二叉树
    #      1
    #    /   \
    #   -5    2
    #  /  \  / \
    # 1    2 4  3
    root1 = TreeNode(1)
    root1.left = TreeNode(-5)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    result1 = find_minimum_subtree(root1)
    assert result1.val == -5, "Should find subtree with root value -5"
    
    # 测试用例2：单节点树
    root2 = TreeNode(1)
    result2 = find_minimum_subtree(root2)
    assert result2.val == 1, "Should return the only node"
    
    # 测试用例3：空树
    assert find_minimum_subtree(None) is None, \
        "Should handle empty tree"
    
    # 测试用例4：负值节点
    #     -1
    #    /  \
    #   2    3
    root4 = TreeNode(-1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    result4 = find_minimum_subtree(root4)
    assert result4.val == -1, "Should handle negative values"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_minimum_subtree() 