from typing import Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def find_lca(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    查找两个节点的最近公共祖先（无父指针版本）
    :param root: TreeNode，二叉树根节点
    :param p: TreeNode，第一个节点
    :param q: TreeNode，第二个节点
    :return: TreeNode，最近公共祖先节点
    """
    if not root or root == p or root == q:
        return root
        
    # 在左右子树中查找p和q
    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)
    
    # 如果p和q分别在左右子树中，则root就是LCA
    if left and right:
        return root
        
    # 否则返回非空的那个结果
    return left if left else right

def find_lca_with_parent(p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    查找两个节点的最近公共祖先（有父指针版本）
    :param p: TreeNode，第一个节点
    :param q: TreeNode，第二个节点
    :return: TreeNode，最近公共祖先节点
    """
    # 记录p的所有祖先节点
    ancestors = set()
    while p:
        ancestors.add(p)
        p = p.parent
        
    # 查找q的祖先中第一个也是p的祖先的节点
    while q:
        if q in ancestors:
            return q
        q = q.parent
        
    return None

def test_find_lca():
    """测试最近公共祖先的实现"""
    # 测试用例1：基本二叉树
    #      3
    #    /   \
    #   5     1
    #  / \   / \
    # 6   2 0   8
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    
    p1, q1 = root1.left, root1.right  # 节点5和1
    result1 = find_lca(root1, p1, q1)
    assert result1.val == 3, "Should find root as LCA"
    
    # 测试用例2：一个节点是另一个的祖先
    p2, q2 = root1.left, root1.left.right  # 节点5和2
    result2 = find_lca(root1, p2, q2)
    assert result2.val == 5, "Should find ancestor node as LCA"
    
    # 测试用例3：带父指针的树
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    
    # 构建树结构和父指针
    node1.left = node2
    node1.right = node3
    node2.parent = node1
    node3.parent = node1
    node2.left = node4
    node2.right = node5
    node4.parent = node2
    node5.parent = node2
    
    result3 = find_lca_with_parent(node4, node5)
    assert result3.val == 2, "Should find correct LCA with parent pointers"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_lca() 