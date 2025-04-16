# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive solution
    def isSymmetric(self, root: 'TreeNode') -> bool:
        if root is None:
            return True
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.val == right.val and 
                self.dfs(left.left, right.right) and 
                self.dfs(left.right, right.left))
    
    # Iterative solution
    def isSymmetricIterative(self, root: 'TreeNode') -> bool:
        if root is None:
            return True
        
        queue = [(root.left, root.right)]
        
        while queue:
            left, right = queue.pop(0)
            
            if left is None and right is None:
                continue
            
            if left is None or right is None:
                return False
            
            if left.val != right.val:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True 

# Test cases
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

def test_symmetric_tree():
    solution = Solution()
    
    # Test case 1: Symmetric tree [1,2,2,3,4,4,3]
    # Should return True
    nodes1 = [1, 2, 2, 3, 4, 4, 3]
    root1 = build_tree_from_list(nodes1)
    print("Test Case 1 (Recursive):", solution.isSymmetric(root1))
    print("Test Case 1 (Iterative):", solution.isSymmetricIterative(root1))
    
    # Test case 2: Non-symmetric tree [1,2,2,null,3,null,3]
    # Should return False
    nodes2 = [1, 2, 2, None, 3, None, 3]
    root2 = build_tree_from_list(nodes2)
    print("Test Case 2 (Recursive):", solution.isSymmetric(root2))
    print("Test Case 2 (Iterative):", solution.isSymmetricIterative(root2))
    
    # Test case 3: Empty tree
    # Should return True
    root3 = None
    print("Test Case 3 (Recursive):", solution.isSymmetric(root3))
    print("Test Case 3 (Iterative):", solution.isSymmetricIterative(root3))
    
    # Test case 4: Tree with only root
    # Should return True
    root4 = TreeNode(1)
    print("Test Case 4 (Recursive):", solution.isSymmetric(root4))
    print("Test Case 4 (Iterative):", solution.isSymmetricIterative(root4))
    
    # Test case 5: Another non-symmetric tree [1,2,3]
    # Should return False
    nodes5 = [1, 2, 3]
    root5 = build_tree_from_list(nodes5)
    print("Test Case 5 (Recursive):", solution.isSymmetric(root5))
    print("Test Case 5 (Iterative):", solution.isSymmetricIterative(root5))

if __name__ == "__main__":
    test_symmetric_tree() 