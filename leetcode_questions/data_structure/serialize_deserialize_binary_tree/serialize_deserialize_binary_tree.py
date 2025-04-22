from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    Serialize and deserialize a binary tree.
    Uses level order traversal to match LeetCode's serialization format.
    """
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Serialized string representation of the tree
        """
        if not root:
            return ""
            
        flat_bt = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                flat_bt.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                flat_bt.append("")
                
        return ",".join(flat_bt)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded data to tree.
        
        Args:
            data: Serialized string representation of the tree
            
        Returns:
            Root of the reconstructed binary tree
        """
        if not data:
            return None
            
        flat_bt = data.split(",")
        root = TreeNode(int(flat_bt[0]))
        queue = deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()
            
            if i < len(flat_bt) and flat_bt[i]:
                node.left = TreeNode(int(flat_bt[i]))
                queue.append(node.left)
            i += 1
            
            if i < len(flat_bt) and flat_bt[i]:
                node.right = TreeNode(int(flat_bt[i]))
                queue.append(node.right)
            i += 1
            
        return root

# Test cases
if __name__ == "__main__":
    # Example 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    codec = Codec()
    serialized = codec.serialize(root)
    print("Example 1:")
    print("Serialized:", serialized)
    deserialized = codec.deserialize(serialized)
    print("Deserialized:", codec.serialize(deserialized))
    
    # Example 2: Empty tree
    print("\nExample 2:")
    serialized = codec.serialize(None)
    print("Serialized:", serialized)
    deserialized = codec.deserialize(serialized)
    print("Deserialized:", codec.serialize(deserialized))
    
    # Example 3: Single node
    print("\nExample 3:")
    root = TreeNode(1)
    serialized = codec.serialize(root)
    print("Serialized:", serialized)
    deserialized = codec.deserialize(serialized)
    print("Deserialized:", codec.serialize(deserialized)) 