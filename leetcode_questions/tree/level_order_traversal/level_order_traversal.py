from typing import List, Optional
from collections import deque

class TreeNode:
    """二叉树节点"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_single_queue(root: Optional[TreeNode]) -> List[List[int]]:
    """
    使用单队列实现层序遍历
    :param root: TreeNode, 二叉树根节点
    :return: List[List[int]], 层序遍历结果
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    
    return result

def level_order_double_queue(root: Optional[TreeNode]) -> List[List[int]]:
    """
    使用双队列实现层序遍历
    :param root: TreeNode, 二叉树根节点
    :return: List[List[int]], 层序遍历结果
    """
    if not root:
        return []
    
    result = []
    current_queue = [root]
    
    while current_queue:
        next_queue = []
        current_level = []
        
        for node in current_queue:
            current_level.append(node.val)
            
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
                
        result.append(current_level)
        current_queue = next_queue
    
    return result

def level_order_dummy_node(root: Optional[TreeNode]) -> List[List[int]]:
    """
    使用哑节点实现层序遍历
    :param root: TreeNode, 二叉树根节点
    :return: List[List[int]], 层序遍历结果
    """
    if not root:
        return []
    
    result = []
    current_level = []
    queue = deque([root, None])  # None 作为层分隔符
    
    while queue:
        node = queue.popleft()
        
        if node is None:
            result.append(current_level)
            current_level = []
            if queue:  # 还有节点要处理
                queue.append(None)
            continue
            
        current_level.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def test_level_order():
    """测试三种实现方法"""
    # 构建测试树
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    expected = [[3], [9, 20], [15, 7]]
    
    # 测试三种实现
    assert level_order_single_queue(root) == expected, "Single queue implementation failed"
    assert level_order_double_queue(root) == expected, "Double queue implementation failed"
    assert level_order_dummy_node(root) == expected, "Dummy node implementation failed"
    
    # 测试空树
    assert level_order_single_queue(None) == [], "Should handle empty tree"
    assert level_order_double_queue(None) == [], "Should handle empty tree"
    assert level_order_dummy_node(None) == [], "Should handle empty tree"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_level_order() 