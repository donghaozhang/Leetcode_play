import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the k-th smallest element in a Binary Search Tree using iterative in-order traversal.

        Args:
            root: The root node of the BST.
            k: The index (1-based) of the desired smallest element.

        Returns:
            The value of the k-th smallest element.
        """
        stack = []
        current = root
        count = 0

        while current or stack:
            # 1. Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # 2. Visit the node popped from the stack (in-order)
            #    This node is the next smallest in the sequence.
            current = stack.pop()
            count += 1

            # 3. Check if this is the k-th node visited
            if count == k:
                return current.val

            # 4. Move to the right subtree to continue the in-order traversal
            current = current.right

        # This part should theoretically not be reached if 1 <= k <= n
        return -1 # Or raise an error

# Helper function to build a BST from a list (level-order) for testing
def build_bst_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = collections.deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()

        # Process left child
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i >= len(values):
            break

        # Process right child
        if values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# --- Test Cases ---
solver = Solution()

# Example 1
root1 = build_bst_from_list([3, 1, 4, None, 2])
k1 = 1
expected1 = 1
result1 = solver.kthSmallest(root1, k1)
print(f"Test Case 1: Input root=[3,1,4,null,2], k={k1}")
print(f"Expected: {expected1}")
print(f"Result: {result1}")
print(f"Pass: {result1 == expected1}\n")

# Example 2
root2 = build_bst_from_list([5, 3, 6, 2, 4, None, None, 1])
k2 = 3
expected2 = 3
result2 = solver.kthSmallest(root2, k2)
print(f"Test Case 2: Input root=[5,3,6,2,4,null,null,1], k={k2}")
print(f"Expected: {expected2}")
print(f"Result: {result2}")
print(f"Pass: {result2 == expected2}\n")

# Additional Test Case 1: k = n (largest element)
root3 = build_bst_from_list([5, 3, 6, 2, 4, None, None, 1]) # n = 6
k3 = 6
expected3 = 6
result3 = solver.kthSmallest(root3, k3)
print(f"Test Case 3: Input root=[5,3,6,2,4,null,null,1], k={k3}")
print(f"Expected: {expected3}")
print(f"Result: {result3}")
print(f"Pass: {result3 == expected3}\n")

# Additional Test Case 2: Skewed tree
root4 = build_bst_from_list([1, None, 2, None, 3, None, 4, None, 5]) # n = 5
k4 = 4
expected4 = 4
result4 = solver.kthSmallest(root4, k4)
print(f"Test Case 4: Input root=[1,null,2,null,3,null,4,null,5], k={k4}")
print(f"Expected: {expected4}")
print(f"Result: {result4}")
print(f"Pass: {result4 == expected4}\n")

# Additional Test Case 3: Single node tree
root5 = build_bst_from_list([1]) # n = 1
k5 = 1
expected5 = 1
result5 = solver.kthSmallest(root5, k5)
print(f"Test Case 5: Input root=[1], k={k5}")
print(f"Expected: {expected5}")
print(f"Result: {result5}")
print(f"Pass: {result5 == expected5}\n")
