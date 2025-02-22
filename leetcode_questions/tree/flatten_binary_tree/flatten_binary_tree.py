from typing import Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten_binary_tree(root: Optional[TreeNode]) -> None:
    """
    将二叉树展开为链表（前序遍历顺序）
    :param root: TreeNode，二叉树根节点
    """
    if not root:
        return
        
    # 记录上一个访问的节点
    last = [None]
    
    def preorder(node: Optional[TreeNode]) -> None:
        """
        前序遍历并重构树
        :param node: 当前节点
        """
        if not node:
            return
            
        # 保存原始的左右子树
        left = node.left
        right = node.right
        
        # 将当前节点连接到链表
        if last[0]:
            last[0].right = node
            last[0].left = None
        last[0] = node
        
        # 递归处理左右子树
        preorder(left)
        preorder(right)
    
    preorder(root)

def tree_to_list(root: Optional[TreeNode]) -> list:
    """将展开后的树转换为列表（用于测试）"""
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result

def test_flatten_binary_tree():
    """测试二叉树展开为链表的实现"""
    # 测试用例1：基本二叉树
    #      1
    #    /   \
    #   2     5
    #  / \     \
    # 3   4     6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(6)
    
    flatten_binary_tree(root1)
    assert tree_to_list(root1) == [1, 2, 3, 4, 5, 6], \
        "Should correctly flatten binary tree"
    
    # 测试用例2：单节点树
    root2 = TreeNode(1)
    flatten_binary_tree(root2)
    assert tree_to_list(root2) == [1], \
        "Should handle single node tree"
    
    # 测试用例3：空树
    flatten_binary_tree(None)
    assert tree_to_list(None) == [], \
        "Should handle empty tree"
    
    # 测试用例4：左偏树
    #   1
    #  /
    # 2
    #/
    #3
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    
    flatten_binary_tree(root4)
    assert tree_to_list(root4) == [1, 2, 3], \
        "Should handle left-skewed tree"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_flatten_binary_tree() 