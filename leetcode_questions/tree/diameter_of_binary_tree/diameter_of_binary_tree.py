from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def maxdepth(root):
            if root == None:
                return 0
            left_height = maxdepth(root.left)
            right_height = maxdepth(root.right)
            self.result = max(self.result, left_height + right_height)
            return max(left_height, right_height) + 1
        
        maxdepth(root)
        return self.result

# Helper function to build a binary tree from a list (level-order traversal)
def build_tree_from_list(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        node = queue.pop(0)
        
        # Left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
def test_diameter_of_binary_tree():
    solution = Solution()
    
    # Test case 1: Example 1 from the problem
    # Tree structure:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    nodes1 = [1, 2, 3, 4, 5]
    root1 = build_tree_from_list(nodes1)
    print("Test Case 1:")
    print("Input: [1,2,3,4,5]")
    print(f"Output: {solution.diameterOfBinaryTree(root1)}")
    print("Expected: 3 (path: 4->2->1->3 or 5->2->1->3)")
    print()
    
    # Test case 2: Example 2 from the problem
    # Tree structure:
    #   1
    #  /
    # 2
    nodes2 = [1, 2]
    root2 = build_tree_from_list(nodes2)
    print("Test Case 2:")
    print("Input: [1,2]")
    print(f"Output: {solution.diameterOfBinaryTree(root2)}")
    print("Expected: 1 (path: 2->1)")
    print()
    
    # Test case 3: Single node
    nodes3 = [1]
    root3 = build_tree_from_list(nodes3)
    print("Test Case 3:")
    print("Input: [1]")
    print(f"Output: {solution.diameterOfBinaryTree(root3)}")
    print("Expected: 0 (no path)")
    print()
    
    # Test case 4: Long path through root
    # Tree structure:
    #      1
    #     / \
    #    2   3
    #   /     \
    #  4       5
    # /         \
    #6           7
    nodes4 = [1, 2, 3, 4, None, None, 5, 6, None, None, None, None, None, None, 7]
    root4 = build_tree_from_list(nodes4)
    print("Test Case 4:")
    print("Input: [1,2,3,4,null,null,5,6,null,null,null,null,null,null,7]")
    print(f"Output: {solution.diameterOfBinaryTree(root4)}")
    print("Expected: 5 (path: 6->4->2->1->3->5->7)")
    
    # Test case 5: Long path not through root
    # Tree structure:
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    # /     \
    #6       7
    solution.result = 0  # Reset the result for a new test case
    nodes5 = [1, 2, 3, 4, 5, None, None, 6, None, None, 7]
    root5 = build_tree_from_list(nodes5)
    print("\nTest Case 5:")
    print("Input: [1,2,3,4,5,null,null,6,null,null,7]")
    print(f"Output: {solution.diameterOfBinaryTree(root5)}")
    print("Expected: 4 (path: 6->4->2->5->7)")

if __name__ == "__main__":
    test_diameter_of_binary_tree() 