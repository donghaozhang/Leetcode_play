from typing import List, Optional

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    """
    找出从根节点到所有叶子节点的路径
    :param root: TreeNode，二叉树根节点
    :return: List[str]，所有路径的字符串表示
    """
    def dfs(node: Optional[TreeNode], path: List[str], paths: List[str]) -> None:
        """
        深度优先搜索生成路径
        :param node: 当前节点
        :param path: 当前路径
        :param paths: 存储所有路径
        """
        if not node:
            return
            
        # 将当前节点加入路径
        path.append(str(node.val))
        
        if not node.left and not node.right:  # 叶子节点
            paths.append('->'.join(path))
        else:
            # 递归处理左右子树
            dfs(node.left, path, paths)
            dfs(node.right, path, paths)
            
        # 回溯：移除当前节点
        path.pop()
    
    result = []
    dfs(root, [], result)
    return result

def test_binary_tree_paths():
    """测试二叉树路径的实现"""
    # 测试用例1：基本二叉树
    #      1
    #     / \
    #    2   3
    #     \
    #      5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    expected1 = ["1->2->5", "1->3"]
    assert sorted(binary_tree_paths(root1)) == sorted(expected1), \
        f"Expected {expected1}, but got {binary_tree_paths(root1)}"
    
    # 测试用例2：单节点树
    root2 = TreeNode(1)
    assert binary_tree_paths(root2) == ["1"], \
        "Should handle single node tree correctly"
    
    # 测试用例3：空树
    assert binary_tree_paths(None) == [], \
        "Should return empty list for empty tree"
    
    # 测试用例4：完全二叉树
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    expected4 = ["1->2->4", "1->2->5", "1->3"]
    assert sorted(binary_tree_paths(root4)) == sorted(expected4), \
        f"Expected {expected4}, but got {binary_tree_paths(root4)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_binary_tree_paths() 