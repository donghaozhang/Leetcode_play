# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive solution
        def recursive_helper(node, result):
            if node:
                result.append(node.val)
                recursive_helper(node.left, result)
                recursive_helper(node.right, result)
        
        result = []
        recursive_helper(root, result)
        return result

        # Uncomment below for iterative solution
        # if not root:
        #     return []
        # stack = [root]
        # result = []
        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return result
