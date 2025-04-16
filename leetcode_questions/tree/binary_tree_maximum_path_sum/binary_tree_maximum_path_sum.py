from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxval = float('-inf')
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_gain(node):
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain
            
            # update max_sum if it's better to start a new path
            self.maxval = max(self.maxval, price_newpath)
            
            # for recursion:
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)
   
        self.maxval = float('-inf')  # Reset maxval for each new test case
        max_gain(root)
        return self.maxval

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
def test_max_path_sum():
    solution = Solution()
    
    # Test case 1: Example 1 from the problem
    # Tree structure:
    #     1
    #    / \
    #   2   3
    nodes1 = [1, 2, 3]
    root1 = build_tree_from_list(nodes1)
    print("Test Case 1:")
    print("Input: [1,2,3]")
    print(f"Output: {solution.maxPathSum(root1)}")
    print("Expected: 6 (path: 2 -> 1 -> 3)")
    print()
    
    # Test case 2: Example 2 from the problem
    # Tree structure:
    #     -10
    #     / \
    #    9  20
    #      /  \
    #     15   7
    nodes2 = [-10, 9, 20, None, None, 15, 7]
    root2 = build_tree_from_list(nodes2)
    print("Test Case 2:")
    print("Input: [-10,9,20,null,null,15,7]")
    print(f"Output: {solution.maxPathSum(root2)}")
    print("Expected: 42 (path: 15 -> 20 -> 7)")
    print()
    
    # Test case 3: Single node
    nodes3 = [5]
    root3 = build_tree_from_list(nodes3)
    print("Test Case 3:")
    print("Input: [5]")
    print(f"Output: {solution.maxPathSum(root3)}")
    print("Expected: 5 (path: 5)")
    print()
    
    # Test case 4: All negative values
    nodes4 = [-3, -2, -1]
    root4 = build_tree_from_list(nodes4)
    print("Test Case 4:")
    print("Input: [-3,-2,-1]")
    print(f"Output: {solution.maxPathSum(root4)}")
    print("Expected: -1 (path: -1)")
    print()
    
    # Test case 5: Complex tree with both positive and negative values
    nodes5 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    root5 = build_tree_from_list(nodes5)
    print("Test Case 5:")
    print("Input: [5,4,8,11,null,13,4,7,2,null,null,null,1]")
    print(f"Output: {solution.maxPathSum(root5)}")
    print("Expected: 48 (path: 11 -> 4 -> 5 -> 8 -> 13)")

if __name__ == "__main__":
    test_max_path_sum() 