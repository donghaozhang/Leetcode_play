from typing import Optional, List

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    """
    二叉搜索树迭代器
    使用栈实现中序遍历的迭代器模式
    """
    def __init__(self, root: Optional[TreeNode]):
        """
        初始化迭代器
        :param root: TreeNode，二叉搜索树的根节点
        """
        self.stack = []
        # 将最左路径节点全部入栈
        self._push_left(root)
    
    def _push_left(self, node: Optional[TreeNode]) -> None:
        """
        将节点及其所有左子节点入栈
        :param node: TreeNode，当前节点
        """
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        """
        返回二叉搜索树中的下一个最小值
        :return: int，下一个最小值
        """
        if not self.hasNext():
            return -1
        
        # 弹出栈顶节点（当前最小值）
        curr = self.stack.pop()
        # 将右子树的最左路径入栈
        self._push_left(curr.right)
        
        return curr.val
    
    def hasNext(self) -> bool:
        """
        判断是否还有下一个值
        :return: bool，是否存在下一个值
        """
        return len(self.stack) > 0

def test_bst_iterator():
    """测试二叉搜索树迭代器"""
    
    def create_bst(values: List[int], index: int = 0) -> Optional[TreeNode]:
        """
        根据层序遍历数组创建二叉搜索树
        :param values: List[int]，层序遍历数组
        :param index: int，当前索引
        :return: TreeNode，创建的二叉树根节点
        """
        if not values or index >= len(values) or values[index] is None:
            return None
        
        root = TreeNode(values[index])
        root.left = create_bst(values, 2 * index + 1)
        root.right = create_bst(values, 2 * index + 2)
        return root
    
    # 测试用例1：基本二叉搜索树
    #       7
    #      / \
    #     3   15
    #        /  \
    #       9    20
    bst1 = create_bst([7, 3, 15, None, None, 9, 20])
    iterator1 = BSTIterator(bst1)
    result1 = []
    while iterator1.hasNext():
        result1.append(iterator1.next())
    assert result1 == [3, 7, 9, 15, 20], f"Expected [3, 7, 9, 15, 20], but got {result1}"
    
    # 测试用例2：空树
    iterator2 = BSTIterator(None)
    assert not iterator2.hasNext(), "Empty tree should have no next element"
    
    # 测试用例3：单节点树
    bst3 = TreeNode(1)
    iterator3 = BSTIterator(bst3)
    assert iterator3.hasNext(), "Single node tree should have one element"
    assert iterator3.next() == 1, "Should return the only node value"
    assert not iterator3.hasNext(), "Should have no more elements"
    
    # 测试用例4：左倾树
    #     3
    #    /
    #   2
    #  /
    # 1
    bst4 = TreeNode(3)
    bst4.left = TreeNode(2)
    bst4.left.left = TreeNode(1)
    iterator4 = BSTIterator(bst4)
    result4 = []
    while iterator4.hasNext():
        result4.append(iterator4.next())
    assert result4 == [1, 2, 3], f"Expected [1, 2, 3], but got {result4}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_bst_iterator() 