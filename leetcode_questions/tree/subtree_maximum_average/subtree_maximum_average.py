from typing import Optional, Tuple

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_subtree_with_max_average(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    找到平均值最大的子树
    :param root: TreeNode，二叉树根节点
    :return: TreeNode，平均值最大的子树的根节点
    """
    if not root:
        return None
        
    # 用于存储全局最大平均值和对应的子树根节点
    max_avg = float('-inf')
    result = None
    
    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
        """
        深度优先搜索计算子树的和与节点数
        :param node: 当前节点
        :return: (子树节点值之和, 子树节点数)
        """
        nonlocal max_avg, result
        
        if not node:
            return 0, 0
            
        # 递归计算左右子树的和与节点数
        left_sum, left_count = dfs(node.left)
        right_sum, right_count = dfs(node.right)
        
        # 计算当前子树的总和与节点数
        curr_sum = left_sum + right_sum + node.val
        curr_count = left_count + right_count + 1
        
        # 计算当前子树的平均值
        curr_avg = curr_sum / curr_count
        
        # 更新全局最大平均值
        if curr_avg > max_avg:
            max_avg = curr_avg
            result = node
            
        return curr_sum, curr_count
    
    dfs(root)
    return result

def test_find_subtree_with_max_average():
    """测试最大平均值子树的实现"""
    # 测试用例1：基本二叉树
    #      1
    #     / \
    #    5   3
    #   /   / \
    #  4   2   6
    root1 = TreeNode(1)
    root1.left = TreeNode(5)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.right.left = TreeNode(2)
    root1.right.right = TreeNode(6)
    result1 = find_subtree_with_max_average(root1)
    assert result1.val == 3, "Should find subtree with root value 3"
    
    # 测试用例2：单节点树
    root2 = TreeNode(1)
    result2 = find_subtree_with_max_average(root2)
    assert result2.val == 1, "Should return the only node"
    
    # 测试用例3：空树
    assert find_subtree_with_max_average(None) is None, \
        "Should handle empty tree"
    
    # 测试用例4：负值节点
    #     -1
    #    /  \
    #   2    3
    root4 = TreeNode(-1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    result4 = find_subtree_with_max_average(root4)
    assert result4.val == 3, "Should handle negative values"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_subtree_with_max_average() 