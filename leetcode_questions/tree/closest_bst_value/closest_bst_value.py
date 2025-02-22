from typing import Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_closest_value(root: Optional[TreeNode], target: float) -> int:
    """
    查找BST中最接近目标值的节点值（二分查找方法）
    :param root: TreeNode，二叉搜索树根节点
    :param target: float，目标值
    :return: int，最接近的值
    时间复杂度：O(H)，H是树高
    """
    if not root:
        return float('inf')
        
    closest = root.val
    
    while root:
        # 更新最接近值
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
            
        # 二分搜索
        if target < root.val:
            root = root.left
        elif target > root.val:
            root = root.right
        else:
            return root.val
            
    return closest

def find_closest_value_inorder(root: Optional[TreeNode], target: float) -> int:
    """
    查找BST中最接近目标值的节点值（中序遍历方法）
    :param root: TreeNode，二叉搜索树根节点
    :param target: float，目标值
    :return: int，最接近的值
    时间复杂度：O(N)，N是节点数
    """
    closest = [float('inf')]
    prev = [float('-inf')]
    
    def inorder(node: Optional[TreeNode]) -> None:
        if not node:
            return
            
        # 中序遍历左子树
        inorder(node.left)
        
        # 处理当前节点
        # 如果当前值比目标值大，比较当前值和前一个值哪个更接近
        if node.val >= target:
            if abs(node.val - target) < abs(closest[0] - target):
                closest[0] = node.val
            return
            
        # 更新closest和prev
        if abs(node.val - target) < abs(closest[0] - target):
            closest[0] = node.val
        prev[0] = node.val
        
        # 中序遍历右子树
        inorder(node.right)
    
    inorder(root)
    return closest[0]

def test_find_closest_value():
    """测试查找BST中最接近值的实现"""
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
    
    # 测试二分查找方法
    assert find_closest_value(root1, 3.7) == 4, "Should find closest value to 3.7"
    assert find_closest_value(root1, 5.2) == 5, "Should find closest value to 5.2"
    
    # 测试中序遍历方法
    assert find_closest_value_inorder(root1, 3.7) == 4, "Should find closest value to 3.7"
    assert find_closest_value_inorder(root1, 5.2) == 5, "Should find closest value to 5.2"
    
    # 测试用例2：单节点树
    root2 = TreeNode(1)
    assert find_closest_value(root2, 1.5) == 1, "Should handle single node tree"
    assert find_closest_value_inorder(root2, 1.5) == 1, "Should handle single node tree"
    
    # 测试用例3：空树
    assert find_closest_value(None, 1.0) == float('inf'), "Should handle empty tree"
    assert find_closest_value_inorder(None, 1.0) == float('inf'), "Should handle empty tree"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_closest_value() 