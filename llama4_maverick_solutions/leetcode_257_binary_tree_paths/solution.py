# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        """
        Returns all root-to-leaf paths in a binary tree.

        :param root: The root of the binary tree.
        :return: A list of strings representing root-to-leaf paths.
        """
        def dfs(node: TreeNode, path: str) -> None:
            """
            Performs a depth-first search on the binary tree.

            :param node: The current node.
            :param path: The current path.
            """
            if not node:
                return
            
            # Update the current path
            new_path = path + str(node.val) if not path else path + "->" + str(node.val)
            
            # If the node is a leaf, add the path to the result
            if not node.left and not node.right:
                result.append(new_path)
                return
            
            # Recursively explore the left and right subtrees
            dfs(node.left, new_path)
            dfs(node.right, new_path)

        result = []
        dfs(root, "")
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: root = [1,2,3,null,5]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    print(solution.binaryTreePaths(root1))  # Output: ["1->2->5", "1->3"]

    # Test case 2: root = [1]
    root2 = TreeNode(1)
    print(solution.binaryTreePaths(root2))  # Output: ["1"]
