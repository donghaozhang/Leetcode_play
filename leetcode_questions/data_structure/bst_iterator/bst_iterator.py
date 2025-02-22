from typing import Optional, List

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    """二叉搜索树迭代器"""
    def __init__(self, root: Optional[TreeNode]):
        """
        初始化迭代器
        :param root: 二叉搜索树的根节点
        """
        self.stack = []
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, root: Optional[TreeNode]) -> None:
        """
        将当前节点到最左叶子节点的路径上的所有节点入栈
        :param root: 当前节点
        """
        while root:
            self.stack.append(root)
            root = root.left
            
    def next(self) -> int:
        """
        返回二叉搜索树中的下一个最小值
        :return: int，下一个最小值
        """
        topmost_node = self.stack.pop()
        
        # 如果当前节点有右子树，将右子树的最左路径入栈
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
            
        return topmost_node.val
        
    def hasNext(self) -> bool:
        """
        判断是否还有下一个值
        :return: bool，是否存在下一个值
        """
        return len(self.stack) > 0

def test_bst_iterator():
    """测试二叉搜索树迭代器的实现"""
    # 构建测试用的二叉搜索树
    #     7
    #    / \
    #   3   15
    #      /  \
    #     9    20
    
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    
    # 测试用例1：基本功能测试
    iterator1 = BSTIterator(root)
    result1 = []
    while iterator1.hasNext():
        result1.append(iterator1.next())
    assert result1 == [3, 7, 9, 15, 20], f"Expected [3, 7, 9, 15, 20], but got {result1}"
    
    # 测试用例2：空树
    iterator2 = BSTIterator(None)
    assert not iterator2.hasNext(), "Empty tree should have no next element"
    
    # 测试用例3：单节点树
    root3 = TreeNode(1)
    iterator3 = BSTIterator(root3)
    assert iterator3.next() == 1, "Should return the only value"
    assert not iterator3.hasNext(), "Should have no more elements"
    
    # 测试用例4：左倾树
    root4 = TreeNode(3)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(1)
    iterator4 = BSTIterator(root4)
    result4 = []
    while iterator4.hasNext():
        result4.append(iterator4.next())
    assert result4 == [1, 2, 3], f"Expected [1, 2, 3], but got {result4}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_bst_iterator() 